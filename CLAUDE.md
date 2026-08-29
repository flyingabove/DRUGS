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

## MCP servers (`.mcp.json`) — each one launch-tested, not just configured

**Working:**
- `biocontext-kb` — Open Targets, UniProt, Reactome, KEGG, AlphaFold, Ensembl, ClinicalTrials.gov.
- `gget-mcp` — Ensembl sequence retrieval, BLAST/BLAT.
- `patent-mcp-server` — patent/trademark search, no key needed for core tools (ODP/PTAB need a free
  USPTO account). Required pinning `mcp<2` — the published package breaks on current `mcp`.

**Blocked, not loaded** (`_disabled_needs_node_24` key in `.mcp.json`): `chembl-mcp-server`,
`pubchem-mcp-server` — both require Node ≥24; this machine runs 10.15.3. `nvm install 24` hangs on a
UAC prompt this session can't answer — needs the user to run it as Administrator, or install Node 24
directly, then move the config back into `mcpServers`. Use `compound-profile`'s script until then.

Prefer working MCPs over the raw-script skills for exploratory work. Same rule as everything else:
verify one real record before trusting output in a doc (see
[docs/research/mcp-landscape.md](docs/research/mcp-landscape.md)).
