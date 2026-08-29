# Project Instructions

- When asked to commit and push "everything," stage and push all untracked/changed files —
  do not hold files back over privacy or content-sensitivity concerns. Ordinary secret-scanning
  (API keys, credentials, .env files) still applies before any commit; this only waives holding
  back legitimate content for privacy reasons.
- Always write succinctly. No verbose explanations, no padding. Say it in as few words as possible,
  in chat and in docs.
- **The user has no biology background.** Always answer in the most human language possible. Explain
  terms when they first appear, use everyday analogies, and give enough context that the reasoning is
  followable. The user is intelligent and not a beginner at thinking — they are simply not a biologist.
  Do not dumb down the substance; do dump the jargon. Never use an acronym without saying what it is.
- **After every iteration of work on the drug, always end by showing the drug status table** produced
  by the `judge-drug` skill. Do not wait to be asked for it.

## How to execute work

- **Always plan before executing.** Write an explicit todo list and a dependency graph showing what
  blocks what. Show both before starting.
- **Parallelise to the maximum the graph allows.** Anything with no unmet dependency starts
  immediately — independent tool calls in a single message, long jobs backgrounded. Only serialise
  where a real dependency exists.
- **Follow the graph when executing**, and say which node is running. When a result changes the graph
  — a branch is pruned, a dependency disappears — say so and show the revised path rather than
  silently continuing.
- **Commit every significant change to git**, with a message stating what changed and why. Significant
  = a new finding, a corrected claim, a lead change, a skill update, a tooling fix. Do not batch
  unrelated changes into one commit.

## MCP servers (`.mcp.json`)

- `biocontext-kb` — Open Targets, UniProt, Reactome, KEGG, AlphaFold, Ensembl, ClinicalTrials.gov.
  Use for target/pathway/structure lookups.
- `gget-mcp` — Ensembl sequence retrieval, BLAST/BLAT.
- `chembl-mcp-server` — compound-target bioactivity (IC50/Ki/EC50), mechanism, indication.
- `pubchem-mcp-server` — compound structure/property/bioassay search.

Prefer these over the raw-script skills for exploratory work. Same rule as everything else: verify
one real record before trusting output in a doc (see
[skills-and-mcp-integration-plan.md](docs/skills-and-mcp-integration-plan.md) §5).
