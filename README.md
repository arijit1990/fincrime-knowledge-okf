# Financial Crime Knowledge Bundle (OKF)

A curated knowledge base on **financial crime detection, prevention and regulation** for the UK, the US and
international standard-setters. It also covers research on detection methods (machine learning, graph analytics,
features, explainability, model risk) and counterparty/external intelligence. It is packaged in
[Google Cloud's Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
so that AI agents without vector search or RAG (for example GitHub Copilot) can navigate and cite it.

- **534 sources**: laws and rules, regulator and supervisory guidance, enforcement actions, FATF/BCBS/Wolfsberg/Egmont
  and other international standards, typology reports, national risk assessments and academic research.
- **376** are held as **verbatim full text**, where the licence permits reproduction. **158** are held as **verified
  digests**, where the licence does not.
- Every file links back to the original document. Status, supersession, licensing and known gaps are tracked in
  `kb/registers/`.
- **Snapshot date: 2026-11-16.**

## Start

- Agents: read [AGENTS.md](AGENTS.md). GitHub Copilot also picks up [.github/copilot-instructions.md](.github/copilot-instructions.md).
- People: open [kb/index.md](kb/index.md), then a [topic hub](kb/topics/) or [jurisdiction hub](kb/jurisdictions/).

## Layout

```
kb/index.md          root listing (okf_version 0.2)
kb/start-here.md     short usage guide
kb/registers/        source register, status & supersession, licensing, known gaps
kb/taxonomy/         normative force, instrument types, tiers, domains, jurisdictions
kb/topics/           one hub per topic domain
kb/jurisdictions/    one hub per jurisdiction
kb/issuers/          one page per issuing organisation
kb/sources/<issuer>/<source_id>/overview.md, text-NNN.md | digest-NNN.md
kb/evaluation/       self-test questions with expected sources
tools/validate_okf.py  conformance and link checker
```

## Validate

```bash
python tools/validate_okf.py
```

The script needs Python 3.10+ and PyYAML. It checks OKF v0.2 conformance (frontmatter and `type` on every concept,
index and log structure), that every link resolves, and that every part listed in each overview exists.

## Licensing

The original documents remain the property of their publishers. Verbatim text is included only under licences
that permit reproduction (US federal public domain, UK Open Government Licence v3.0, FCA reuse terms, EU reuse
policy, CC BY and CC0). Attribution is given in every file. Other sources are summarised as digests with short
anchor phrases, and their original wording should be read at the linked source. Per-source details are in
[kb/registers/licensing.md](kb/registers/licensing.md). Digests and navigation pages were produced for internal
reference use. They are not legal advice.
