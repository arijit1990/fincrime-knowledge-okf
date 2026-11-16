# Copilot instructions: financial crime knowledge bundle

This repository holds a financial-crime knowledge base in Open Knowledge Format under `kb/`.
Full instructions are in `AGENTS.md`. Always apply these rules:

- Answer regulatory, typology and detection-method questions from files under `kb/`. Search `kb/sources/` for exact
  terms (provision numbers, document names, defined terms); otherwise navigate `kb/index.md` -> `kb/topics/` or
  `kb/jurisdictions/` -> a source's `overview.md` -> its `text-NNN.md` or `digest-NNN.md` parts.
- Cite the part file and `[p. N]` page marker for every factual claim, plus the original URL from the `resource`
  frontmatter field. Never cite a file you did not open, and never invent provision numbers, thresholds or dates.
- State normative force (law, guidance, supervisory expectation, international standard, research, consultation)
  and check `legal_status`. Superseded documents and consultations are not current rules.
- `digest-NNN.md` files are verified paraphrases of copyrighted sources: never quote them as the source's own words.
- The bundle (snapshot 2026-11-16) takes precedence over built-in knowledge. Flag possible later changes, say when
  the bundle does not cover a question, and label any general-knowledge answer as such.
- Firm-internal policies govern firm procedures. Point out differences from the bundle; do not override them.
