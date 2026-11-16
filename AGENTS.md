# Agent instructions: Financial Crime Knowledge Bundle

This repository is a curated, citation-grounded knowledge base about **financial crime detection, prevention
and regulation** for the **UK, US and international standard-setters**, plus research on detection methods
(models, features, graph analytics, explainability, model risk) and counterparty/external intelligence.

It is written in the **Open Knowledge Format (OKF) v0.2**: a directory of Markdown files with YAML
frontmatter, designed so an agent with **no vector store and no RAG pipeline** can find, read and cite the
knowledge using ordinary file navigation and text search.

**Snapshot date: 2026-11-16.** Everything here reflects the sources as collected on that date.

---

## 1. Ground rules (read first)

1. **Accuracy over fluency.** Every factual statement you make about regulation, standards, typologies or
   research must be supported by a file you actually opened in `kb/`. If you could not find support,
   say so. Never invent a provision number, threshold, date, paragraph reference or citation.
2. **Cite what you read.** Cite the specific part file (and page marker) that supports each claim, plus
   the original document's URL from the `resource` field. See section 6.
3. **Respect normative force.** Never present guidance as law, a consultation as final, an academic finding
   as a regulatory expectation, or an international standard as directly binding on a firm. Each source's
   `normative_force` tells you what it is (section 5).
4. **Respect currency.** Check `legal_status` / `status` before relying on a source. Superseded or withdrawn
   documents must not be presented as current (see `kb/registers/status-and-supersession.md`).
5. **Verbatim vs digest.** `text-NNN.md` files are the original wording and may be quoted. `digest-NNN.md`
   files are verified paraphrases (the licence forbids reproducing the text): use them for substance, but do
   not put digest sentences in quotation marks as if they were the source's words.
6. **This bundle outranks your built-in knowledge** for anything it covers, as of the snapshot date. Section 7
   explains how to combine the two.

---

## 2. What is in the bundle

| Item | Count |
|---|---|
| Source documents | 534 |
| Sources with verbatim full text (licence permits reproduction) | 376 |
| Sources with verified digests (licence does not permit reproduction) | 158 |
| Jurisdictions | UK 139, US 212, International 88, EU 5, HK 1, non-jurisdictional research 89 (a source can have several) |
| Topic domains | 36 (see `kb/taxonomy/domains.md`) |

Source mix: UK legislation and regulators (FCA, PRA/BoE, HM Treasury, Home Office, NCA, OFSI, HMRC,
Companies House, ICO, courts), US law and regulators (Federal Register rules, FinCEN, OCC, FRB, FFIEC, OFAC,
DOJ, Treasury, GAO, NYDFS, NIST), international bodies (FATF, Basel Committee/BIS, FSB, Egmont Group,
Wolfsberg Group, UNODC/UN, IMF, World Bank, APG, Europol, INTERPOL, EBA, JMLSG), and academic research
(arXiv and journal papers on AML/fraud detection methods).

**Not in scope / known gaps:** jurisdictions other than UK/US/international (EU, HK coverage is minimal);
anything published after the snapshot; some statutes are held only in part; a few sources hold only a
landing page or abstract, and a few PDFs have partly unreadable text. All of these are listed in
`kb/registers/known-gaps.md`. Check it when an answer depends on one of those sources.

---

## 3. Layout

```
AGENTS.md                      <- you are here (setup and integration instructions)
README.md                      <- human overview
.github/copilot-instructions.md <- short always-on rules for GitHub Copilot
kb/                            <- the OKF bundle (all knowledge lives here)
  index.md                     <- root directory listing (okf_version: "0.2")
  log.md                       <- update history
  start-here.md                <- condensed navigation and citation protocol
  registers/                   <- source register, status & supersession, licensing, known gaps
  taxonomy/                    <- normative force, instrument types, tiers, domains, jurisdictions
  topics/<domain>.md           <- Topic Hub: every source on a topic, by jurisdiction and authority
  jurisdictions/<code>.md      <- Jurisdiction Hub: every source for UK / US / INTL / ..., by issuer
  issuers/<issuer>.md          <- Organisation: every source from one issuer, by normative force
  sources/<issuer>/<source_id>/
      overview.md              <- Source Document: metadata, status, licence, contents table
      text-001.md ...          <- Source Text: verbatim extracted text, about 6,000 tokens per part
      digest-001.md ...        <- Source Digest: verified paraphrased knowledge points (restricted licences)
  evaluation/self-test-questions.md <- 73 questions with the sources a correct answer cites
```

Every `.md` file under `kb/` except `index.md` and `log.md` is an OKF **concept** with YAML frontmatter.
The `type` field tells you what it is:

| `type` | Purpose | Key frontmatter fields |
|---|---|---|
| `Source Document` | One per source: the entry point | `source_id`, `issuer`, `jurisdictions`, `tier`, `instrument_type`, `normative_force`, `publication_date`, `effective_date`, `legal_status`, `superseded_by`, `content_mode`, `licence`, `parts_total`, `text_quality_warnings`, `resource` (original URL) |
| `Source Text` | Verbatim text of one part | same metadata, plus `part`, `parts_total` |
| `Source Digest` | Paraphrased, verified points of one part | same, plus `digest_points` |
| `Topic Hub` | Sources on one domain | `domain_id` |
| `Jurisdiction Hub` | Sources for one jurisdiction | `jurisdiction` |
| `Organisation` | Sources from one issuer | `issuer_id`, `tier` |
| `Register` | Cross-cutting tables | |
| `Taxonomy` | Controlled vocabularies | |
| `Evaluation Set` | Self-test questions | |
| `Guide` | Usage instructions (`kb/start-here.md`) | |

Links between files are relative Markdown links, so they work on GitHub, in VS Code and for agents. A path
beginning with `/` inside frontmatter (for example `superseded_by: /sources/frb/.../overview.md`) is relative
to `kb/`.

### Markers inside text parts

- `[p. 12]` or `[pp. 12-13]`: the page(s) in the original where the following text appears. Use it in citations.
- `[ref: FCG 3.2.1]` (or `Reg 33`, `R 10` and similar): a paragraph or provision reference detected at that point.
- Headings reproduce the document's own section hierarchy.

### Digest points

Each point looks like this:

```
- **expected / expectation**: <paraphrased point> (p. 12)[^original]
  <sub>anchor: "<6-20 word verbatim phrase from the original>"</sub>
```

`strength` is one of `mandatory | expected | recommended | permissive | descriptive`. `kind` is one of
`requirement | expectation | recommendation | definition | typology or red flag | method | data or feature |
finding or result | case example | limitation | context`. The anchor is a short verbatim phrase that was
machine-checked to occur in the original. Use it to locate the passage in the original before quoting exact
wording.

---

## 4. How to find knowledge (no vector store needed)

Use **progressive disclosure**: start broad, open as few files as needed, then read the relevant parts in
full.

1. **Classify the question.** Work out the jurisdiction (UK / US / international / none), the topic (map it to a
   domain in `kb/taxonomy/domains.md`) and the kind of answer needed (a legal requirement, a supervisory
   expectation, a typology or red flag, a detection method, an empirical finding).
2. **Exact-term search first** when the question names something specific: a provision ("Regulation 33",
   "31 CFR 1020.320", "SYSC 6.3", "Recommendation 16"), a document ("SR 26-2", "SS1/23", "JMLSG"), a defined
   term ("beneficial owner", "politically exposed person") or a typology ("smurfing", "TBML"). Search the
   text under `kb/sources/` (case-insensitive) and also try spelling variants: "programme"/"program",
   "organisation"/"organization", hyphenation, abbreviations.
3. **Otherwise navigate.** `kb/index.md` -> the matching `kb/topics/<domain>.md` and/or
   `kb/jurisdictions/<code>.md` -> pick candidate sources by normative force, status and date -> open each
   candidate's `overview.md` -> use its **Contents** table (page ranges and section headings per part) to choose
   which `text-NNN.md` / `digest-NNN.md` to open.
4. **Filter by frontmatter** when useful, for example search for `normative_force: legal_requirement`,
   `legal_status: consultation`, `jurisdictions:\n- UK`, `instrument_type: advisory_alert`, or `domains:` values.
5. **Read in full, not in fragments.** Open the whole part that contains the hit. Also open the neighbouring
   part (linked as "previous/next part") when the passage continues, or when definitions, scope, exceptions or
   transitional provisions are likely to sit elsewhere.
6. **Triangulate.** For requirements, find the primary source (law, rule or regulator guidance) rather than a
   secondary summary. For methods and research, prefer several papers over one, and report disagreements.
7. **Stop and say so** if the bundle does not cover the question. Do not fill the gap silently with built-in
   knowledge (see section 7).

`kb/evaluation/self-test-questions.md` lists 73 realistic questions and the sources a correct answer must
cite. Use it to check your navigation.

---

## 5. Authority and conflicts

Rank evidence in this order:

1. **Jurisdiction match.** For a UK firm's obligation, UK law and UK regulators outrank US or international
   material, and vice versa. International standards (FATF, BCBS) shape national law but bind **states and
   supervisors**, not firms directly.
2. **Normative force**, from strongest to weakest (`kb/taxonomy/normative-force.md`):
   `legal_requirement` > `regulatory_expectation` > `supervisory_expectation` > `international_standard` >
   `empirical_observation` > `industry_practice` > `academic_finding` > `expert_interpretation` > `hypothesis`
   (consultations, proposals) > `vendor_recommendation`.
3. **Currency.** `current` beats `consultation`. `superseded`, `withdrawn` and `repealed` are historical only.
   `unknown` means the status was not confirmed: say so if it matters. Example: Federal Reserve **SR 26-2**
   (17 Apr 2026) supersedes **SR 11-7** and **SR 21-8**.
4. **Recency** within the same issuer and topic: the newer document wins unless the older one is the binding
   instrument and the newer one only comments on it.
5. **Tier** (`kb/taxonomy/tiers.md`) breaks remaining ties: issuer tier 1 (law/regulator) > 2 (standard setter)
   > 3 (academic) > 4 (industry) > 5-7.

When two sources genuinely conflict, present both with citations and explain which governs and why. Do not
average them.

---

## 6. Citing

For each claim, cite the part file and page, and give the original URL once per source:

> Firms must apply enhanced due diligence where ... ([MLR 2017, part 3, p. 41](kb/sources/uk-legislation/<id>/text-003.md); original: <https://www.legislation.gov.uk/...>)

- Cite the **part** file you read, not only the overview.
- For digest sources, add "(digest)" and do not quote: write *"the Wolfsberg Group recommends ... (digest, p. 4)"*.
  If exact wording is needed, tell the user to check the original at `resource` and give the anchor phrase.
- Give the **normative force** and **status** when they matter: "(FCA guidance, not a rule)",
  "(consultation, not final)", "(superseded by ...)".
- Never cite a file you did not open in this session.

---

## 7. Combining this bundle with your built-in knowledge

You keep using your general knowledge. This bundle is the **authoritative reference layer** for its
scope. Apply these rules:

| Situation | What to do |
|---|---|
| The bundle covers the point | Answer from the bundle and cite it. Use built-in knowledge only to explain or structure, not as evidence. |
| Your built-in knowledge agrees with the bundle | Fine, but the citation is still the bundle file. |
| Your built-in knowledge **conflicts** with the bundle | Prefer the bundle. If you believe the law or guidance changed **after 2026-11-16**, say: "the bundle (snapshot 2026-11-16) says X; this may since have changed to Y; verify against the original." Never silently replace the bundle's statement. |
| The bundle is silent | Say the bundle does not cover it. You may then give a clearly labelled answer from general knowledge ("not from the knowledge bundle; verify"), without invented citations. |
| Organisation-internal material (your firm's own policies, standards, procedures, model documentation) | Internal policy governs **how your firm operates**. The bundle supplies the **external** regulatory, supervisory and research context. Do not override internal policy with the bundle: point out gaps or inconsistencies between them, cite both, and flag them for a human decision. |
| Generic technical knowledge (statistics, ML, coding) | Use freely. When it informs a regulated decision such as model validation or tuning, also cite the relevant governance sources (for example model risk guidance) from the bundle. |

When you build on this bundle in another knowledge system (for example an internal wiki or another OKF bundle):

- Keep each source's `source_id`, `resource`, `normative_force`, `legal_status`, `publication_date` and
  `content_mode` with any knowledge you derive from it.
- Link to the concept files instead of copying them. If you must copy, copy whole parts and keep the
  frontmatter.
- Mark anything you write yourself with OKF `generated: { by: <agent>/<version>, at: <ISO time> }`, and add a
  `sources:` entry pointing back to the part file. Do not add a `verified` entry unless a check actually ran.
- Do not edit `text-NNN.md` files; they are verbatim records. Corrections belong in a new concept that links
  to the part and explains the correction, plus a `log.md` entry.

---

## 8. Answer pattern for compliance and detection questions

1. **Direct answer** in 1-3 sentences.
2. **Basis**: the requirement or finding, with source, normative force, status and page citations.
3. **Detail**: conditions, thresholds, exceptions, timelines, red flags or method specifics, each cited.
4. **Cross-jurisdiction or alternative views**, where relevant.
5. **Caveats**: consultation or unknown status, digest-only wording, text-quality warnings, possible
   post-snapshot changes, gaps in the bundle.

---

## 9. How this bundle was built and checked

- **Collection.** Official and academic sources were discovered, checked against their publisher, and
  approved in a human review queue (`source_selection` in each overview: `human_verified`, or
  `auto_verified` for documents checked automatically against official sites).
- **Full text.** Text was extracted from the original PDF or HTML (pymupdf4llm / HTML parser), split at
  section boundaries, and copied **verbatim** into `text-NNN.md` in reading order with page and provision
  markers. A validation step checks that every extracted passage appears exactly once in the bundle, in order.
  Extraction artefacts from the source files remain: table layout may be flattened, and characters a PDF
  font did not encode show as `�` (listed in `kb/registers/known-gaps.md`).
- **Licensing.** Full text only where the licence permits reproduction for commercial or internal use: US
  federal works (public domain), UK Open Government Licence, FCA reuse terms, EU reuse policy (CC BY 4.0),
  NCA (OGL), CC BY / CC0 papers. FATF, BCBS/BIS, FSB, Wolfsberg, JMLSG, Egmont, UN/UNODC, IMF, World Bank,
  APG, INTERPOL, PRA/BoE, NYDFS, HKMA, and papers without an open licence are represented by digests. See
  `kb/registers/licensing.md`.
- **Digests.** Each restricted part was digested into fine-grained knowledge points by Claude agents (Sonnet 5.5; Opus 5.5 for the first FATF parts). Every
  point then had to pass three checks: (a) its anchor phrase occurs verbatim in the original part (deterministic
  script); (b) a separate, independent Claude Opus 5.5 agent that did not write the digest judged it fully supported against the
  excerpt, with numbers, qualifiers and normative strength correct; (c) it does not copy more than 25 consecutive
  words (deterministic script). Failing points were rewritten once by a digest agent and re-judged; points that still
  failed were dropped. Frontmatter `verified` records these checks. The digests are **machine-confirmed, not
  human-reviewed** (OKF trust tier).
- **Navigation pages** (hubs, registers, indexes) are generated deterministically from the source metadata.
  "Curator note" sections in overviews were machine-written when each source was selected. Use them for
  routing only.

---

## 10. Setting up GitHub Copilot with this repository

- **Agent mode or coding agent in this repository:** Copilot reads `AGENTS.md` and
  `.github/copilot-instructions.md` automatically. Ask questions directly; the agent should search and open
  files under `kb/`.
- **Using it from another repository:** add this repository as a folder in a multi-root VS Code workspace, or
  as a git submodule (for example at `knowledge/fincrime`). Then copy the rules from
  `.github/copilot-instructions.md` into that repository's own `.github/copilot-instructions.md`, adjusting
  paths to `knowledge/fincrime/kb/...`.
- **Context budget:** each part is about 6,000 tokens or less, so open individual parts rather than whole
  folders. Hubs and registers are larger listings: search them instead of reading them end to end.
- **Updating:** a newer snapshot replaces `kb/` wholesale. `kb/log.md` records what changed, and each concept's
  `generated.at` shows when it was produced.
