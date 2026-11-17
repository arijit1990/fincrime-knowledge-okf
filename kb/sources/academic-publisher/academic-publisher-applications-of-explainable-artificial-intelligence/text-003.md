---
type: Source Text
title: Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature - part 3 of 6 (pp. 19-33)
description: 'Verbatim extracted text, pp. 19-33: XAI'
resource: https://link.springer.com/article/10.1007/s11301-023-00320-0
tags:
- academic_finding
- academic_paper
- explainability
- global_academic
- responsible_ai
status: stable
source_id: academic-publisher-applications-of-explainable-artificial-intelligence
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2023-02-28'
legal_status: unknown
part: 3
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T17:21:51Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T17:21:51Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1007/s11301-023-00320-0
  title: Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature
  author: org:academic_publisher
  last_modified: '2023-02-28T00:00:00Z'
---

# Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-02-28), part 3 of 6, pp. 19-33. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[pp. 19-20]

Informativeness 42 Bekiros (2010); Kamalloo and Abadeh (2010); Ghandar and Michalewicz (2011); Chen et al. (2012); Hayashi

Transferability 11 Bastos (2010); Kim et al. (2011); Jarovsky et al. (2018); Horel et al. (2018); Zhang et al. (2019); Oppold and

Causality 6 Bastos (2010); Ariza-Garzón et al. (2020); Kraus et al. (2020); Schnaubelt et al. (2020); Kong et al. (2020);

Trustworthiness 10 Ariza-Garzón et al. (2020); Zheng et al. (2020); Attanasio et al. (2020); Kong et al. (2020); Maree et al. (2020);

Table 3 Overview of XAI in Finance papers dealing with specific XAI goals (n = 60)

XAI goal Count Articles

1 3

Fig. 8 Publication trend of XAI research in Finance regarding transparent models and post-hoc explainability (n = 60)

Number of Ar cle(s)

2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021

Transparent Models Post-Hoc Explainability

[p. 20]

Table 4 provides an overview of the reviewed articles and their XAI methods. Multi-method usage is possible, while six papers do not employ methods (Ghandar and Michalewicz 2011; Renault 2017; Oppold and Herschel 2019; Koshiyama et al. 2020; Daníelsson et al. 2021; Ge et al. 2021), but only deal with XAI from a high- level perspective considering goals. Thus, they are not included in Table 4 but in Table 3. The results indicate that roughly the same number of papers use transparent models (n = 26) or introduce XAI in the form of post-hoc explainability (n = 32). This balance represents researchers’ balanced preferences towards both kinds of XAI, transparent models next to post-hoc explainability, highlighting XAI in Finance as a well-recognized, established research stream. Additionally, we observe articles employing both kinds of XAI, thus comparing, e.g., neural networks and logistic regression (Adams and Hagras 2020), showing academia targeting both kinds of XAI individually and their combination and comparison. Decision trees are the most used method (n = 12) when only looking at transparent models, while general addi- tive and Bayesian models are not used. Related studies (e.g., Arrieta et al. 2019; Chou 2019) confirm decision trees to be well-employed in XAI research, but we find a different picture regarding general additive models. Relevant research concerning XAI in the form of general additive models in Finance (Berg 2007; Taylan et al. 2007; Calabrese 2012) did not appear in our search. This fact eventually hints at pos- sible limitations of this study and sparks further research as to why there has been no research on general additive models in Finance in top-tiered outlets since 2010. Looking at methods including post-hoc explainability (n = 37), we find roughly two- fifths being model-agnostic (n = 16) and three-fifths being model-specific (n = 21). Most model-specific methods deal with multi-layer neural networks (n = 14), while least model-specific methods focus on recurrent neural networks (n = 1) and none on SVMs. Among model-agnostic methods, an equal number of articles deal with explanation by simplification and feature relevance explanation (n = 5).

[pp. 20-21]

In Fig. 8, we provide an overview of the publication trend of XAI research in Finance grouped by explainability type. Research trends change over time regarding transparent models (blue) or post-hoc explainability (orange). Some papers employ both types of XAI, while others employ neither (n = 6), focusing on goals instead (see Table 3). While up to 2018, except for 2012, there has been more, or at least as much, research applying transparent models compared to post-hoc explainability,

1 3

Recurrent

neural

networks

lutional

neural

networks

Convo-

works

Multi-

Layer

neural

net-

x

Support

vector

machines

bles and

multiple

classifier

systems

Ensem-

tion

Visual

explana-

evance

explana-

tion

Feature

rel-

Model-agnostic Model-specific

tion by

simplifi-

cation

x

Bayesian models Explana-

General

additive

models

x

Rule-

base

learners

est

neigh-

bors

K-near-

Deci-

sion

trees

linear

regres-

x x

## XAI


[pp. 21-24]

Transparent models Post-hoc explainability

sion

x x

et al.

(2020)

(2010) x x

(2010) x

et al.

(2016)

zón et al.

(2020)

et al.

(2019)

Hagras

(2020)

(2020) x

Article Logistic/

Attanasio

Bastos

Bekiros

Butaru

Table 4 Overview of XAI in Finance papers applying specific XAI methods (n = 54)

Achituve

Adams and

Alam et al.

Ariza-Gar-

1 3

Recurrent

neural

networks

lutional

neural

networks

Convo-

works

x

Multi-

Layer

neural

net-

Support

vector

machines

bles and

multiple

classifier

systems

Ensem-

tion

Visual

explana-

evance

explana-

tion

Feature

rel-

Model-agnostic Model-specific

tion by

simplifi-

cation

x x

x x

Bayesian models Explana-

General

additive

models

Rule-

base

learners

est

neigh-

bors

K-near-

Deci-

sion

trees

linear

regres-

Transparent models Post-hoc explainability

sion

tachaud-

huri et al.

(2020a)

(2021) x

(2012) x

et al.

(2021)

(2019) x x

(2020) x

Celik

(2021)

Article Logistic/

Table 4 (continued)

Carta et al.

Chen et al.

Cheong

Chou

Cong et al.

Dastile and

Dat-

1 3

Recurrent

neural

networks

lutional

neural

networks

Convo-

works

x

x

Multi-

Layer

neural

net-

Support

vector

machines

bles and

multiple

classifier

systems

Ensem-

tion

Visual

explana-

evance

explana-

tion

Feature

rel-

Model-agnostic Model-specific

tion by

simplifi-

cation

Bayesian models Explana-

General

additive

models

x

x

Rule-

base

learners

est

neigh-

bors

K-near-

Deci-

sion

trees

linear

regres-

Transparent models Post-hoc explainability

sion

Zeng

(2015)

et al.

(2021)

(2021) x

tachaud-

huri et al.

(2020b)

et al.

(2015)

(2018) x

(2021) x

Article Logistic/

Duan and

Ferdaus

Guo et al.

Hayashi

Horel et al.

Ito et al.

Table 4 (continued)

Dat-

1 3

Recurrent

neural

networks

lutional

neural

networks

Convo-

works

Multi-

Layer

neural

net-

Support

vector

machines

bles and

multiple

classifier

systems

Ensem-

tion

Visual

explana-

evance

explana-

tion

Feature

rel-

Model-agnostic Model-specific

tion by

simplifi-

cation

Bayesian models Explana-

General

additive

models

x

Rule-

base

learners

x

est

neigh-

bors

K-near-

[pp. 24-27]

Deci-

sion

trees

linear

regres-

x x

Transparent models Post-hoc explainability

sion

loo and

Abadeh

(2010)

et al.

(2010)

(2011) x x

(2020) x

(2020) x

(2021) x

(2021) x

et al.

(2018)

Article Logistic/

Khandani

Kim et al.

Kong et al.

Kraus et al.

Kute et al.

Lee et al.

Table 4 (continued)

Jarovsky

Kamal-

1 3

Recurrent

neural

networks

lutional

neural

networks

Convo-

works

Multi-

Layer

neural

net-

Support

vector

machines

bles and

multiple

classifier

systems

Ensem-

tion

Visual

explana-

x

evance

explana-

tion

Feature

rel-

x

Model-agnostic Model-specific

tion by

simplifi-

cation

Bayesian models Explana-

General

additive

models

Rule-

base

learners

est

neigh-

bors

K-near-

Deci-

sion

trees

x

x x

linear

regres-

Transparent models Post-hoc explainability

sion

(2018) x

(2021) x

et al.

(2021)

et al.

(2020)

et al.

(2021)

et al.

(2020)

(2021) x

(2021) x

Article Logistic/

Table 4 (continued)

Li et al.

Liu et al.

Lusinga

Maree

Mariotti

Mayer

Nian et al.

Park et al.

1 3

Recurrent

neural

networks

lutional

neural

networks

Convo-

works

Multi-

Layer

neural

net-

Support

vector

machines

bles and

multiple

classifier

systems

Ensem-

tion

Visual

explana-

x x

evance

explana-

tion

Feature

rel-

Model-agnostic Model-specific

tion by

simplifi-

cation

Bayesian models Explana-

General

additive

models

Rule-

base

learners

x

x

est

neigh-

bors

K-near-

Deci-

sion

trees

x x x

x

linear

regres-

Transparent models Post-hoc explainability

sion

schall

(2019)

Sharma

(2019)

et al.

(2020)

Hagras

(2018)

(2015) x x

et al.

(2020)

(2019) x

Hirn-

Article Logistic/

Table 4 (continued)

Rajab and

Rosati

Saeed and

Sanz et al.

Schnaubelt

Shi et al.

Sigrist and

1 3

Recurrent

neural

networks

lutional

neural

networks

Convo-

works

Multi-

Layer

neural

net-

Support

vector

machines

bles and

multiple

classifier

systems

Ensem-

tion

Visual

explana-

evance

explana-

tion

Feature

rel-

Model-agnostic Model-specific

tion by

simplifi-

cation

Bayesian models Explana-

General

additive

models

Rule-

base

learners

est

neigh-

bors

[pp. 27-28]

K-near-

Deci-

sion

trees

linear

regres-

Transparent models Post-hoc explainability

sion

(2020) x

(2019) x

(2020a) x x

(2020b) x

(2019) x

(2020) x

(2020) x x

(2017) x

(2018) x

Article Logistic/

Table 4 (continued)

Wang et al.

Wu and Yan

Xu et al.

Yang et al.

Zhang et al.

Zhang et al.

Zhang et al.

Zheng et al.

Zhu et al.

Count 7 12 2 11 0 0 5 6 5 2 0 14 4 1

1 3

this trend recently shifted. If we consider the research-intense years of 2019–2021, the volume of research and its distribution changed. Research employing post-hoc explainability surpassed the former more popular transparent models by far with, e.g., almost four times as many papers dealing with post-hoc explainability (n = 11) than with transparent models (n = 3) in 2021. This development is in line with the general development of AI-based systems, where complex AI methods such as deep neural networks are more frequently used for decision-making.

Table 5 gives an overview of XAI methods concerning their application areas in Finance. This overview allows us to indicate blind spots, deriving fruitful avenues for future research, especially from a Finance point of view. From Table 5, we can infer underrepresented research areas in Finance, such as anti-money laundering. Up-and-coming scientists may evaluate the application of other XAI methods, e.g., rule-based learners or SVMs, to these areas to advance research and help practition- ers employ AI models complemented with explainability. Of course, it is manda- tory to investigate the absence of XAI methods applications in Finance areas derived from Table 5. Some combinations might be less than others or not fruitful at all. For instance, new researchers undertaking projects in this space should take a closer look at the Finance area of electronic financial transaction classification and try to apply XAI methods such as logistic/linear regression or visual explanation. Thus, they will advance research by supplementing the current research landscape with new insights or providing evidence for the impossibility of such an XAI method and Finance area combination. Furthermore, we may spot areas of Finance, which are already well-researched, such as risk management and portfolio optimization. These areas may benefit from applying new yet unused XAI methods, which we do not list in our overview in Table 5, or from comparing research between the methods men- tioned above to acquire a broader perspective on the subject at hand, e.g., comparing transparent models and post-hoc explainability.

[pp. 28-30]

Furthermore, we discern that research tackled some, but not all, of the most press- ing issues in Finance. Risk management is central to the Finance industry in many respects and essential for the successful continuation of a wide variety of agents. Hence, it is not surprising that prior research put much effort into researching the application of XAI in this Finance area due to its centrality to the domain (Adams and Hagras 2020). The same applies to the stock market and portfolio optimization, building blocks upon which the success of many agents in the domain of Finance grounds (Zhang et al. 2020a). Besides, anti-money laundering is one of the most pressing issues threatening financial systems (Kute et al. 2021). However, research so far has only rarely tackled this issue, posing the question of why that is the case. Classifying electronic financial transactions has recently become a differentiator in customers’ eyes. Therefore, agents in the financial domain renewed their interest in this area (Maree et al. 2020).

Hence, prior research focused on more critical and also predestinated Finance areas and evaluated the application of at least one XAI method per area. However, there is still an imbalance urging research attention in the future on the one hand concerning the application of more diverse XAI methods to several areas. On the other hand, future research should assess less urgent but still promising areas in Finance for possible application of XAI methods.

1 3

Recurrent

neural

networks

x

Convo-

lutional

neural

networks

Multi-

layer

neural

networks

Support

vector

machines

Ensem-

bles and

multiple

classifier

systems

Visual

explana-

tion

Feature

relevance

explana-

tion

tion by

simplifi-

cation

Model-agnostic Model-specific

Bayesian

models Explana-

General

additive

models

Rule-

base

learners

est

neigh-

bors

x x

Decision

trees K-near-

x x x x x x x

x x x x x x x x x x

linear

regres-

sion

Transparent models Post-hoc explainability

Money

Laun-

dering

tronic

Finan-

cial

Trans-

action

Classi-

fication

Optimi-

zation

market x x x x x x x x x

Man-

age-

ment

Anti-

Elec-

Portfolio

Stock

Risk

Table 5 Overview of XAI methods and areas of Finance research considered

Areas of

Finance Logistic/

1 3

5 Conclusion and future research avenues

[p. 30] [ref: 5.1]

To exploit AI applications’ full potential in Finance, XAI methods’ employ- ment seems promising. Using XAI instead of AI is decisive to ensure the neces- sary level of transparency and traceability required by regulatory and legal entities and achieve the trust needed for such systems to be deployed. However, research on XAI in Finance is highly dispersed over application areas and research methods (see Table 4). Frequently, researchers only investigated applying a particular XAI method to a specific use case. In this way, however, research takes place very iso- lated. This study provides an overview of previous research and aggregates prior research results to help exploit the full potential of XAI. Thus, we identify future research directions. To the best of our knowledge, there is no research reviewing the application of XAI in Finance on a broader level, albeit the necessity to implement XAI methods to ensure legally binding traceability and transparency of decisions made by the system in the financial industry. We are the first to provide an SLR and thus advance the fields of Finance, IS, and CS. This way, we contribute to con- ceptualizing the topic under investigation and answer respective calls for research. This paper aims to guide future research and to be a thorough approach to the sub- ject. To achieve this goal, we reviewed relevant Finance, IS, and CS journals next to important databases, analyzing 60 articles in detail to acquire an overview of recent research (year 2010 to year 2021) dealing with this topic. We discuss our results by summarizing the implications for both researchers and practitioners. Finally, we present the limitations of our study and avenues for future research regarding XAI in Finance.

5.1 Theoretical implications

Our research contributes to academia’s emerging interest in XAI in Finance research (see Fig. 5). In this vein, we provide an easy-to-follow, low-threshold, comprehen- sive overview for interested scholars willing to get acquainted with XAI in Finance. We provide basics of XAI method application in Finance, next to areas of Finance where XAI employment is likely fruitful and pressing. Finally, we present research trends and cluster research and discuss the combinations of XAI methods and areas of Finance existing research focused. Due to the recent increase in publications, a reasonable amount of overlap between specific research streams emerged. In a per- fect world, these scientists consolidate their work and progress together, rather than in parallel, into the future.

[pp. 30-31]

Our research offers broad guidance for scientists to understand the growing emphasis on XAI in Finance research, which we also found in other domains (Wells and Bednarz 2021; Islam et al. 2022). When looking at the disciplines that focused on XAI in Finance, we found a minority of research rooted in the Finance discipline. Thus, we especially encourage Finance researchers to evaluate how XAI may benefit their field of application. As most articles were published in outlets without a rating by VHB, we conclude that research predominantly took an application point of view,

1 3

thus, possibly, neglecting the theory-building and development part of research. We highly encourage XAI and Finance researchers to consider engaging in theory build- ing and development regarding XAI in Finance in high-ranked outlets.

When taking a closer look at the goals these papers try to achieve with the appli- cation of XAI, we notice an imbalance already highlighted by prior research (e.g., Arrieta et al. 2019). The reviewed articles mainly focus on the goals of informative- ness and confidence but rather neglect the goals of, e.g., privacy awareness, accessi- bility, and causality. Hence, research pursuing these goals might be a fruitful avenue for future research, especially as laws, e.g., the GDPR, emphasize privacy and the right to informational self-determination. Future research has to unravel this mis- match and identify potential reasons for it.

Besides, theorists may benefit from our study employing it as an overview of cur- rent research on XAI and especially in Finance. While there is research dealing with AI in IS and CS (e.g., Abdel-Karim et al. 2021; Martin 2019; Rai et al. 2019) or Finance (e.g., Cao 2020, 2022; Goodell et al. 2021; Zheng et al. 2019) or XAI in general (e.g., Arrieta et al. 2019; Ciatto et al. 2020; Doran et al. 2017; Rosenfeld and Richardson 2019; Sanneman and Shah 2020; Verhagen et al. 2021), so far, there is no paper reviewing the current state of research on XAI in Finance in leading inter- national journals and conferences. Scientists looking for the distribution of a specific XAI method in Finance find answers in our provided results. For instance, they may spot decision trees and multi-layer neural networks as well-researched XAI method applications in Finance or find an indication for the underrepresentation of, e.g., Bayesian models. Additionally, we provide interested researchers with a set of stud- ies employing both kinds of XAI, transparent models next to post-hoc explainability, in the area of Finance, thus highlighting these comparing works.

[pp. 31-32]

With our overview of XAI methods and areas of Finance, we identified blind spots for future research. We provide a summary of XAI methods, which are less researched than others. Future researchers could focus on these underrepresented areas, e.g., k-nearest neighbors or SVMs, to broaden our understanding of applicable XAI methods in Finance, albeit having to investigate the reason for this research paucity first. Similarly, we point out fewer explored still pressing areas of Finance that could benefit from additional research on XAI method applicability to provide a better understanding of (potential) XAI method employment in Finance, e.g., anti-money laundering. Besides, new researchers undertaking projects should take a closer look at the Finance area of electronic financial transaction classification and try to apply XAI methods such as logistic/linear regression or visual explana- tion. Thus, they will advance research by supplementing the current research land- scape with new insights or providing evidence for the impossibility of such an XAI method and Finance area combination. XAI applications in the Finance area of risk management, especially default and bankruptcy prediction, deserve further research, as financial institutions perform them continuously due to regulatory requirements (Adams and Hagras 2020). In addition, future research should evaluate less press- ing Finance areas for the potential application of XAI in future. Still, applying XAI models to less pressing and therefore less present Finance areas could be rewarding for the domain concerning a more comprehensive understanding.

1 3

When analyzing the contributions of the final set of papers, most models can vis- ibly outperform current industry practices and offer transparency and traceability of decisions, hence fulfilling the requirements for automating processes in Finance. Nevertheless, very few papers deal with whether the developed or applied methods and models actually meet regulatory requirements and can thus be implemented in practice (except for, e.g., Park et al. 2021). Especially in a highly-regulated appli- cation domain like Finance with legal requirements for using AI-based systems in practice, such an assessment should be part of the individual evaluations. Accord- ingly, this represents an important future research endeavor to examine and consider compliance with existing laws and regulations during the development and testing of methodologies. Summing up, we provide a research agenda for future XAI research in Finance incorporating different approaches to the issue.

[pp. 32-33] [ref: 5.2]

Finally, our research results also emphasize the need for XAI compared to mere AI deployment in Finance. However, one of the problems targeted by XAI is not new to research. One may also interpret XAI as a means of information asymmetry reduction. Information asymmetry refers to a state where a party has less or other information than their counterpart in a (planned) mutual relationship or contract (Akerlof 1970). AI implementation might create such a situation between the AI user and the AI tool when the user knows less or nothing about the inner mecha- nisms of an applied AI tool. XAI may educate the user with such knowledge, thus helping reduce the aforementioned information asymmetry. In Finance, this helps increase trust and understandability of AI systems, ultimately leading to higher adoption rates. Currently, multiple XAI methods apply to areas of Finance such as risk management and the stock market. Hence, we conclude higher relevance of information asymmetries and needs for information asymmetry reduction in these areas.

5.2 Managerial implications

Interested readers from business practice may also thrive by consulting our study. Our review provides an easy-to-follow, low-threshold, comprehensive overview for interested practitioners willing to get acquainted with XAI in Finance. Legislators, regulators, and Finance managers seeking to educate themselves benefit from our research, as we provide the basics of XAI methods employed in Finance. Addition- ally, we identify application areas in Finance where XAI employment is likely to be fruitful. We furthermore present research trends and cluster existing research, next to discussing the combinations of XAI methods and areas of Finance researched so far. As academia preferred the methods of real market datasets and experiments, it adds to this study’s practical applicability, showing practitioners that XAI is already well-connected to, e.g., real market datasets and thus more readily available for implementation.

Research on XAI in Finance is dispersed and thus makes it difficult for practition- ers to get an overview of possibly suitable XAI methods for a specific application problem or to fathom possible areas of application for XAI methods. Our study maps XAI methods and areas of Finance, thus providing easy access to the deployment of

1 3

XAI methods in practice. Hence, Finance managers planning to adopt XAI might consider our work an initial overview. Looking for existing XAI applications in their specific Finance areas, they may consult our study to learn about ready-to-employ solutions to add transparency and explainability to their yet black-box nature AI- based systems or not-yet automated processes. Alternatively, existing knowledge in the company about specific XAI models can be used, and possible application sce- narios can be identified.


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: Patrick Weber, K. Valerie Carl, Oliver Fast Hinz, "Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature" (2023-02-28). https://link.springer.com/article/10.1007/s11301-023-00320-0
