# MCP Landscape — What We Have, What We Lack, What's Out There

Status: research + 1 new install. Extends
[skills-and-mcp-integration-plan.md](../skills-and-mcp-integration-plan.md) (the first 4 servers).

## Part 1 — Confirmed Gaps (nothing found fills these)

Searched specifically for each; none exist as an MCP server or credential-free skill anywhere checked.

| Gap | Why it matters | Status |
|---|---|---|
| **Retrosynthesis** (AiZynthFinder/IBM RXN-class) | compute-pipeline-plan.md's synthesizability gate has no tool | No MCP found. AiZynthFinder itself is still a manual pip install |
| **Covalent docking** | Track 1's entire GPX4 program is covalent | No MCP or skill found anywhere. Manual (AutoDock-Vina covalent mode / from-bonded-state MD) is still the only path |
| **De novo pocket-conditioned generation** (FLOWR.root/GenMol/DiffSBDD) | compute-pipeline-plan.md Section 4 names these specifically | Not packaged as MCP. NVIDIA BioNeMo NIMs cover GenMol/DiffDock/RFdiffusion/ProteinMPNN but require Baseten (paid) or self-hosted NIM (GPU beyond our Titan Xp) — see Part 2 |
| **Structure prediction / co-folding** (Boltz-2/Chai-1) | Track 2's designed C/EBPγ-selective miniprotein has no crystal structure to dock against — this will bite as soon as that design work starts | Boltz-2 has **no MCP wrapper**. It is MIT-licensed and free to run locally (`pip install boltz`) — still the recommended path, just not an MCP. Rowan (rowansci.com) offers it as a paid cloud tool |
| **DepMap essentiality (standalone)** | Both tracks lean on this for target safety (C/EBPγ knockout was clean; IRF8 knockout was not) | Only found bundled inside ToolUniverse (heavier, not installed) — no simple standalone MCP |
| **DDI checking** (DrugBank) | Both tracks are now 4-drug regimens | Real MCP servers exist (Part 2) but every path needs a DrugBank account — cannot be set up without the user |

## Part 2 — Newly Found, Verified

Same discipline as last time: existence confirmed via direct search hits, then actually launched
before trusting.

| Server | Fills | Credential | Verified | Action |
|---|---|---|---|---|
| **`patent-mcp-server`** (riemannzeta, PyPI) | Patent/FTO search — the gap left by excluding `huifer/drug-discovery-skills`'s fake `patent-search` skill | **None** for core patent/trademark search + PDF download. Optional free USPTO account (ID.me verification) unlocks ODP/PTAB tools | **Installed and launched successfully** — but only after pinning `mcp<2`; the published package has an unpinned `mcp` dependency that breaks against the current `mcp` 2.x (`FastMCP` renamed to `MCPServer`). Real bug, not ours | **Added to `.mcp.json`** |
| **`openpharma-org/fda-mcp`** | Pharmacovigilance — openFDA + Orange Book + Purple Book (adverse events, recalls, labels) | None (openFDA is public) | Confirmed no-auth via README, but **not published to PyPI or npm** — only installable by cloning and running `node build/index.js` locally | Documented, not installed — clone+build is a bigger step than the one-liners used elsewhere; revisit if pharmacovigilance data becomes load-bearing |
| **`openpharma-org/drugbank-mcp-server`** (unofficial) | DDI checking | **Still needs a DrugBank account** — must download the DrugBank XML yourself and place it locally; the repo hosts no data | Confirmed via README | Not installed — needs the user's registration first, same conclusion as before |
| **Official DrugBank MCP** (go.drugbank.com/mcp) | DDI checking | **Paid** DrugBank OS account with MCP access | Confirmed real product page | Not installed |
| **NVIDIA BioNeMo NIMs** (GenMol, DiffDock, RFdiffusion, ProteinMPNN, Boltz-2, OpenFold3) | The single biggest capability gap — de novo generation, docking, PPI binder design, and structure prediction, all in one family | **Paid** (Baseten hosting, usage-billed) or self-hosted (needs a real GPU — Titan Xp doesn't qualify per compute-pipeline-plan.md) | Real, actively developed, matches the original brief's FLOWR.root/GenMol comparison closely | Not installed — flagging as the one item worth paying for if/when Track 2's biologic-interface design work actually starts |
| **`Augmented-Nature/ChEMBL-MCP-Server`** | ChEMBL (alternate implementation) | None | Real | Redundant with the already-installed `chembl-mcp-server` — skip |

## Part 3 — Full Verification: Launch, Don't Just Resolve

Every server in `.mcp.json` was actually started and watched for a clean stdio launch, not just
checked for package existence — the same standard `drug-simulation`'s own rules demand of chemistry
tooling.

| Server | Launch result |
|---|---|
| `biocontext-kb` | Clean — 126 packages, only harmless deprecation warnings |
| `gget-mcp` | Clean — 133 packages, no errors |
| `patent-mcp-server` | **Crashed** on first try — published package has an unpinned `mcp` dependency that resolves to `mcp` 2.x, which renamed `FastMCP` to `MCPServer`. Fixed by pinning `mcp<2`. Clean after that |
| `chembl-mcp-server` | **Broken.** `npm view` shows `engines: {node: '>=24.0.0'}`. This machine's only Node is **10.15.3**. `npx -y` itself errors before the package's own check would fire — the installed npx (6.4.1) is too old to parse the flag correctly |
| `pubchem-mcp-server` | **Broken**, same cause — same `engines: {node: '>=24.0.0'}` |

**Attempted fix:** `nvm install 24` without touching the global Node default (nvm-windows would
otherwise symlink `C:\Program Files\nodejs` to the new version, affecting everything else on the
machine that calls plain `node`). nvm-windows needs Administrator rights to write that folder even
just to *install* a version — the resulting UAC elevation prompt cannot be answered from this
non-interactive session and hangs indefinitely. **Not fixable without the user present.**

Both broken configs are preserved in `.mcp.json` under an inert `_disabled_needs_node_24` key —
correct and ready, just not loaded. Fix path: run `nvm install 24` as Administrator (or install Node
24 directly, e.g. from nodejs.org), then move that block back into `mcpServers`. No code changes
needed after that.

## Verdict

**Nothing found closes the retrosynthesis or covalent-docking gaps.** Those stay hand-built per
compute-pipeline-plan.md regardless of how much of the MCP ecosystem we adopt.

**Of the 5 servers touched this round, 3 actually work: `biocontext-kb`, `gget-mcp`,
`patent-mcp-server`** (the latter only after fixing a real bug in the published package). **2 are
correctly configured but cannot run on this machine** without a Node upgrade only the user can grant.

**The one gap worth planning to pay for** is NVIDIA BioNeMo, if Track 2 needs de novo binder design.

## Related Docs

- [skills-and-mcp-integration-plan.md](../skills-and-mcp-integration-plan.md) — the first 4 installed servers
- [compute-pipeline-plan.md](../compute-pipeline-plan.md) — the hand-built stack these fill parts of
