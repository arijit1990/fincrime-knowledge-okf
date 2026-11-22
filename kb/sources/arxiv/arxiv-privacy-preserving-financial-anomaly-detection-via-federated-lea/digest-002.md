---
type: Source Digest
title: Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation - part 2 of 4 (pp. 5-9)
description: 'Verified paraphrased digest, pp. 5-9: Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation > 4 TECHNICAL APPROACH; Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation > 5 PROOF OF PRIVACY; Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation > 6 EXPERIMENTAL RESULTS; and 4 more sections'
resource: https://arxiv.org/abs/2310.04546
tags:
- academic_finding
- global_academic
- ml_statistics
- preprint
- privacy_data_protection
status: stable
source_id: arxiv-privacy-preserving-financial-anomaly-detection-via-federated-lea
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-06-10'
legal_status: unknown
part: 2
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2310.04546
  title: Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation
  author: org:arxiv
  last_modified: '2023-06-10T00:00:00Z'
digest_points: 53
---

# Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 5-9) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4 TECHNICAL APPROACH

- **descriptive / method**: During training, the aggregator encrypts a sample of Gaussian noise with mean 0 and standard deviation sigma, and the aggregator and S aggregate all shared updates and the noise; only S learns the decrypted aggregated noisy update as plaintext, and S then updates its model with it, repeating until the desired number of iterations (e.g. convergence). (p. 5)[^original]  
  <sub>anchor: "The aggregator encrypts a sample of Gaussian noise N (0 _, 𝜎_ ) with mean 0 and standard deviation _𝜎_ obtaining"</sub>
- **descriptive / method**: At inference time S runs a transaction through its model twice, once assuming the account is normal and once assuming it is abnormal, yielding preliminary labels l0 and l1, which are then combined with the bank's normal indicator bit in a secure two-party computation to give the final prediction. (p. 5)[^original]  
  <sub>anchor: "S runs it through its model twice, once guessing that the account is normal and once guessing that the account is abnormal"</sub>
- **descriptive / method**: The final inference prediction is computed as (1 minus b) times l0 plus b times l1, where b is the normal indicator bit held by the bank, so that S learns the combined label. (p. 5)[^original]  
  <sub>anchor: "which is the final prediction of our system"</sub>
- **descriptive / definition**: The approach can use any model structure trainable by incremental and aggregatable updates, such as stochastic gradient descent; per-transaction updates are computed independently of other transactions and are size-limited, and the overall update is the sum of a subset of them plus Gaussian noise. (p. 5)[^original]  
  <sub>anchor: "In principle, S can use any model structure that can be trained by incremental and aggregatable updates"</sub>
- **descriptive / method**: The ideal functionality takes per-transaction update pairs and bank normal indicator flags for the batch, computes the sum of the selected updates, adds Gaussian noise supplied by the aggregator, and outputs the noisy update to S. (p. 5)[^original]  
  <sub>anchor: "The ideal functionality computes: • _𝑢_′ =� _𝑖__𝑢_ _𝑖,𝑏𝑖_."</sub>
- **descriptive / method**: The model used in the evaluation is a classical multilayer perceptron with ReLU as the activation function. (p. 5)[^original]  
  <sub>anchor: "we use the classical multilayer perceptron (MLP) model with ReLU as the activation function for _𝑀_ ."</sub>
- **descriptive / requirement**: The authors require that training can be performed by applying only the aggregate update to the model after each batch, without other knowledge of the individual component updates. (p. 6)[^original]  
  <sub>anchor: "We require that train- ing can be performed by applying only _𝑢_ to the model after each batch"</sub>
- **descriptive / definition**: Oblivious transfer is a two-party protocol in which a sender with two messages sends one to a receiver who chooses which; the sender does not learn the choice and the receiver does not learn the other message. (p. 6)[^original]  
  <sub>anchor: "Oblivious transfer (OT) is a two-party secure computation protocol that allows a Sender with two messages"</sub>
- **descriptive / definition**: Secret sharing splits a value x into two random shares whose sum equals x, so each share alone is random while together they encode x; the notation with double brackets denotes a secret-shared value. (p. 6)[^original]  
  <sub>anchor: "In typical secret sharing setup, two parties respectively hold random shares _𝑟_ 0 and _𝑟_ 1."</sub>
- **descriptive / method**: The approach combines oblivious transfer and secret sharing; for training, S masks both per-update messages with a random mask, the bank obliviously selects the message matching its indicator bit, and the bank's share is forwarded to the aggregator so S and the aggregator hold a share of the update. (p. 6)[^original]  
  <sub>anchor: "S samples a random mask _𝑟𝑆_ , defines two messages"</sub>
- **descriptive / finding or result**: Because of additive sharing, S and the aggregator add all shares in a batch to obtain a secret share of the aggregated update, and the aggregator adds its noise term to its share before the result is revealed to S. (p. 6)[^original]  
  <sub>anchor: "S and the aggregator add together all shares in the current batch to get the secret share"</sub>
- **descriptive / method**: For inference, the bank performs oblivious transfer on masked versions of the two preliminary labels, and S recovers the label by adding its mask to the bank's returned share. (p. 6)[^original]  
  <sub>anchor: "The bank performs an oblivious transfer on _𝑚_ 0 = _ℓ_ 0 − _𝑟𝑆,𝑚_ 1 = _ℓ_ 1 − _𝑟𝑆_"</sub>
- **descriptive / finding or result**: Scalability: the approach scales with the number of participating banks because only the bank needed to evaluate a transaction takes part; the main limiting factor is communication between parties. (p. 6)[^original]  
  <sub>anchor: "Our approach is scalable with the number of participating banks since only the bank required for evaluating a transaction participates"</sub>
- **descriptive / finding or result**: Privacy of transaction details: S reveals only the receiving bank (to the aggregator) and the account (to that bank), so this form of privacy involves no utility trade-off. (p. 6)[^original]  
  <sub>anchor: "S reveals no information about the transaction details other than which receiving bank is involved"</sub>
- **descriptive / limitation**: Privacy of account flags is only partly achieved because leakage inherent in the setting lets S fairly well guess whether most accounts have flag zero; the aggregator's noise hides which model was updated, and increasing noise better protects flags but reduces training effectiveness. (p. 6)[^original]  
  <sub>anchor: "adding more noise will protect the flags of accounts better, but will also diminish the training effectiveness"</sub>
- **descriptive / finding or result**: The model is described as fairly explainable to S, with integrated gradients and counterfactual explanations readily usable, while banks learn nothing of value about the model. (p. 6)[^original]  
  <sub>anchor: "Classic methods such as integrated gradients [31] and counterfactual explanation [34] can be readily used."</sub>
- **descriptive / limitation**: The solution requires significant communication during training, linear in the number of training steps, though training is typically done offline while inference on a new transaction is very fast. (p. 6)[^original]  
  <sub>anchor: "Our solution requires significant communication during training (linear with respect to the number of training steps)."</sub>

## 5 PROOF OF PRIVACY

- **descriptive / finding or result**: Privacy against the aggregator is argued as reducing to the security of the oblivious transfer and secret sharing; the aggregator learns only the masked update and the identity of the receiving bank, and the proof assumes either the aggregator or S is honest, with S honest in this section. (p. 6)[^original]  
  <sub>anchor: "Privacy against the aggregator then reduces to the security of the underlying oblivious transfer protocol"</sub>
- **descriptive / finding or result**: Privacy against banks: during training a bank learns only the queried account and its secret share, which leaks no information; learning the queried account is inherent to the problem setting. (p. 6)[^original]  
  <sub>anchor: "During training, a Bank only learns the account queried and the secret share _𝑠_ 1."</sub>
- **descriptive / finding or result**: Privacy against S: updates are norm-clipped before aggregation, and the noise is calibrated to the clipping norm and the expected number of transactions per account in a batch to hide account-level flags. (p. 7)[^original]  
  <sub>anchor: "We clip the updates via norm clipping _before_ they are aggregated"</sub>
- **descriptive / finding or result**: The noise standard deviation is set to 10 times the clipping bound, intended to cover the worst-case account's influence on the overall update; the authors consider this sufficient given the significant inherent leakage. (p. 7)[^original]  
  <sub>anchor: "We calibrate our noise to have a standard deviation 10 times the clipping bound"</sub>
- **descriptive / finding or result**: The upscaled dataset comprises 7M records, with individual accounts having up to 7K transactions, up from 749 in the original training set; batch size is about 8K. (p. 7)[^original]  
  <sub>anchor: "Our upscaled dataset comprises 7M records overall. Within that, there are individual accounts with up to 7K transactions, up from 749"</sub>
- **descriptive / finding or result**: During inference S learns only the final classification, which reveals nothing about the bank's flag beyond the inherent leakage discussed in Section 3. (p. 7)[^original]  
  <sub>anchor: "During inference, S learns the final classification of a transaction"</sub>
- **recommended / recommendation**: Against a malicious aggregator, the proposal could be extended with zero-knowledge proofs showing the output sent to S was computed honestly, including honest sampling and noise application, which could alternatively be replaced by a small MPC among several banks. (p. 7)[^original]  
  <sub>anchor: "our proposal can be extended to include (fairly inexpensive) ZeroKnowledge proofs where the aggregator proves its output"</sub>
- **descriptive / limitation**: Fully malicious banks can supply false flags for their accounts, causing incorrect predictions; the suggested defence is for each bank to commit to its account set and prove responses are correct without revealing the account. (p. 7)[^original]  
  <sub>anchor: "each bank commits to its entire account set and proves that their response is indeed correct"</sub>
- **descriptive / limitation**: Protection mechanisms against fully malicious parties are described as possible with little overhead but are orthogonal to the work and not implemented in it. (p. 7)[^original]  
  <sub>anchor: "implementing these protection mechanisms is orthogonal to our work."</sub>

## 6 EXPERIMENTAL RESULTS

- **descriptive / finding or result**: The experiments evaluate accuracy, privacy leakage and running time; a centralized approach on S without bank flags serves as baseline, then a federated approach is evaluated. (p. 7)[^original]  
  <sub>anchor: "We first evaluate a centralized approach running on S without taking the additional flags held by Banks into account"</sub>
- **descriptive / finding or result**: Combining S's transaction data with bank account information in a centralized solution significantly boosts model accuracy. (p. 7)[^original]  
  <sub>anchor: "Combining S’s transaction data with account information from the banks in a centralized solution significantly boosts"</sub>
- **descriptive / finding or result**: Privacy mechanisms in the federated solution (MPC, noise injection) use bank account information with minimal privacy leakage to S during training. (p. 7)[^original]  
  <sub>anchor: "Privacy mechanisms used in our federated solution (e.g., MPC, noise injection) harness the benefit of bank account information"</sub>
- **descriptive / finding or result**: The inference implementation leaks at most 1 bit (normal versus abnormal) about the bank account flag by design, while bank account flags can take 13 statuses in the PETs challenge datasets, one normal and the rest abnormal. (p. 7)[^original]  
  <sub>anchor: "Our inference implementation leaks at most 1-bit of information (normal v.s. abnormal) about the bank account flag by design"</sub>
- **descriptive / finding or result**: Caching and statistical properties of the data accelerate the federated solution by 100x compared with a naive implementation. (p. 7)[^original]  
  <sub>anchor: "we accelerate our federated solution by 100x compared to a naïve implementation"</sub>

## 6.1 Centralized Approach

- **descriptive / method**: The centralized model is a multi-layer perceptron trained with SGD, with three hidden layers of 256, 64 and 16 nodes using ReLU; it was chosen for good training performance at moderate size and because the per-sample gradient matches the network size, keeping messages reasonable. (p. 7)[^original]  
  <sub>anchor: "Our MLP architecture has three hidden layers with 256, 64 and 16 hidden nodes using ReLU activation."</sub>

## 5 PROOF OF PRIVACY

- **descriptive / limitation**: The authors state that their approach can still protect against a fully malicious S by initially committing to all transactions and the data gathering steps. (p. 7)[^original]  
  <sub>anchor: "Our approach can still protect against fully malicious S by initially committing on all transactions and the data gathering steps."</sub>
- **descriptive / limitation**: A fully malicious S could arbitrarily poison the model or infer account flags by training on a crafted batch of transactions that all share the same receiving account. (p. 7)[^original]  
  <sub>anchor: "infer information about the account flag by training on a crafted batch of transactions with the same receiving account"</sub>

## 6.1 Centralized Approach

- **descriptive / data or feature**: Velocity features are computed for each transaction from the average, minimum and maximum amount of transactions from the sender, to the receiver, and between the sender-receiver pair over the last 20 transactions, the last 7 days and the last 28 days prior to the transaction. (p. 8)[^original]  
  <sub>anchor: "we examine the average, min and max amount of transactions from the sender, to the receiver and between the sender-receiver pair"</sub>
- **descriptive / data or feature**: All amounts are converted into USD, and 17 numerical features that are most impactful on the developer dataset are kept for the PETs challenge. (p. 8)[^original]  
  <sub>anchor: "we keep 17 numerical features that are the most impactful on the developer dataset."</sub>
- **descriptive / context**: The original training set is highly unbalanced, with only 1 out of roughly 1000 transactions anomalous; anomalous transactions are upsampled uniformly at random to create a balanced set. (p. 8)[^original]  
  <sub>anchor: "The original training set is highly unbalanced: only 1 out of ∼1000 transactions is anomalous."</sub>
- **descriptive / method**: Training uses standard SGD for 20 epochs with batch size 4092, an initial learning rate of 5e-2 decaying by a factor of 1/sqrt(t) with t the number of epochs, and weight decay of 5e-4. (p. 8)[^original]  
  <sub>anchor: "We train the model using standard SGD optimizer for 20 epochs with batch size 4092."</sub>

## 6.2 Federated Approach

- **descriptive / method**: The federated approach is implemented with the Opacus library for per-sample gradients and an oblivious transfer functionality based on a customised libOTe library. (p. 8)[^original]  
  <sub>anchor: "We implement our federated approach using the Opacus libary [28] which enables us to compute a per-sample gradient."</sub>
- **descriptive / finding or result**: The centralized solution achieves AUPRC 0.79; the model with bank account information significantly outperforms an XGBoost tree without bank account information. (p. 8)[^original]  
  <sub>anchor: "Our centralized solution achieves AUPRC=0.79 on our dataset."</sub>
- **descriptive / finding or result**: The federated solution achieves AUPRC 0.49 after just one epoch of training, and a local simulation with 20 epochs reaches AUPRC 0.70, which is still significantly better than the centralized solution without bank information. (p. 8)[^original]  
  <sub>anchor: "Our federated solution achieves AUPRC=0.49 with just one epoch of training."</sub>

## 6.4 Optimizations

- **descriptive / method**: Because OT count equals the number of anomalous transactions in training, anomalous transactions are upsampled to a 1:1 ratio in the centralized solution and to 1:10 in the federated solution, reducing communication cost by a factor of 20. (p. 8)[^original]  
  <sub>anchor: "we upsample the anomalous transactions to a ratio of 1:10 with respect to the non-anomalous ones in order to reduce the communication cost by a factor of 20."</sub>
- **descriptive / method**: OT results are cached per account: S inputs two random encryption keys per account, the bank selects one via its flag, and S encrypts the two gradients; this reduces the number of OTs by the number of epochs (20) and halves interaction rounds. (p. 8)[^original]  
  <sub>anchor: "This optimization can effectively reduce the number of OTs needed by the number of epochs performed in training"</sub>

## 6.5 Efficiency and Scalability

- **descriptive / method**: Five time-cost components are identified: feature extraction, SGD computation, message preparation, OT computation, and communication. (p. 8)[^original]  
  <sub>anchor: "We identify five main components of time costs."</sub>
- **descriptive / method**: Feature extraction and OT computation are unit tested, while the other components are estimated from three reference implementations: centralized SGD only, a semi-distributed version passing messages in memory, and the full implementation. (p. 8)[^original]  
  <sub>anchor: "We conduct unit test on feature extraction and OT computation for the running time."</sub>
- **descriptive / finding or result**: Communication cost is identified as the main bottleneck of the Flower-based solution; the overhead includes tensor movement between CUDA and CPU, disk I/O simulating message passing, and re-initializing client context each round. (p. 8)[^original]  
  <sub>anchor: "The result shows that the communication cost is the main bottleneck for our solution in flower."</sub>
- **descriptive / finding or result**: Table 3 timings for one epoch: feature extraction about 2,000 s; SGD-only learning under 100 s; with message preparation about 600 s; with distributed simulation in Flower about 3 h; OT computation under 200 s. (p. 8)[^original]  
  <sub>anchor: "∼2,000s|_<_100s|∼600s|∼3h|_<_200s|"</sub>
- **descriptive / finding or result**: Communication cost of the model is proportional to dataset size times model update size; it can be reduced by querying bank flags of high uncertainty, and performance scales well with the number of bank partitions because the total number of OTs is independent of partitions. (p. 8)[^original]  
  <sub>anchor: "The total number of OTs is independent of number of partitions."</sub>
- **descriptive / finding or result**: Message preparation on CPU is significantly more costly than gradient computation on GPU, so a higher CPU:GPU ratio could boost efficiency; in the submission bank communication over partitions was run serially, so more partitions cost slightly more time. (p. 8)[^original]  
  <sub>anchor: "The message preparation (serialization/deserialization) done in CPU is significantly more costly than gradients computation in GPU."</sub>
- **descriptive / limitation**: The PETs challenge handlers require all messages, client states and models to be written to disk for integrity checks, forcing clients to re-initialise context from disk at each stage; in the real world clients could stay alive and stream messages. (p. 9)[^original]  
  <sub>anchor: "For integrity check purposes, all the messages and clients status including the models are required to be written to the disk."</sub>

## 6.6.1 Training Time

- **descriptive / typology or red flag**: Threat model: S attempts to learn accounts' bit flags from the banks, already knows the model architecture, training parameters and all transaction features except the receiver account flag, and knows the status flags of a fraction alpha of bank accounts. (p. 9)[^original]  
  <sub>anchor: "In addition, we also assume S already knows the status flags of a fraction (denoted by _𝛼_ ) of the bank accounts."</sub>
- **descriptive / finding or result**: Two attacker strengths are considered: a strong attacker with alpha 0.2 and a weak attacker with alpha 0.05. (p. 9)[^original]  
  <sub>anchor: "We consider both a strong ( _𝛼_ = 0 _._ 2) and a weak ( _𝛼_ = 0 _._ 05) attacker."</sub>

## 6.5 Efficiency and Scalability

- **descriptive / finding or result**: The authors state that feature extraction could be significantly accelerated in the real world by map-reduce over a cluster, which is described as a common practice in industry. (p. 9)[^original]  
  <sub>anchor: "this feature extraction procedure can be significantly accelerated by map-reduce over a cluster"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Privacy-Preserving Financial Anomaly Detection via Federated Learning & Multi-Party Computation" (2023-06-10). https://arxiv.org/abs/2310.04546
