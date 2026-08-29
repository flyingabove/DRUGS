# Skills & MCP Integration Plan

Status: **4 MCP servers installed** (`.mcp.json`), see §6a. Skills library (K-Dense-AI) and
credential-gated items (DrugBank, Tamarind, ToolUniverse) not installed. Researched from three
sources the user provided (Claude for Life Sciences announcement, the Agent Skills blog post, and a
DrugBank skill listing) plus verification of what those sources pointed to.

## 0. What This Doc Is For

We already hand-built two things that overlap heavily with what exists off-the-shelf:

- [compute-pipeline-plan.md](compute-pipeline-plan.md) specs a small-molecule generative/docking/
  ADMET stack to build from scratch (Section 4).
- `.claude/skills/{target-profile,compound-profile,literature-search,...}` are hand-written Python
  scripts making raw `requests.get()` calls to ChEMBL/PubMed/Open Targets — functional (verified
  yesterday) but thin: one script, one JSON blob, no iterative querying, no maintenance from anyone
  but us.

The ecosystem below replaces significant chunks of both with maintained, richer tooling. **This is a
menu, not an install script.** Installing an MCP server grants it tool-execution and network access;
per this session's own norms, that is a more consequential action than reading a web page, and I'm
not adding any of it without a specific go-ahead on which items.

---

## 1. What Each Source Actually Contained

### 1.1 [Claude for Life Sciences](https://www.anthropic.com/news/claude-for-life-sciences) (Anthropic, official)

**MCP connectors named:** Benchling (ELN), BioRender (figures), PubMed, Scholar Gateway (Wiley),
Synapse.org, 10x Genomics. Plus existing Google Workspace/SharePoint/Databricks/Snowflake integrations.

**Skills named:** `single-cell-rna-qc` (scverse-based QC for scRNA-seq).

**The actual repo behind this** (found by verifying, not in the announcement itself):
[anthropics/life-sciences](https://github.com/anthropics/life-sciences) — the Claude Code Marketplace
for this launch. Hosts `marketplace.json` (a plugin index), not the MCP servers themselves. Confirmed
contents: MCP servers for PubMed/BioRender/Synapse/Scholar Gateway/10x Genomics/Benchling; skills for
single-cell RNA QC, lab-instrument-data-to-Allotrope-format conversion, Nextflow pipeline development,
scvi-tools.

**Relevance to us:** Low-to-medium. This is built for wet-lab teams with an ELN (Benchling), a
sequencing core (10x Genomics), and institutional data warehouses (Databricks/Snowflake) — we have
none of those. **Synapse.org** is the one item worth a second look: it hosts public cancer genomics
datasets and could be a route to Beat AML or TCGA-LAML data for Phase 0 of
[aml-lsc-drug-discovery-plan.md](aml-lsc-drug-discovery-plan.md), which currently has no concrete
data-access plan beyond naming the datasets.

### 1.2 [Agent Skills](https://claude.com/blog/skills) (Anthropic, official)

Confirms the mechanics we already rely on: a skill is a folder with a `SKILL.md`, loaded on demand,
composable ("Claude automatically identifies which skills are needed and coordinates their use"), and
should be sourced only from trusted authors since a skill can execute code. No new information for us
beyond validating the practice — worth noting the blog names a `skill-creator` tool for scaffolding new
skills, which we haven't used (our three project skills were hand-written).

### 1.3 [K-Dense-AI DrugBank skill](https://www.skillsdirectory.com/skills/k-dense-ai-drugbank-database)

The listing page is a directory entry, not the source. The actual project is much bigger than one
skill: **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)**
— 158–163 skills, 78+ public databases, MIT-licensed, "used by 170,000+ scientists" (unverified claim,
take as marketing). This is the significant find — see Section 2.

**DrugBank specifically:** wraps the full DrugBank XML (~9,591 drugs, 200+ fields/entry) — DDIs,
targets/pathways, ADMET, chemical similarity. Requires a **free DrugBank account** (username/password
via env vars) — that's a registration step only the user can do. Flagged by the directory's own
security scan: "installs packages at runtime which could introduce malicious dependencies." Given
[compute-pipeline-plan.md](compute-pipeline-plan.md) Rule 27 (dedicated conda env, never the working
one), treat this the same way — isolate before trusting.

---

## 2. The Real Find: K-Dense-AI's Broader Library Maps Directly Onto Our Compute Plan

Cross-referencing against [compute-pipeline-plan.md](compute-pipeline-plan.md) Section 4:

| Our hand-specced tool | K-Dense-AI skill that already wraps it | Verdict |
|---|---|---|
| RDKit (cheminformatics) | `skills/rdkit/` | Direct match |
| gnina/smina (docking) | `skills/diffdock/` (DiffDock) | Different tool, same job — evaluate both |
| ADMET-AI | `skills/deepchem/` (DeepChem) | Direct match, different backend |
| OpenMM (MD) | `skills/molecular-dynamics/` (OpenMM + MDAnalysis) | Direct match — **this is the stack we ran M0–M4 benchmarking with by hand** |
| Boltz-2 / Chai-1 / structure prediction | `skills/tamarind/` — AlphaFold, Boltz, Chai, **RFdiffusion, ProteinMPNN**, DiffDock, via one REST API | Covers Branch A *and* Branch B (the biologics branch for the differentiation-track IRF8/C/EBPγ binder work) — but proprietary, API key required |
| AiZynthFinder (synthesizability) | Not found in this library | Still a gap — see Section 4 |
| DepMap essentiality (Phase 0) | `skills/depmap/` | Direct match — API key required |
| scRNA-seq / LSC17 signature analysis (Phase 0) | `skills/scanpy/` | Direct match — this is the actual tool needed to do the van Galen et al. differential-expression work Phase 0 calls for and we have never actually run |
| ChEMBL/PubChem/DrugBank/UniProt lookups | `skills/database-lookup/` — **78 databases unified in one skill** | Strictly better than our 8 separate raw-script skills for breadth, though ours are already verified working and simpler |

**The honest implication:** M0–M1 of compute-pipeline-plan.md (installing WSL2, wiring RDKit/DiffSBDD/
docking/ADMET by hand) is largely re-buildable from `rdkit` + `diffdock` + `deepchem` +
`molecular-dynamics` skills instead of hand-installed conda stacks. Doesn't remove the WSL2 vs. native
Windows decision (RDKit/DiffDock still want Linux-shaped dependency trees), but removes weeks of glue
code if these skills are as functional as claimed. **Unverified — see Section 5.**

---

## 3. Official / Verified MCP Servers Worth Individual Consideration

Found and independently confirmed via GitHub search (not just page-summary):

| Server | What it does | Source | Credential |
|---|---|---|---|
| **Official ChEMBL connector** | 6 tool calls against ChEMBL, Anthropic-maintained | [claude.com tutorial](https://claude.com/resources/tutorials/using-the-chembl-connector-in-claude) | None stated |
| **PubChem MCP** | 30 tools, 110M+ compounds, bioassay + ADMET | [augmented-nature](https://github.com/augmented-nature/pubchem-mcp-server) / [cyanheads](https://github.com/cyanheads/pubchem-mcp-server) | None |
| **ChEMBL MCP (community)** | 22 tools — compound↔target linking, IC50/Ki/EC50 ranking, mechanism/indication lookup | [cyanheads/chembl-mcp-server](https://github.com/cyanheads/chembl-mcp-server) | None |
| **BioContextAI Knowledgebase MCP** | One server, unifies **Open Targets, Reactome, UniProt, KEGG, AlphaFold, Ensembl, HPA, STRINGDb, InterPro, PRIDE, ClinicalTrials.gov, bioRxiv, openFDA** | [biocontext-ai/knowledgebase-mcp](https://github.com/biocontext-ai/knowledgebase-mcp), `pip install biocontext_kb` | None stated |
| **gget-mcp** | Wraps the Pachter Lab's `gget` — Ensembl search, sequence retrieval, BLAST/BLAT/MUSCLE, ARCHS4 expression | [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp), run via `uvx`, no clone needed | None |
| **ToolUniverse** | 211 tools, "all FDA-approved drugs since 1939," Open Targets clinical insights, 68 prebuilt skills incl. precision oncology + pharmacovigilance | [mims-harvard/ToolUniverse](https://github.com/mims-harvard/ToolUniverse) (Zitnik Lab, Harvard) | Varies by sub-tool |

**BioContextAI is the standout.** One install replaces the individual Open Targets / Reactome / UniProt
/ KEGG needs from compute-pipeline-plan.md Section 4 (structure acquisition, pocket/pathway context)
and Phase 0 (target discovery, `aml-lsc-drug-discovery-plan.md` Section 4) in a single, no-credential
server, from a named academic group (not an anonymous repo).

---

## 4. What Nobody Has — Confirmed Gaps

Worth stating plainly since it's easy to assume a mature ecosystem covers everything:

- **AiZynthFinder / retrosynthesis** — not found in any source checked. Still a manual install per
  compute-pipeline-plan.md.
- **FLOWR.root, GenMol, DiffSBDD, TargetDiff** (the specific pocket-conditioned generators named in
  the original brief) — not packaged by K-Dense-AI (which offers DiffDock instead, a different tool
  doing pose prediction, not de novo generation) or any MCP server found. These remain manual installs
  if we want that specific lineage of tool.
- **Covalent docking** (needed for the GPX4 program specifically) — DiffDock is non-covalent by
  design. No skill or MCP found addressing covalent docking. compute-pipeline-plan.md Section 4b's
  covalent lane is still hand-built.
- **DepMap gene essentiality** — only via K-Dense-AI's `skills/depmap/` (API key) or ToolUniverse.
  No free/no-key MCP server found for this specifically.

---

## 5. Trust Before Use — Same Discipline We Just Applied to `drug-discovery-skills`

Yesterday's audit of `huifer/drug-discovery-skills` found 9 of 16 skills silently returning
hard-coded fake data behind names like `_get_mock_patents()` and `_mock_docking()`. **Nothing in this
doc has had that audit run on it.** Before relying on any output from these tools for a scientific
claim in either track's docs:

1. Grep the source for `mock|placeholder|dummy|for now|sample.*demonstration` the way we did before.
2. Run one real query and check the output is plausible and traceable to a real record (a real PMID,
   a real DrugBank ID) — not just structurally valid JSON.
3. For anything requiring an API key (Tamarind, Rowan, DepMap, Modal, Paperclip, BGPT, DrugBank) — an
   API key doesn't imply real data, but a project charging for API access is a weaker fabrication risk
   than a free anonymous repo, since there's a paying customer base that would notice.

**K-Dense-AI's scale claims ("170,000+ scientists," "163 validated skills") are marketing copy from
the project itself, not independently verified.** The repo is real and the file structure it describes
is plausible, but "validated" has not been checked by us. Same rule as everything else in this
project: verify before trusting, especially before it touches a document that argues for a specific
molecule.

---

## 6. Recommendation — Ranked

1. **BioContextAI Knowledgebase MCP** — highest value, no credential, single install, directly fills
   the Open Targets/Reactome/UniProt/KEGG/AlphaFold gap in both `aml-lsc-drug-discovery-plan.md`
   Phase 0/1 and `compute-pipeline-plan.md` Section 4. Audit it first per Section 5, then adopt.
2. **K-Dense-AI `skills/scanpy/` + `skills/depmap/`** — these are the literal missing pieces for
   Phase 0 of the master plan (differential expression on van Galen et al./Beat AML data, DepMap
   essentiality scoring) which has never been executed. Worth standing up before anything else in
   Phase 0, since Phase 0 is the one phase both tracks agree is foundational and unstarted.
3. **Official ChEMBL connector + PubChem MCP** — low-risk upgrade over our existing raw-script
   `compound-profile` skill; richer tool surface, Anthropic/well-known maintained.
4. **K-Dense-AI `skills/rdkit/`, `diffdock/`, `deepchem/`, `molecular-dynamics/`** — evaluate against
   compute-pipeline-plan.md's M0–M1 before committing; may shortcut the WSL2 build-out, may not (still
   need to check whether they assume WSL2/Linux themselves).
5. **DrugBank skill** — useful specifically for DDI-checking the growing multi-drug regimens in both
   tracks (GPX4i + FSP1i + venetoclax + azacitidine; menin inhibitor + C/EBPγ blocker + venetoclax +
   azacitidine) — a real gap neither track has addressed. Requires the user to register a free
   DrugBank account first; I can't do that step.
6. **Tamarind** (AlphaFold/Boltz/Chai/RFdiffusion/ProteinMPNN/DiffDock, one API) — the single most
   relevant item if the differentiation track's IRF8–C/EBPγ or C/EBPα:AP-1 interface work goes
   biologic (binder design), per compute-pipeline-plan.md's Branch B. Proprietary, API key required.
   Hold until a modality decision is made on that track.

**Not recommended:** Benchling, BioRender, 10x Genomics, Databricks/Snowflake connectors — built for
wet-lab/institutional workflows this project doesn't have.

## 6a. Installed

`.mcp.json` (project root) now configures all four no-credential servers verified in Section 3:
`biocontext-kb`, `gget-mcp`, `chembl-mcp-server` (v0.2.4, pinned), `pubchem-mcp-server` (v0.6.1,
pinned). All four confirmed to exist and resolve real dependencies before wiring in — uvx-based
servers pulled real matching packages (openmm, biopython, gget), npm packages confirmed on the
registry. **Requires a session restart to activate** — Claude Code loads project MCP servers at
startup, not mid-session.

Pointers added to `target-profile`, `compound-profile`, `target-validation`, and `drug-simulation`
skills, and to `CLAUDE.md`, noting when to prefer the MCP tool over the existing raw-script skill.

**Not installed:** official ChEMBL connector (that's an account-level OAuth connector via claude.ai
settings, not something addable from a repo config — same category as the Gmail/Calendar/Drive
connectors already noted as unavailable from this session); ToolUniverse (heavier, no simple one-line
run command found, deprioritized for compactness); K-Dense-AI skills library and DrugBank/Tamarind
(credential- or account-gated, need the user's own registration first).

## Related Docs

- [compute-pipeline-plan.md](compute-pipeline-plan.md) — the hand-built stack this partially replaces
- [aml-lsc-drug-discovery-plan.md](aml-lsc-drug-discovery-plan.md) — Phase 0 is where scanpy/DepMap slot in
