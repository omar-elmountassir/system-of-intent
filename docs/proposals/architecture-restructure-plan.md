# Architecture Restructure Plan

**Date**: 2026-01-05
**Status**: Proposal - Pending Mind Approval
**Phase**: 3.5 Consolidation & Architecture

---

## Executive Summary

This proposal addresses the 7 SSOT violations and structural issues identified during Phase 3.5 research. It recommends a modular directory structure that separates concerns, enables navigation (Knowledge Graph), and prepares for automation (self-healing configurations).

---

## 1. Current Problems

### 7 SSOT Violations Identified

1. **Golden Rules** - Duplicated in SYSTEM_OF_INTENT.md, AGENTS.md, CLAUDE.md, plan files
2. **Workforce Registry** - Duplicated in SYSTEM_OF_INTENT.md and AGENTS.md
3. **Technical Environment** - Info scattered across multiple files
4. **OODA Loop** - Documented in both SYSTEM_OF_INTENT.md and AGENTS.md
5. **Repository Identity** - URL and paths repeated in 3+ files
6. **Roadmap Status** - Duplicated references
7. **Agent Orchestration Rules** - Scattered across CLAUDE.md, AGENTS.md, plan files

### Structural Issues

- Files mixed at root level (philosophy, config, logs, docs)
- No clear navigation structure (Knowledge Graph missing)
- Some agent-facing files in French (now translated)
- No automation for configuration synchronization

---

## 2. Proposed Directory Structure

```
system-of-intent/
├── SYSTEM_OF_INTENT.md    # Entry point - links to everything (SSOT index)
├── ROADMAP.md             # Project roadmap (keep at root for visibility)
│
├── docs/                  # All documentation
│   ├── PHILOSOPHY.md      # Golden Rules (SINGLE SOURCE)
│   ├── ARCHITECTURE.md    # Technical specifications
│   └── proposals/         # Architecture proposals (already exists)
│       ├── phase-3.5-architecture-initiative.md
│       └── architecture-restructure-plan.md
│
├── registry/              # Agent definitions and protocols
│   ├── AGENTS.md          # Agent roles (moved from root)
│   ├── WORKFORCE.md       # Workforce status (extracted from SYSTEM_OF_INTENT)
│   └── ORCHESTRATOR.md    # Claude Code specific protocols (extracted from CLAUDE.md)
│
├── config/                # Configuration files
│   ├── bashrc.template    # Bash configuration template
│   ├── install.sh         # Symlink automation script
│   └── README.md          # Config documentation
│
├── scripts/               # Automation scripts
│   ├── setup.sh           # Initial setup
│   └── sync-config.sh     # Configuration synchronization
│
├── logs/                  # All logs (already exists)
│   ├── decisions/         # Decision logs
│   ├── incidents/         # Incident tracking
│   └── sessions/          # Session logs
│
├── reports/               # Generated reports (already exists)
│   └── phase-3.5-research-synthesis.md
│
├── .memory/               # Agent memory and state
│   ├── CONTEXT.md         # Current context
│   ├── SESSION_LOG.md     # Session tracking
│   └── templates/         # Templates
│       └── AGENT_CONTEXT_TEMPLATE.md
│
├── .admin/                # Administrative files
│   └── prompts/           # Mind's prompts (archive)
│
└── .claude/               # Claude Code configuration
    ├── settings.json      # Project settings with hooks
    ├── settings.local.json # Local overrides (not committed)
    └── hooks/             # Hook scripts
        ├── output-redirector.py
        └── session-init.sh
```

---

## 3. SSOT Resolution Plan

### Golden Rules → docs/PHILOSOPHY.md
- Move all Golden Rules to single file
- Other files link to it (never duplicate content)
- Format: Full rule text with examples

### Workforce → registry/WORKFORCE.md
- Extract from SYSTEM_OF_INTENT.md
- Single source for agent status and capabilities
- SYSTEM_OF_INTENT.md links to it

### Agent Orchestration → registry/ORCHESTRATOR.md
- Extract from CLAUDE.md
- Contains: Wave limits, pre-launch checklist, workflow
- CLAUDE.md becomes minimal (just @references)

### OODA Loop → docs/ARCHITECTURE.md
- Single definition in Architecture doc
- AGENTS.md links to it

### Repository Identity → SYSTEM_OF_INTENT.md
- Keep in entry point only
- Other files use relative paths

---

## 4. Knowledge Graph Implementation

### Header Template (for all documentation files)

```markdown
# [File Title]

> **Part of**: [System of Intent](../SYSTEM_OF_INTENT.md)
> **See also**: [Related File 1](path), [Related File 2](path)
> **Last updated**: YYYY-MM-DD

---
```

### Footer Template

```markdown
---

## Navigation

- **Parent**: [SYSTEM_OF_INTENT.md](../SYSTEM_OF_INTENT.md)
- **Related**: [File1](path), [File2](path)
- **Next**: [Suggested next reading](path)
```

---

## 5. Migration Checklist

### Phase 1: Create New Structure
- [ ] Create `/docs/PHILOSOPHY.md` with Golden Rules
- [ ] Create `/docs/ARCHITECTURE.md` with technical specs
- [ ] Create `/registry/` directory
- [ ] Create `/config/` directory
- [ ] Create `/scripts/` directory

### Phase 2: Move and Extract Content
- [ ] Extract Golden Rules from SYSTEM_OF_INTENT.md → docs/PHILOSOPHY.md
- [ ] Extract Workforce from SYSTEM_OF_INTENT.md → registry/WORKFORCE.md
- [ ] Move AGENTS.md → registry/AGENTS.md
- [ ] Extract Orchestrator protocols from CLAUDE.md → registry/ORCHESTRATOR.md

### Phase 3: Update References
- [ ] Update SYSTEM_OF_INTENT.md with @links to new locations
- [ ] Update CLAUDE.md to reference registry/ORCHESTRATOR.md
- [ ] Update all files with Knowledge Graph headers/footers
- [ ] Verify no broken links

### Phase 4: Automation Setup
- [ ] Create config/install.sh for symlink automation
- [ ] Create scripts/setup.sh for initial setup
- [ ] Test symlink creation for .bashrc

---

## 6. Symlink Automation (install.sh)

```bash
#!/bin/bash
# install.sh - System of Intent configuration installer
# Creates symlinks from repo to system locations

SOI_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "Installing System of Intent configurations..."

# Backup existing configs
if [ -f ~/.bashrc ] && [ ! -L ~/.bashrc ]; then
    mv ~/.bashrc ~/.bashrc.backup.$(date +%Y%m%d)
    echo "Backed up existing .bashrc"
fi

# Create symlinks
ln -sf "$SOI_ROOT/config/bashrc.template" ~/.bashrc
echo "Linked .bashrc"

# Add navigation alias
if ! grep -q "goto-soi" ~/.bashrc 2>/dev/null; then
    echo "alias goto-soi='cd $SOI_ROOT'" >> "$SOI_ROOT/config/bashrc.template"
    echo "alias soi='cd $SOI_ROOT'" >> "$SOI_ROOT/config/bashrc.template"
fi

echo "Installation complete!"
echo "Run 'source ~/.bashrc' to reload configuration"
```

---

## 7. Success Criteria

- [ ] Zero SSOT violations (each piece of information in exactly one place)
- [ ] All documentation files have Knowledge Graph headers/footers
- [ ] Navigation from any file to related files possible
- [ ] Symlink automation tested and working
- [ ] All agent-facing files in English

---

## 8. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Broken links during migration | Run link checker after each phase |
| Lost content during extraction | Git history preserves all changes |
| Confusion during transition | Document migration in ROADMAP.md |
| Hooks affecting existing workflows | Test hooks in isolated session first |

---

## Next Steps

1. **Mind Approval**: Present this proposal for review
2. **Phase G Planning**: Create detailed migration plan
3. **Execution**: Implement via sub-agents (max 2 per wave)
4. **Validation**: Verify SSOT compliance and link integrity
