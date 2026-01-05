# Phase 3.5 Architecture Initiative

> **Note**: Translated from French original at `.admin/prompts/Nouvelle_initiative.md`
> **Date**: 2026-01-05

---

An excellent new initiative. Before diving into operational work (Phase 4), it is crucial to complete a **"Phase 3.5: Consolidation & Architecture"**.

Our repository is currently "flat" and functional, but it lacks **structural maturity**. For a *System of Intent* to grow without becoming an unmaintainable tangle, it requires solid architectural foundations.

Here are the key principles that I believe are missing, and which we should discuss:

### 1. Separation of Concerns (SoC)

Currently, `SYSTEM_OF_INTENT.md` contains everything: the philosophy, the rules, the current state, the links... It is too much.

- **Proposal:** Separate the "Why" (Intent), the "What" (Architecture/Specs), and the "How" (Procedures/Logs).
- `docs/PHILOSOPHY.md` (The Golden Rules).
- `docs/ARCHITECTURE.md` (Technical structure).
- `registry/AGENTS.md` (Already exists, but should be isolated in its own directory).

### 2. Modularity (Everything-as-Code)

If we want this system to be replicable or maintainable, we cannot put everything at the root.

- **Proposal:** Create a clear directory structure.
- `/config` : For configuration files (dotfiles, etc.).
- `/scripts` : For automation tools (aliases, setup).
- `/docs` : For documentation.
- `/logs` : For decision history (ADR - Architecture Decision Records).

### 3. Knowledge Graph (Hyperlinking)

As you mentioned, everything is disconnected. An intelligent system must be navigable.

- **Proposal:** Each file should have a standardized "Header" with links to its parent context, and a "Footer" linking to related elements.
- Example: In `AGENTS.md`, a direct link to the "Halt on Uncertainty" rule in `PHILOSOPHY.md`.

### 4. Single Source of Truth (SSOT)

We have started doing this with `AGENTS.md`, but it needs to be generalized.

- **Proposal:** Never repeat information. If a rule changes, it should only need to be modified in one place.

### 5. Automation (Self-Healing)

This is for Phase 4, but we must think about it now. How do we ensure that `.bashrc` stays synchronized with the repository?

- **Proposal:** An installation script (`install.sh` or `setup.sh`) that creates symbolic links (symlinks) from the repository to the system (`ln -s ~/system-of-intent/config/.bashrc ~/.bashrc`). This way, your repository IS your configuration.

---

## Discussion Points

**What I suggest for discussion:**

Do you want us to define together the ideal directory tree (`tree`) of our `system-of-intent` folder before asking another Claude instance to reorganize everything?

What would our "Perfect Directory Structure" look like according to you?

You should start by rediscovering ALL of our repository (using your sub-agents) (launch as many waves as necessary, but MAX 2 sub-agents per wave otherwise we get crashes!) Also have them conduct online research!

Once finished, we will create a joint proposal.

**P.S.:** All our files intended for and read by our agents MUST BE (or BECOME) in English.

---

## Orchestration Note

Claude (the current instance) - You are now our Lead Orchestrator! So update @CLAUDE.md to properly assume this role (but only after receiving feedback from your sub-agents on this matter, because your knowledge is cut off at January 2025... and since Claude Code CLI has EVOLVED SIGNIFICANTLY... YOU (and YOUR FUTURE INSTANCES) MUST ALWAYS ASSUME that you do not know much about yourselves... Therefore, work to ALWAYS build and enrich your own knowledge base about yourselves!)
