---
type: Source Digest
title: Explainable Fraud Detection with GNNExplainer and Shapley Values - part 1 of 3 (pp. 1-17)
description: 'Verified paraphrased digest, pp. 1-17: Abstract; Acknowledgement; Table of Contents; and 8 more sections'
resource: https://arxiv.org/abs/2509.12262
tags:
- academic_finding
- explainability
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-explainable-fraud-detection-with-gnnexplainer-and-shapley-values
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-12-09'
legal_status: unknown
part: 1
parts_total: 3
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
  resource: https://arxiv.org/abs/2509.12262
  title: Explainable Fraud Detection with GNNExplainer and Shapley Values
  author: org:arxiv
  last_modified: '2025-12-09T00:00:00Z'
digest_points: 53
---

# Explainable Fraud Detection with GNNExplainer and Shapley Values (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-17) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The dissertation notes that financial fraud risk grows as digital payments become more frequent, and that regulators and society have raised transparency standards for AI fraud-detection systems, so the work focuses on developing an explainable fraud detector. (p. 1)[^original]  
  <sub>anchor: "society and regulators have raised the standards for these systems' transparency for reliability verification purposes"</sub>
- **descriptive / context**: Fraud analysts benefit from concise and understandable explanations to make fraud investigations more effective. (p. 1)[^original]  
  <sub>anchor: "fraud analysts also profit from having concise and understandable explanations"</sub>
- **descriptive / context**: The implementation uses Python, PyTorch 2.0, TorchGeometric 1.13 and Bash scripts; keywords include machine learning, explainable AI, payment fraud and data visualization. (p. 3)[^original]  
  <sub>anchor: "Python, PyTorch 2.0, TorchGeometric 1.13, Bash Script"</sub>

## 1.1. Motivation

- **descriptive / context**: Fraud detection and decision support systems are widely used in digital banking and e-commerce, and many employ AI to recognise subtle and complex fraud patterns from historical and real-time data. (p. 7)[^original]  
  <sub>anchor: "A significant percentage of these systems employ Artificial Intelligence (AI) to better recognize subtle and complex patterns of fraud"</sub>
- **descriptive / context**: Users of AI fraud systems face a black-box problem, which may lead them to regard AI predictions as untrustworthy. (p. 7)[^original]  
  <sub>anchor: "users of such systems are presented with a black-box problem, and thus, they might deem predictions from AI untrustworthy"</sub>
- **descriptive / limitation**: Implementing explainable AI faces challenges: it requires semantic financial data that is often inaccessible due to privacy and security concerns, and explanations from most existing XAI methods are vague, unintuitive and open to contradicting interpretations. (p. 7)[^original]  
  <sub>anchor: "XAI requires semantic financial data which is often inaccessible due to privacy and security concerns"</sub>

## 1.2. Project Objective

- **descriptive / context**: The project targets tabular transaction data with fields such as sender, receiver, monetary amount and timestamp, and aims to propose a fraud detection model with an explanation method that simulates a real fraud investigation. (p. 7)[^original]  
  <sub>anchor: "The target data is the tabular transaction data containing typical information such as sender, receiver, monetary amount and timestamp"</sub>
- **descriptive / definition**: Objectives are to propose a machine learning model to detect consumer payment fraud, and to give clear explanations of its predictions using finance knowledge and data visualization. (p. 8)[^original]  
  <sub>anchor: "Provide a clear explanation for the prediction of the model by utilizing finance knowledge and data visualization"</sub>

## 2.1. Consumer Payment Fraud

- **descriptive / finding or result**: In the UK, more than £360 million in thefts were reported in H1 2022 alone, according to UK Finance (2021). (p. 8)[^original]  
  <sub>anchor: "more than £360 million in thefts were reported in H1 2022 alone, according to UK Finance (2021)"</sub>
- **descriptive / definition**: Unauthorized fraud occurs when the account holder does not consent and a criminal completes the transaction, such as by using the victim's card information; this is usually called account takeover fraud (ATO). (p. 8)[^original]  
  <sub>anchor: "Unauthorized fraud occurs when the account holder does not give consent and a criminal completes the transaction"</sub>
- **descriptive / definition**: Per Forbes Finance Council (2022), ATO is criminals taking control of online accounts they do not own, using techniques such as buying stolen information on the dark web, social engineering, phishing, password cracking or credential stuffing. (p. 8)[^original]  
  <sub>anchor: "take control of online accounts that do not belong to them in order to further a variety of malicious objectives"</sub>

## 2.2. Machine Learning and Explainable AI in Fraud Detection

- **descriptive / context**: Fraud detection is researched in applications including anti-money laundering, spam reviews and news identification, fraudulent social network accounts, online payment systems and online store platforms. (p. 8)[^original]  
  <sub>anchor: "It is researched in several applications, including anti-money laundering"</sub>

## 2.1. Consumer Payment Fraud

- **descriptive / context**: Consumer payment fraud falls into two basic categories, authorized and unauthorized. Unauthorized transactions are more prevalent in volume, at least in the UK, where over £360 million in thefts were reported in H1 2022 alone according to UK Finance. (p. 8)[^original]  
  <sub>anchor: "Unauthorized transactions are more prevalent in volume, at least in the UK, where more than"</sub>
- **descriptive / context**: The project focuses on detecting and explaining account takeover (ATO) fraud, a form of unauthorized fraud where the criminal completes a transaction without the account holder's consent. (p. 8)[^original]  
  <sub>anchor: "This project will focus on detecting and explaining ATO frauds."</sub>
- **descriptive / finding or result**: ATO ranks as the fifth most frequent attack method for North American merchants. (p. 8)[^original]  
  <sub>anchor: "ATO fraud now ranks as the fifth most frequent attack method for North American merchants"</sub>
- **descriptive / finding or result**: In the 2022 Global Payments and Fraud Report, 27% of worldwide merchants that took part had experienced ATO in the past year. (p. 8)[^original]  
  <sub>anchor: "for 27% of worldwide merchants who took part in the 2022 Global Payments and Fraud Report"</sub>

## 2.2. Machine Learning and Explainable AI in Fraud Detection

- **descriptive / limitation**: Although most research reports high accuracy and scalability, interpretability is a significant concern; false predictions can harm customer experience and provider credibility, and human review is costly and inefficient. (p. 9)[^original]  
  <sub>anchor: "their interpretability appears to be a significant concern"</sub>
- **descriptive / requirement**: The author argues that automatically generated explanations are necessary to eliminate human intervention in fraud detection. (p. 9)[^original]  
  <sub>anchor: "automatically generated explanation is necessary to eliminate human intervention in fraud detection"</sub>
- **descriptive / context**: Homogeneous graphs are widely used in fraud prevention, such as anti-money laundering and risky or malicious account detection; heterogeneous and combined graphs are becoming more prevalent because they aggregate information across node and edge types. (p. 9)[^original]  
  <sub>anchor: "it allows aggregating information propagation through different node and edge types"</sub>
- **descriptive / finding or result**: GEM (Liu et al, 2018) used attention in a device-account heterogeneous graph and performs very well for Alipay, although it does not consider type features as inputs. (p. 9)[^original]  
  <sub>anchor: "the model performs very well for Alipay in its day-to-day business"</sub>
- **descriptive / case example**: Rao (2020) used a GNN to detect fraudulent transactions on eBay, and GNNExplainer was then used to generate a subgraph around the node to explain. (p. 9)[^original]  
  <sub>anchor: "a Graph Neural Network (GNN) (Gori, Monfardini, and Scarselli, 2005) model is used to detect fraudulent transactions on eBay"</sub>
- **descriptive / limitation**: A static graph alone often makes explanations vague and open to conflicting interpretation; the author suggests adding methods such as SHAP to provide more evidence. (p. 10)[^original]  
  <sub>anchor: "having just a static graph makes the explanation vague and open to potentially conflicting interpretation"</sub>

## 3. Literature Review

- **descriptive / context**: The literature review is divided into machine learning models for fraud detection (Section 3.1) and interpretability methods (Section 3.2). (p. 10)[^original]  
  <sub>anchor: "The fraud detection methods are covered in Section 3.1"</sub>

## 3.1.1. Transformer

- **descriptive / finding or result**: Transformer was proposed to address CNN-based models whose number of operations grows with distance between positions, making long-range dependencies computationally expensive; it computes position representations with a constant number of operations. (p. 10)[^original]  
  <sub>anchor: "making it computationally expensive to quantify dependencies between distant entities in a network"</sub>
- **descriptive / definition**: Attention maps a query and key-value pairs to an output, computed as a weighted sum of values, with weights reflecting query-key compatibility. (p. 11)[^original]  
  <sub>anchor: "The output is a weighted sum of the values whose weights are computed by quantifying how compatible the query is with the corresponding key"</sub>
- **descriptive / definition**: Multiheaded attention runs parallel attention calculations with different projections of key, value and query vectors, concatenates the head outputs and projects them back to the input dimension. (p. 11)[^original]  
  <sub>anchor: "each single attention calculation is carried out in parallel with different projections of key, value, and query vectors"</sub>
- **descriptive / context**: Although Transformer is mainly used in NLP, the author suggests adapting it in a GNN to represent node relationships as attention vectors. (p. 11)[^original]  
  <sub>anchor: "we could adapt this in our GNN to represent relationships among nodes as attention vectors"</sub>

## 3.1.2. Heterogeneous Graph Transformer

- **descriptive / definition**: HGT (Hu et al, 2020) uses heterogeneous mutual attention over each edge based on its meta relation triplet (source node type, edge type, target node type), avoiding parameters tied to specific edge types. (p. 11)[^original]  
  <sub>anchor: "based on its meta relation triplet, which consists of the node type of s, the edge type of e between s and t, and the node type of t"</sub>
- **descriptive / finding or result**: HGT can integrate data from high-order neighbours of various types through message passing across layers and implicitly learns important meta pathways from one-hop edges without explicit meta path construction. (p. 12)[^original]  
  <sub>anchor: "HGT may integrate data from high-order neighbours of various types by message passing across layers"</sub>
- **descriptive / definition**: HGT has three components: heterogeneous mutual attention, heterogeneous message passing, and target-specific aggregation. (p. 12)[^original]  
  <sub>anchor: "There are 3 main components of HGT 1) Heterogeneous Mutual Attention 2) Heterogeneous Message Passing and 3) Target-Specific Aggregation"</sub>
- **descriptive / finding or result**: HGT uses different weight matrices for different relations and is therefore claimed to handle distribution differences in heterogeneous graphs better than the original Transformer. (p. 12)[^original]  
  <sub>anchor: "HGT uses different weight matrices for different relations, thus it is better than the original Transformer"</sub>

## 3.1.3. xFraud Detector

- **descriptive / definition**: The xFraud detector is inspired by Transformer and HGT, using Transformer self-attention adapted for GNNs as in HGT. (p. 12)[^original]  
  <sub>anchor: "xFraud detector uses the self-attention mechanism as presented in Transformer but adapts it for GNN as shown in HGT"</sub>
- **descriptive / finding or result**: Compared with HGT, xFraud does not use different weight matrices for different node and edge types, claimed to improve performance while maintaining accuracy, and omits HGT's temporal encoding so the model can view all of a user's transactions at any time. (p. 13)[^original]  
  <sub>anchor: "xFraud detector does not use different weight matrices for different node and edge types to improve performance"</sub>
- **descriptive / method**: The xFraud detector takes as input a heterogeneous graph with node features, one-hot encoded node types and edge types, with initial feature values set to 0 for non-transaction nodes. (p. 13)[^original]  
  <sub>anchor: "The detector received a heterogeneous graph including node features, one-hot encoded node types and edge types as inputs"</sub>
- **descriptive / method**: Convolution layers with self-attention compute query, key and value vectors, attention scores for each edge's source and target nodes, layer-wise normalisation, and a ReLU activation passed to the next layer. (p. 13)[^original]  
  <sub>anchor: "These scores are fed into a _ReLU_ activation function which are taken by the next layer as inputs"</sub>
- **descriptive / method**: A tanh activation is applied to the final transaction representation, which is concatenated with the original transaction features and fed to a feedforward network with 2 hidden layers; dropout, layer normalization and ReLU then produce a risk score. (p. 13)[^original]  
  <sub>anchor: "fed into a feedforward connected network with 2 hidden layers"</sub>
- **descriptive / method**: The loss is cross entropy between the fraud label and the probability score computed by softmax. (p. 13)[^original]  
  <sub>anchor: "The loss function used is the cross entropy of the fraud label and the probability score calculated by _softmax._"</sub>

## 3.2.1. LIME

- **descriptive / definition**: LIME (Ribeiro et al, 2016) samples instances close to the original, trains a simpler model such as a linear model on them, and examines it to explain the original model; it is model-agnostic and easy to use. (p. 14)[^original]  
  <sub>anchor: "This algorithm samples instances close to the original instance, and trains a simpler model"</sub>
- **descriptive / limitation**: LIME faces challenges including difficulty sampling data points and choosing the right explanation model. (p. 14)[^original]  
  <sub>anchor: "Nonetheless, LIME faces many challenges including difficulties in sampling data points and choosing the right explanation model"</sub>

## 3.2.2. Shapley Values

- **descriptive / definition**: Shapley values come from coalitional game theory and give each feature's contribution to a prediction as its average marginal contribution across all feature combinations. (p. 14)[^original]  
  <sub>anchor: "the Shapley value of a feature is its average marginal contribution across all possible combinations"</sub>
- **descriptive / method**: The marginal contribution of feature v is found by comparing predictions with and without v across all combinations of the other features. (p. 14)[^original]  
  <sub>anchor: "predictions are calculated with and without 𝑣 together with all combinations of the values of other features"</sub>
- **descriptive / limitation**: Shapley values distribute contributions fairly better than LIME, but exact computation needs Ω(2^n) time, so with hundreds of features it is not feasible. (p. 14)[^original]  
  <sub>anchor: "this method requires a lot of computing time (Ω(2𝑛 )), and in a typical dataset with hundreds of features, it is not feasible"</sub>

## 3.2.3. SHAP and KernelSHAP

- **descriptive / definition**: SHAP (Lundberg and Lee, 2017) stands for Shapley Additive Explanations and approximates Shapley values because the exact method is too inefficient in real-world settings. (p. 14)[^original]  
  <sub>anchor: "SHAP aims to approximate Shapley Values (Shapley, 1953) since the original method is too inefficient in real-world settings"</sub>
- **descriptive / method**: KernelSHAP generates samples from feature masks where present features take the instance's values and absent features are taken from a random data instance. (p. 15)[^original]  
  <sub>anchor: "KernelSHAP generates samples based on feature masks where present features are mapped to the instance’s features"</sub>
- **descriptive / method**: KernelSHAP weights feature masks by the missingness or isolation of features, unlike LIME which weights instances by distance to the original instance. (p. 15)[^original]  
  <sub>anchor: "instead, KernelSHAP weights feature masks based on the missingness/isolation of features in the mask"</sub>
- **descriptive / data or feature**: The SHAP summary plot ranks features in descending order of importance, with horizontal position showing whether a value raises or lowers the prediction, and colour showing whether the feature value is high (red) or low (blue). (p. 15)[^original]  
  <sub>anchor: "Feature importance: features are ranked in descending order"</sub>

## 3.2.4. GNNExplainer

- **descriptive / context**: GNNs use pairwise message passing, updating node features by exchanging information with neighbours, but offer insufficient transparency because of their typically large number of layers. (p. 15)[^original]  
  <sub>anchor: "GNNs does not provide sufficient transparency in their predictions due to the typically large number of layers"</sub>
- **descriptive / definition**: GNNExplainer takes a trained GNN and its predictions as input and outputs a subgraph with the subset of features most important to the prediction; it is model-agnostic. (p. 15)[^original]  
  <sub>anchor: "GNNExplainer is model-agnostic and can be used to provide more insights into predictions from any GNN model"</sub>

## 3.2.3. SHAP and KernelSHAP

- **descriptive / finding or result**: In the same SHAP example, volatile acidity is described as negatively correlated with the target variable. (p. 15)[^original]  
  <sub>anchor: "Similarly, we will say the “volatile acidity” is negatively correlated with the target variable."</sub>

## 3.2.4. GNNExplainer

- **descriptive / data or feature**: In the GNNExplainer figure, green marks important neural message-passing paths and yellow marks unimportant ones when generating the most influential features for a node's prediction. (p. 15)[^original]  
  <sub>anchor: "green represents important paths, yellow represents unimportant ones"</sub>
- **descriptive / method**: GNNExplainer generates a subgraph such that the information shared with the original graph is maximised, using mutual information (MI) to quantify how a node's prediction changes when its computation graph is limited to the explanation subgraph. (p. 16)[^original]  
  <sub>anchor: "GNNExplainer generates a subgraph of the entire original input graph such that the shared information between the two graphs is maximized"</sub>
- **descriptive / method**: The subgraph with associated features is found by maximising mutual information with the original graph and full feature set, with H denoting the entropy function; the output is an edge mask and a feature mask with weights. (p. 16)[^original]  
  <sub>anchor: "At the end of the process, an edge mask and a feature mask will be generated"</sub>
- **descriptive / limitation**: Because MI scores are only positive, the direction of an edge's or feature's effect on the predicted class is unclear, so it cannot be told whether a feature or edge correlates negatively or positively with the prediction. (p. 16)[^original]  
  <sub>anchor: "MI scores can only be positive. As such, it is unclear if a certain node feature or edge has negative or positive correlation"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Explainable Fraud Detection with GNNExplainer and Shapley Values" (2025-12-09). https://arxiv.org/abs/2509.12262
