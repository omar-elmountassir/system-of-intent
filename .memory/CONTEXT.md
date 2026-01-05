# System of Intent - Persistent Memory

> **PURPOSE**: This file ensures NO DATA LOSS between sessions. Agents MUST read this after any /compact or context reset.

---

## Identity

| Key            | Value                                                   |
| -------------- | ------------------------------------------------------- |
| **Repository** | `https://github.com/omar-elmountassir/system-of-intent` |
| **Local Path** | `/home/omar/system-of-intent`                           |
| **Quick Nav**  | `goto-soi` or `soi` (aliases in ~/.bashrc)              |
| **Owner**      | Omar (The Mind)                                         |

---

## The 4 Golden Rules [MANDATORY]

### 1. Persistence First

**Nothing remains in chat. Every decision, status change, or new information MUST be recorded in the repository files immediately.**

### 2. Zero Silent Failures

**Any warning, error, or unexpected output (stderr) must be REPORTED to the Mind immediately. Do not assume 'it's fine'. Let the Mind decide.**

### 3. Halt on Uncertainty

**If a command fails, returns unexpected data, or displays a warning, or if functionality is ambiguous, STOP immediately. Do not guess the cause. Do not assume it is benign. Report the anomaly to the Mind and ask for clarification.**

### 4. Mandatory Initialization

- ALWAYS START BY READING: [SYSTEM_OF_INTENT.md](../SYSTEM_OF_INTENT.md) + [ROADMAP.md](../ROADMAP.md)
- ALL WORK MUST BE ADDED TO ROADMAP FIRST
- UPDATE ROADMAP ON EVERY PROGRESS

---

## Anti-Pattern: "Heuristique de la Facilité"

**FORBIDDEN BEHAVIOR**: Filling unknowns with probabilities instead of stopping.

| Hypothesis   | Description                               | Correct Action |
| ------------ | ----------------------------------------- | -------------- |
| "C'est rien" | Assuming errors are benign                | REPORT to Mind |
| Context      | Assuming environment without verification | VERIFY first   |
| Causality    | Deducing without formal proof             | TEST and PROVE |

**RULE**: Know or Ask. NEVER Guess.

---

## Anti-Pattern: "Documentation Theater"

**DEFINITION**: Creating documentation artifacts that appear structured but provide no actual value.

**SYMPTOMS**:
1. Template not followed in practice
2. Content is self-evident (anyone would write it naturally)
3. Creates SSOT violation (template vs reality diverge)
4. Maintenance burden exceeds value

**EXAMPLE**: SESSION_LOG_TEMPLATE.md (archived 2026-01-05)
- Template said "Changes Made", actual log used "Infrastructure Changes"
- Template structure was obvious - no checklist value
- Template and log diverged immediately

**RULE**: If a template provides no more value than the artifact itself, it is theater.

**ACTION**: Archive as example of anti-pattern (per Golden Rule #8), don't replicate.

---

## Anti-Pattern: "Repetition Burden"

**DEFINITION**: When the Mind must repeatedly remind agents of tasks that should be automatic.

**SYMPTOMS**:
1. Mind asks "did you update SESSION_LOG?"
2. Agent forgets mandatory session-end tasks
3. Same instructions given across multiple sessions
4. Defeats purpose of documented protocols

**ROOT CAUSE**: No enforcement mechanism for session-end responsibilities.

**RULE**: If an agent task is mandatory at session end, it MUST be:
1. Documented in a checklist
2. Enforced via hooks (when possible)
3. Self-triggered, not Mind-triggered

**SOLUTION**: Session End Protocol in CLAUDE.md (mandatory checklist).

---

## Workforce Registry

| Agent        | Status   | Version | Role                                                      |
| ------------ | -------- | ------- | --------------------------------------------------------- |
| Claude Code  | Active   | v2.0.76 | Primary execution agent for system config, code, file ops |
| Gemini CLI   | Verified | v0.22.5 | Interactive AI, MCP server management, extensions         |
| OpenAI Codex | Verified | v0.77.0 | Code generation, review, sandboxed execution              |

---

## Behavioral Paradigm: OODA Loop

Agents operate on a strict **Observe-Orient-Decide-Act** loop:

- Cannot skip from "Observe" to "Act" without Mind validation when uncertainty exists
- Must HALT at "Orient" phase if anomaly detected
- Mind approval required before proceeding past uncertainty

---

## Technical Environment

### Shell Context

- **System Default**: Zsh (`/usr/bin/zsh`) - prompt shows `pop-os%`
- **VS Code Terminal**: Bash (configured override)
- **Bash Enhancements**: ble.sh + Starship prompt

### Critical Technical Facts

1. `source ~/.bashrc` FAILS when run from Zsh (`shopt` is bash-only builtin)
2. Non-interactive bash (`bash -c`) does NOT load .bashrc
3. Use `bash -i -c "command"` to test bash aliases
4. ble.sh requires bash context for initialization

### Archived Configurations

- **Legacy Zsh**: `~/legacy_zsh_archive/`
  - Contents: .zshrc, .zshenv, .zsh_history, .fzf.zsh, .zcompdump, .zshrc.backup.\*

### Navigation Shortcuts (in ~/.bashrc)

```bash
alias goto-soi='cd ~/system-of-intent && echo "Welcome to the System of Intent"'
alias soi='goto-soi'
```

---

## Tooling

| Tool              | Status | Purpose                |
| ----------------- | ------ | ---------------------- |
| GitHub CLI (`gh`) | Ready  | Repository management  |
| Claude CLI        | Ready  | Primary agent          |
| Gemini CLI        | Ready  | Secondary agent        |
| Codex CLI         | Ready  | Code review/generation |

---

## Current Roadmap Status

### Phase 1: Foundation & Migration

- [x] Shortcuts (goto-soi, soi)
- [x] Archive "The Ruins" (Zsh configs)
- [ ] Finalize Bash Transition
- [ ] Port Aliases
- [ ] Linting & Validation

### Phase 2: Connectivity

- [x] GitHub Sync
- [ ] Repo Sharing (URL shared, awaiting Mind confirmation)

### Phase 3: The Workforce

- [x] Codex Verification
- [x] Role Definition
- [ ] Claude Optimization
- [ ] Handover Protocol

### Phase 3.5: Resource Organization

- [x] Create resources/ directory
- [x] Create archives/ directory
- [x] Document Golden Rule #8 (Archive Over Delete)
- [x] Document Documentation Theater anti-pattern
- [x] Migrate AGENT_CONTEXT_TEMPLATE.md to resources/
- [x] Migrate COMPACT_TEMPLATE.md to resources/
- [x] Archive SESSION_LOG_TEMPLATE.md (Documentation Theater example)

### Phase 4: Operations & Architecture

- [ ] Everything-as-Code templates
- [ ] Workflow Documentation

---

## Session Continuity

**Last Updated**: 2026-01-05

**Pending Tasks** (from previous session):

1. Complete persistence audit - update logs/decisions/README.md
2. Update SYSTEM_OF_INTENT.md with missing sections
3. Update AGENTS.md with OODA paradigm
4. Mark Repo Sharing complete in ROADMAP.md

---

## Instructions for Agents

After any `/compact` or context reset:

1. READ this file first
2. READ [SYSTEM_OF_INTENT.md](../SYSTEM_OF_INTENT.md)
3. READ [ROADMAP.md](../ROADMAP.md)
4. Check `SESSION_LOG.md` for recent activity
5. Resume pending tasks

**REMEMBER**: The Mind sees everything. Systematically create your Report(s) in `reports/`. Don't assume.
