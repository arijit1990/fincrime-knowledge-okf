---
type: Source Digest
title: A Survey of Predictive Modelling under Imbalanced Distributions - part 3 of 5 (pp. 23-33)
description: 'Verified paraphrased digest, pp. 23-33: A Survey of Predictive Modelling under Imbalanced Distributions > 4 Modelling Strategies for Handling Imbalanced Domains; A Survey of Predictive Modelling under Imbalanced Distributions > 5 Related Problems; A Survey of Predictive Modelling under Imbalanced Distributions > 6 Conclusions; and 1 more sections'
resource: https://arxiv.org/abs/1505.01658
tags:
- academic_finding
- fraud_screening_synergies
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-a-survey-of-predictive-modelling-under-imbalanced-distributions
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2015-05-07'
legal_status: unknown
part: 3
parts_total: 5
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
  resource: https://arxiv.org/abs/1505.01658
  title: A Survey of Predictive Modelling under Imbalanced Distributions
  author: org:arxiv
  last_modified: '2015-05-07T00:00:00Z'
digest_points: 65
---

# A Survey of Predictive Modelling under Imbalanced Distributions (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 23-33) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.2 Special-purpose Learning Methods

- **descriptive / context**: Algorithm-modification approaches require deep knowledge of both the learning algorithm and the target domain, and understanding why the algorithm fails under skewed distributions is essential before modifying it. (p. 23)[^original]  
  <sub>anchor: "It requires a deep knowledge of both the learning algorithm and the target domain."</sub>
- **descriptive / limitation**: Some algorithm adaptations assume a cost or cost-benefit matrix is known for the different error types, which is frequently not the case in practice. (p. 23)[^original]  
  <sub>anchor: "Also, some of the adaptations assume that a cost/cost-benefit matrix is known for different error types, which is frequently not the case."</sub>
- **descriptive / finding or result**: Algorithm-modification methods are described as very effective in the contexts for which they were designed. (p. 23)[^original]  
  <sub>anchor: "On the other hand, these methods have the advantage of being very effective in the contexts for which they were designed."</sub>
- **descriptive / definition**: Learning-level solutions for imbalanced domains modify the algorithm preference criteria. (p. 23)[^original]  
  <sub>anchor: "Existing solutions for dealing with imbalanced domains at the learning level are focused on the introduction of modifications in the algorithm preference criteria."</sub>
- **descriptive / context**: Table 4 summarises the main bibliographic references for strategies involving algorithm modifications. (p. 23)[^original]  
  <sub>anchor: "Table 4 summarizes the main bibliographic references for strategies involving modifications of algorithms."</sub>
- **descriptive / definition**: Cost-sensitive algorithms minimise total cost, where misclassified examples may carry different costs; in imbalanced settings misclassifying a minority example costs more than misclassifying a majority example, and correct predictions usually carry no cost. (p. 23)[^original]  
  <sub>anchor: "In an imbalanced context, the cost of misclassifying a minority class example is superior to the cost of misclassifying a majority class example"</sub>
- **descriptive / context**: Maloof (2003) addressed the impact of incorporating costs into decision trees under imbalanced domains. (p. 23)[^original]  
  <sub>anchor: "For decision trees, the impact of the incorporation of costs under imbalanced domains was addressed by Maloof (2003)"</sub>
- **descriptive / method**: Cost-sensitive SVMs have been built by assigning different penalties to false negatives and false positives (Akbani et al., 2004) or by a weighted attribute strategy (Yuanhong et al., 2009), among other approaches (Weiguo et al., 2012). (p. 23)[^original]  
  <sub>anchor: "such as assigning different penalties to false negatives and positives (Akbani et al., 2004) or including a weighted attribute strategy (Yuanhong et al., 2009)"</sub>
- **descriptive / method**: Cost-sensitive neural network work includes Zhou and Liu (2006), Alejo et al. (2007) and Oh (2011). (p. 23)[^original]  
  <sub>anchor: "Regarding neural networks, the possibility of making them cost-sensitive has also been considered (e.g. Zhou and Liu (2006); Alejo et al. (2007); Oh (2011))."</sub>
- **descriptive / method**: Castro and de Pádua Braga (2013) proposed a Cost-Sensitive Multilayer Perceptron (CSMLP) for asymmetrical MLP learning via a modified backpropagation weight update rule. (p. 24)[^original]  
  <sub>anchor: "A Cost-Sensitive Multilayer Perceptron (CSMLP) algorithm was proposed by Castro and de P´adua Braga (2013)"</sub>
- **descriptive / method**: Cao et al. (2013) present a framework for cost-sensitive neural networks using Particle Swarm Optimization to optimise misclassification cost, feature subset and intrinsic structure parameters. (p. 24)[^original]  
  <sub>anchor: "Cao et al. (2013) present a framework for improving the performance of cost-sensitive neural networks"</sub>
- **descriptive / method**: Alejo et al. (2007) propose two strategies for imbalanced domains using RBF neural networks that include a cost function in the training phase. (p. 24)[^original]  
  <sub>anchor: "Alejo et al. (2007) propose two strategies for dealing with imbalanced domains using RBF neural networks"</sub>
- **descriptive / context**: Boosting was the most extensively explored ensemble approach for adapting ensembles to cost-sensitivity. (p. 24)[^original]  
  <sub>anchor: "However, boosting was the most extensively explored."</sub>
- **descriptive / finding or result**: AdaBoost under imbalanced class distributions biases learning through its weights towards the majority class, because the majority class contributes more to overall accuracy. (p. 24)[^original]  
  <sub>anchor: "When the class distribution is imbalanced, AdaBoost biases the learning (through the weights) towards the majority class"</sub>
- **descriptive / method**: RareBoost (Joshi et al., 2001), AdaC1, AdaC2 and AdaC3 (Sun et al., 2007), and BABoost (Song et al., 2009) modify AdaBoost's weight update formula by introducing costs, differing in how they change the update rule. (p. 24)[^original]  
  <sub>anchor: "All of them modify the AdaBoost algorithm by introducing costs in the used weight updating formula."</sub>
- **descriptive / method**: Weighted Random Forest (WRF), proposed by Chen et al. (2004), assigns a higher misclassification cost to the minority class to handle highly-skewed class distributions. (p. 24)[^original]  
  <sub>anchor: "WRF strategy operates by assigning a higher misclassification cost to the minority class."</sub>
- **descriptive / context**: The survey refers readers to Galar et al. (2012) for an extensive review of ensembles for class imbalance. (p. 25)[^original]  
  <sub>anchor: "For an extensive review on ensembles for handling class imbalance see Galar et al. (2012)."</sub>
- **descriptive / method**: Some SVM proposals bias the hyperplane away from the positive class without a cost matrix, because skewed data pushes the hyperplane towards the positive class; Wu and Chang (2003) do this by changing the kernel function. (p. 25)[^original]  
  <sub>anchor: "Wu and Chang (2003) accomplish this with an algorithm that changes the kernel function."</sub>
- **descriptive / method**: Fuzzy Support Vector Machines for Class Imbalance Learning (FSVM-CIL), proposed by Batuwita and Palade (2010b), improves the FSVM outlier-and-noise handling method of Lin and Wang (2002) to also deal with imbalanced data sets. (p. 25)[^original]  
  <sub>anchor: "Fuzzy Support Vector Machines for Class Imbalance Learning (FSVM-CIL) was a method proposed by Batuwita and Palade (2010b)."</sub>
- **descriptive / method**: Potential SVM (P-SVM) uses a new objective function and constraints; an improved P-SVM by Li et al. (2009) was proposed for imbalanced data sets. (p. 25)[^original]  
  <sub>anchor: "An improved P-SVM algorithm (Li et al., 2009) was proposed to better cope with imbalanced data sets."</sub>
- **descriptive / method**: Barandela et al. (2003) use a weighted distance function in k-NN classification that assigns weights per class rather than per prototype, so minority examples become closer and the learner finds nearest neighbours among the minority class. (p. 25)[^original]  
  <sub>anchor: "This method assigns different weights to the respective classes and not to the individual prototypes."</sub>
- **descriptive / method**: Class Confidence Proportion Decision Tree (CCPDT), proposed by Liu et al. (2010), embeds the Class Confidence Proportion measure in information gain as the splitting criterion and prunes branches with a Fisher exact test. (p. 26)[^original]  
  <sub>anchor: "CCP measure is embedded in the information gain and used as the splitting criteria."</sub>
- **descriptive / finding or result**: CCPDT is described as robust, insensitive to class distribution, and generating statistically significant rules. (p. 26)[^original]  
  <sub>anchor: "CCPDT is robust and insensitive to class distribution and generates rules that are statistically significant."</sub>
- **descriptive / method**: Hellinger Distance Decision Trees (HDDT) use Hellinger distance as splitting criterion (Cieslak and Chawla, 2008) and were shown to be insensitive to class distribution skewness. (p. 26)[^original]  
  <sub>anchor: "Hellinger distance was introduced as a decision tree splitting criterion to build Hellinger Distance Decision Trees (HDDT)"</sub>
- **recommended / recommendation**: Cieslak et al. (2012) recommended bagged HDDTs as the preferred decision-tree method for imbalanced data sets. (p. 26)[^original]  
  <sub>anchor: "Cieslak et al. (2012) recommended the use of bagged HDDTs as the preferred method"</sub>
- **descriptive / method**: For regression trees, some works change the splitting criteria to address imbalance (e.g. Torgo and Ribeiro 2003; Ribeiro and Torgo 2003). (p. 26)[^original]  
  <sub>anchor: "some works have addressed the problem of imbalanced domains by changing the splitting criteria of regression trees"</sub>
- **descriptive / method**: Kernel Boundary Alignment (KBA), Wu and Chang (2005), shifts the boundary towards the majority class by modifying the kernel matrix according to the imbalanced distribution. (p. 26)[^original]  
  <sub>anchor: "This method adjusts the boundary towards the majority class by modifying the kernel matrix"</sub>
- **descriptive / method**: eKISS, proposed by Tan et al. (2003), is an ensemble for multi-class imbalanced data designed to raise classifier sensitivity without losing specificity, combining base classifier rules to create new classifiers. (p. 26)[^original]  
  <sub>anchor: "This algorithm was specifically designed to increase classifiers sensitivity without losing the corresponding specificity."</sub>
- **descriptive / method**: Dynamic Classifier Ensemble for Imbalanced Data (DCEID), Xiao et al. (2012), combines dynamic ensemble learning with cost-sensitive learning and adaptively selects the more appropriate ensemble approach. (p. 26)[^original]  
  <sub>anchor: "DCEID combines dynamic ensemble learning with costsensitive learning and is able to adaptively select the more appropriate ensemble approach."</sub>
- **descriptive / limitation**: Algorithm-modification strategies have disadvantages: an often unavailable cost matrix, the need for deep knowledge of the learner, and difficulty of reusing a method with a different learning system, unlike pre-processing approaches. (p. 26)[^original]  
  <sub>anchor: "the difficulty of using an already existing method with a different learning system which contrasts with pre-processing approaches."</sub>

## 4.3 Prediction Post-processing

- **descriptive / definition**: Post-processing covers two solution types: threshold methods that vary the class-membership threshold on a score to produce several learners, and cost-sensitive post-processing that associates costs with errors and minimises expected cost. (p. 26)[^original]  
  <sub>anchor: "cost-sensitive post-processing: associates costs to prediction errors and minimizes the expected cost."</sub>
- **descriptive / context**: Table 5 summarises the main bibliographic references for post-processing strategies. (p. 26)[^original]  
  <sub>anchor: "Table 5 summarizes the main bibliographic references of post-processing strategies."</sub>

## 4.3.1 Threshold Method

- **descriptive / finding or result**: Maloof (2003) concluded that moving the decision threshold, applying a sampling strategy and adjusting the cost matrix produce classifiers with the same performance. (p. 26)[^original]  
  <sub>anchor: "concluded that the operations of moving the decision threshold, applying a sampling"</sub>
- **descriptive / method**: Post hoc cost-sensitive methods change only model predictions (e.g. Domingos 1999; Sinha and May 2004); they could potentially apply to imbalanced distributions but have not been applied or evaluated on such tasks to the authors' knowledge. (p. 27)[^original]  
  <sub>anchor: "However, to the best of our knowledge, these methods have never been applied or evaluated on these tasks."</sub>

## 4.3.2 Cost-sensitive Post-processing

- **descriptive / context**: Cost-sensitive post-processing for regression was only recently proposed (Bansal et al., 2008; Zhao et al., 2011) and remains under-explored with few solutions; no evaluation in imbalanced domains has yet been made. (p. 27)[^original]  
  <sub>anchor: "In regression , introducing costs at a post-processing level has only recently been proposed (Bansal et al., 2008; Zhao et al., 2011)."</sub>
- **descriptive / method**: Reframing (Hernández-Orallo, 2012, 2014) adjusts predictions of a previously built model to different data distributions and is potentially suitable for imbalanced problems, though not developed specifically for them. (p. 27)[^original]  
  <sub>anchor: "this framework aims at adjusting the predictions of a previously built model to different data distributions."</sub>
- **descriptive / definition**: Reframing is the process of applying a previously built model to a new operating context by transforming inputs, outputs and patterns. (p. 27)[^original]  
  <sub>anchor: "The notion of reframing was established as the process of applying a previously built model to a new operating context"</sub>
- **descriptive / method**: Reframing step one converts a traditional crisp regression model with one parameter into a soft regression model with two parameters, viewed as a normal conditional density estimator (NCDE), using enrichment methods. (p. 27)[^original]  
  <sub>anchor: "the conversion of any traditional crisp regression model with one parameter into a soft regression model with two parameters"</sub>
- **descriptive / method**: Reframing step two adapts the enriched soft model to new contexts through an instance-dependent optimisation of the expected loss derived from the conditional normal distribution. (p. 27)[^original]  
  <sub>anchor: "the reframing of an enriched soft regression model to new contexts by an instance-dependent optimisation of the expected loss"</sub>

## 4.4 Hybrid Methods

- **descriptive / context**: Hybrid methods combine basic approaches, capitalising on the main advantages of each; Table 6 lists the main references for hybrids combining re-sampling with special-purpose learners. (p. 28)[^original]  
  <sub>anchor: "Existing hybrid approaches combine the use of re-sampling strategies with special-purpose learning algorithms."</sub>
- **descriptive / method**: Estabrooks and Japkowicz (2001) and Estabrooks et al. (2004) proposed a mixture-of-experts framework with classifier, expert and output levels, motivated by the observation that a perfectly balanced dataset may not be optimal and the right amount of over/under-sampling is hard to determine. (p. 28)[^original]  
  <sub>anchor: "the fact that a perfectly balanced data may not be optimal and that the right amount of over/under-sample to apply is difficult to determine."</sub>
- **descriptive / method**: The Estabrooks framework has an under-sampling expert and an over-sampling expert, each with 10 classifiers trained on data re-sampled at different rates, with an elimination step removing unreliable learners. (p. 28)[^original]  
  <sub>anchor: "The architecture incorporates 10 classifiers on the over-sampling expert and another 10 classifiers on the under-sampling expert."</sub>
- **descriptive / finding or result**: The Estabrooks combination heuristic (positive if any classifier, expert or output votes positive) is described as clearly heavily biased towards the minority positive class. (p. 28)[^original]  
  <sub>anchor: "This strategy is clearly heavily biased towards the minority (positive) class."</sub>

## 4.4.1 Re-sampling and Special-purpose Learning Methods

- **descriptive / method**: Kotsiantis and Pintelas (2003) use a facilitator agent that filters features and passes data to three learning agents (Naive Bayes, C4.5 and 5NN), each re-sampling the data, and the facilitator combines predictions by majority voting. (p. 28)[^original]  
  <sub>anchor: "Finally, the facilitator makes the final prediction according to majority voting."</sub>
- **descriptive / method**: Phua et al. (2004) re-sample into eleven data sets each containing all minority examples and part of the majority, train Naive Bayes, C4.5 and backpropagation classifiers on each partition, bag same-algorithm classifiers and stack across algorithms. (p. 29)[^original]  
  <sub>anchor: "The applied re-sampling strategy partitions the data set into eleven new data sets"</sub>
- **descriptive / method**: EasyEnsemble and BalanceCascade (Liu et al., 2009) use bagging with AdaBoost per bag, build balanced bags by random majority under-sampling; EasyEnsemble runs AdaBoost iterations simultaneously, while BalanceCascade discards majority examples correctly classified with higher confidence after each AdaBoost round. (p. 29)[^original]  
  <sub>anchor: "both construct balanced bags by randomly under-sampling examples from the majority class."</sub>
- **descriptive / method**: Wang (2008) combines SMOTE with Biased-SVM (Veropoulos et al., 1999): Biased-SVM is applied to obtain support vectors of both classes, then SMOTE over-samples support vectors (or the entire minority class) before a final Biased-SVM classification. (p. 29)[^original]  
  <sub>anchor: "Then SMOTE is used to over-sample the support vectors with two alternatives"</sub>
- **descriptive / method**: Yoon and Kwek (2005) use class-purity-maximising clustering producing pure majority clusters and non-pure clusters; minority examples join non-pure clusters, each with a decision tree committee, and minority predictions from the committee are passed to a neural network classifier. (p. 30)[^original]  
  <sub>anchor: "Finally, a strategy using a clustering method based on class purity maximization is proposed by Yoon and Kwek (2005)."</sub>

## 5 Related Problems

- **descriptive / context**: Small disjuncts, class overlap and small sample size frequently coexist with imbalanced classification and are identified as possible causes of performance degradation. (p. 30)[^original]  
  <sub>anchor: "Problems such as small disjuncts, class overlap and small sample size, usually coexist with imbalanced classification domains"</sub>
- **descriptive / definition**: The overlap problem occurs when a region of data space contains an identical number of training cases for each class, making it harder for a learner to distinguish the classes there. (p. 30)[^original]  
  <sub>anchor: "The overlap problem occurs when a given region of the data space contains an identical number of training cases for each class."</sub>
- **descriptive / finding or result**: Combining imbalance with class overlap causes a significant deterioration of learner performance, producing more difficulty than either problem alone (Denil and Trappenberg, 2010). (p. 30)[^original]  
  <sub>anchor: "both problems acting together produce much more difficulties than expected when considering their effects individually"</sub>
- **descriptive / context**: Small sample size hinders learners from capturing minority characteristics and reduces generalisation, and imbalance degrades performance in small data sets, though the loss lessens as training set size grows (Japkowicz and Stephen 2002; Jo and Japkowicz 2004). (p. 30)[^original]  
  <sub>anchor: "class imbalance degrades classification performance in small data sets although this loss of performance tends to gradually reduce as the training set size increases."</sub>
- **descriptive / definition**: Rare cases are extremely scarce examples that are difficult to detect and use for generalisation (Weiss, 2005). (p. 31)[^original]  
  <sub>anchor: "Rare examples are extremely scarce cases that are difficult to detect and use"</sub>
- **descriptive / finding or result**: Forman and Cohen (2004) showed that a balanced training set is not the most favourable setting for imbalanced domains, and non-random sampling favouring the minority class can greatly improve classifier performance. (p. 31)[^original]  
  <sub>anchor: "obtaining a balanced training set is not the most favourable setting and classifiers performance can be greatly improved by non-random sampling"</sub>
- **descriptive / context**: In high-dimensional domains such as text classification, the main challenge is selecting features that contain the key information. (p. 31)[^original]  
  <sub>anchor: "The main challenge here is to adequately select features that contain the key information of the problem."</sub>
- **recommended / recommendation**: Feature selection is recommended for high-dimensional imbalanced data (Wasikowski and Chen, 2010) and is pointed to as a solution for class imbalance. (p. 31)[^original]  
  <sub>anchor: "Feature selection is recommended (Wasikowski and Chen, 2010)"</sub>
- **descriptive / finding or result**: Noise has a greater impact on minority examples in imbalanced domains (Weiss, 2004). (p. 31)[^original]  
  <sub>anchor: "In imbalanced domains, noisy data has a greater impact on the least represented examples"</sub>
- **descriptive / finding or result**: Seiffert et al. (2011) concluded that class noise generally has a more significant impact on learners than class imbalance, and that the interaction between imbalance level and noise level is significant. (p. 31)[^original]  
  <sub>anchor: "class noise has a more significant impact on learners than imbalance."</sub>
- **descriptive / definition**: Small disjuncts are subclusters with low coverage, classifying few examples (Holte et al., 1989); learners are biased towards large disjuncts and so tend to overfit and misclassify cases in small disjuncts. (p. 32)[^original]  
  <sub>anchor: "When a subcluster has a low _coverage_ , i.e., it classifies few examples, it is called small (Holte et al., 1989)."</sub>
- **descriptive / finding or result**: Pruning was not considered an effective strategy for small disjuncts under class imbalance (Prati et al., 2004b; Weiss, 2010). (p. 32)[^original]  
  <sub>anchor: "it was not considered an effective strategy for dealing with small disjuncts in the presence of class imbalance"</sub>
- **descriptive / finding or result**: Weiss (2010) found errors concentrate on smaller disjuncts even with balanced data, with class imbalance increasing error concentration; artificially balancing training data decreases error concentration, so imbalance is partly responsible for the small disjunct problem. (p. 32)[^original]  
  <sub>anchor: "artificially modifying the class distribution of the training data to be more balanced, causes a decrease in the error concentration."</sub>
- **descriptive / definition**: Error concentration (Weiss and Hirsh, 2000) is a metric proposed for evaluating error concentration towards smaller disjuncts. (p. 32)[^original]  
  <sub>anchor: "A new metric called _error concentration_ (Weiss and Hirsh, 2000) was proposed for evaluating the error concentration towards the smaller disjuncts."</sub>
- **expected / recommendation**: The interaction between related problems and imbalance should not be ignored, since their conjunction further degrades classifier performance. (p. 32)[^original]  
  <sub>anchor: "therefore this relationship should not be ignored."</sub>

## 6 Conclusions

- **descriptive / context**: The paper proposes a formulation of imbalanced modelling covering both classification and regression, and a taxonomy grouping approaches into data pre-processing, special-purpose learning methods and prediction post-processing. (p. 32)[^original]  
  <sub>anchor: "We propose a new taxonomy for the existing approaches grouping them into: (i) data pre-processing"</sub>
- **descriptive / context**: Most existing solutions for imbalanced modelling focus on classification, and the survey claims to be the first to also address regression approaches to imbalanced data sets. (p. 32)[^original]  
  <sub>anchor: "In this paper, we propose the first survey that also addresses existing approaches to imbalanced data sets within regression tasks."</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Paula Branco, Luı́s Torgo, Rita P. Ribeiro, "A Survey of Predictive Modelling under Imbalanced Distributions" (2015-05-07). https://arxiv.org/abs/1505.01658
