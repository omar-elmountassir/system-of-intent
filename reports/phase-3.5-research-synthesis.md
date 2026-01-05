# Phase 3.5 Research Synthesis Report

**Date**: 2026-01-05
**Status**: Complete

---

## 1. Repository Structure Analysis

### 7 SSOT Violations Found

1. **Golden Rules** duplicated in 4+ files (SYSTEM_OF_INTENT.md, AGENTS.md, CLAUDE.md, plan files)
2. **Workforce Registry** duplicated (SYSTEM_OF_INTENT.md + AGENTS.md)
3. **Technical Environment** info duplicated across files
4. **OODA Loop** documented in 2 files
5. **Repository Identity** (URL, paths) in 3 files
6. **Roadmap Status** duplicated
7. **Agent Orchestration Rules** scattered across multiple files

### Current Structure Issues

- Files mixed at root level (philosophy, config, logs, docs)
- No clear navigation structure (Knowledge Graph missing)
- Agent-facing files in mixed languages (some French)
- No automation for self-healing configurations

### Proposed Directory Structure

```
/docs/          # PHILOSOPHY.md, ARCHITECTURE.md, RULES.md
/registry/      # AGENTS.md, WORKFORCE.md, ORCHESTRATOR.md
/config/        # bashrc.template, settings.local.json, install.sh
/scripts/       # setup.sh, sync-config.sh
/logs/          # decisions/, incidents/, sessions/
/reports/       # Generated analysis
/.memory/       # state/, templates/, archive/
/.admin/        # prompts/, scripts/
/.claude/       # settings.json, hooks/
```

---

## 2. Claude Code CLI Evolution (Since Jan 2025)

### New Features Discovered

| Feature | Description |
|---------|-------------|
| **LSP Integration** | goToDefinition, findReferences, hover, documentSymbol |
| **Hooks System** | 10 events (PreToolUse, PostToolUse, UserPromptSubmit, SessionStart, etc.) |
| **Output Styles** | Custom system prompts via markdown files |
| **Background Agents** | `run_in_background` parameter for parallel execution |
| **MCP Server Patterns** | `.mcp.json` at project root with wildcard permissions |
| **Claude Agent SDK** | Building custom agents programmatically |
| **Non-Interactive Mode** | `claude -p "prompt"` for scripting |
| **Task Resumption** | Resume agents via agent IDs |

### Key CLI Improvements

- Task tool with specialized sub-agent types
- LSP tool for code intelligence
- Enhanced Bash tool with sandboxing
- WebFetch and WebSearch tools
- Background task management

---

## 3. Hooks Research Findings

### Key Discovery

**Output Styles do NOT redirect output to files** - they only modify the system prompt. Custom hooks are required to prevent chat-based outputs.

### Available Hook Events (10 Total)

| Event | Trigger | Use Case |
|-------|---------|----------|
| `PreToolUse` | Before tool executes | Block/approve/modify tool calls |
| `PostToolUse` | After tool completes | Validate results, trigger actions |
| `UserPromptSubmit` | User submits prompt | Inject context, validate prompts |
| `SessionStart` | Session begins | Load context, setup environment |
| `SessionEnd` | Session terminates | Cleanup, logging |
| `Stop` | Main agent finishes | Block stoppage |
| `SubagentStop` | Subagent finishes | Control subagent completion |
| `PermissionRequest` | Permission dialog | Auto-allow/deny |
| `Notification` | Notifications sent | Custom alerts |
| `PreCompact` | Before compaction | Backup state |

### Configuration Locations (Priority Order)

1. `.claude/settings.local.json` - Local (NOT committed, highest priority)
2. `.claude/settings.json` - Project-wide
3. `~/.claude/settings.json` - User-wide

### Solution for Output Redirection

Use `UserPromptSubmit` hook to inject context telling Claude to save reports to files:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/output-redirector.py"
          }
        ]
      }
    ]
  }
}
```

---

## 4. Recommendations

### Immediate Actions

1. Fix SSOT violations by consolidating to single source files
2. Implement directory restructure
3. Create hooks infrastructure for output control
4. Translate all French files to English

### Architecture Priorities

1. **docs/PHILOSOPHY.md** - Single source for Golden Rules
2. **docs/ARCHITECTURE.md** - Technical specs
3. **registry/AGENTS.md** - Agent roles and protocols
4. **scripts/install.sh** - Symlink automation

---

## Sources

- Repository exploration (Phase E Agent 1)
- Claude Code CLI research (Phase E Agent 2)
- Hooks research (Phase F claude-code-guide)
- Mind's Nouvelle_initiative.md proposal
