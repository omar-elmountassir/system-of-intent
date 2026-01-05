# Roadmap: System of Intent

## Phase 1: Foundation & Migration (The Cleanup)

- [ ] **Finalize Bash Transition**: Confirm strictly NO dependency on Zsh remains.
- [x] **Archive "The Ruins"**: Backup old `.zshrc` and Zsh configs into an `archive/` folder, then remove them from root.
- [ ] **Port Aliases**: Extract useful aliases/functions from old Zsh config and port them to `.bashrc` (or `~/.bash_aliases`).
- [x] **Shortcuts**: Create `goto-soi` alias in `.bashrc` to jump to this repository immediately.
- [ ] **Linting & Validation**: Setup shellcheck or similar to validate .bashrc changes automatically to avoid blind errors.

## Phase 2: Connectivity (The Bridge)

- [x] **GitHub Sync**: Initialize remote 'origin', authenticate via `gh`, and push the initial System of Intent.
- [x] **Repo Sharing**: Share the repository URL with the "Mind" (Gemini Web Interface) to close the loop.

## Phase 3: The Workforce (Agents)

- [ ] **Claude Optimization**: Tune settings (auto-compact, permissions) in `settings.json` or CLI config.
- [x] **Codex Verification**: Debug `codex` CLI (it had issues locating the command previously) and verify usability.
- [x] **Role Definition**: Update `AGENTS.md` to explicitly define what Gemini CLI and Codex are used for vs. Claude.
- [ ] **Handover Protocol**: Document how to pass context from one agent to another.

## Phase 3.5: Consolidation & Architecture

### Rule Documentation

- [x] **Add Golden Rules 5-7**: ROADMAP First, Sub-Agent Context, Flag-Log-Fix
- [x] **Create Incident Log**: `logs/incidents/README.md` with tracking system
- [x] **Establish Orchestrator Protocol**: Update CLAUDE.md with Lead Orchestrator role

### Research Tasks

- [x] **Explore Repository Structure**: Map all files, identify SSOT violations, note duplications
- [x] **Research Claude Code CLI Evolution**: What's new since Jan 2025?
- [x] **Research Project Structure Best Practices**: How modern Claude Code projects organize
- [x] **Research MCP Server Patterns**: Conventions and patterns

### Documentation Tasks

- [ ] **Complete Session Persistence Audit**: Backlog from Plan A
- [ ] **Convert Files to English**: All agent-facing files must be English
- [ ] **Create Standardized Headers**: Knowledge Graph with navigation links

### Architecture Tasks

- [ ] **Design Directory Structure**: Propose /docs, /config, /scripts, /registry, /logs structure
- [ ] **Create Migration Plan**: Step-by-step restructure plan
- [ ] **Implement Directory Restructure**: Execute the migration
- [ ] **Create Symlink Automation**: install.sh for dotfiles-as-code

### Resource Organization (Current)

- [ ] **Create resources/ directory**: Centralize reusable templates and guides
- [ ] **Create archives/ directory**: Historical preservation per Golden Rule #8
- [ ] **Document Golden Rule #8**: Archive Over Delete principle
- [ ] **Document Documentation Theater**: New anti-pattern identification
- [ ] **Migrate resources**: Move AGENT_CONTEXT_TEMPLATE.md, COMPACT_TEMPLATE.md
- [ ] **Archive SESSION_LOG_TEMPLATE.md**: Example of Documentation Theater

## Phase 4: Operations & Architecture

- [ ] **Everything-as-Code**: Create templates for new generic files/scripts to ensure consistency.
- [ ] **Workflow Documentation**: Document common collaboration scenarios (e.g., "How to debug a script using the Trinity").

## Future: Automation & Hooks

- [ ] **Fork/Clone Hook Repositories**:
  - https://github.com/disler/claude-code-hooks-mastery
  - https://github.com/disler/claude-code-hooks-multi-agent-observability
  - https://github.com/disler/claude-code-damage-control
- [ ] **Create Custom Hooks**: Prevent agent mistakes via automated enforcement
- [ ] **Self-Testing Framework**: Use `claude -p` for agent self-verification
- [ ] **Output Redirection Hook**: Implement UserPromptSubmit hook to prevent chat-based outputs
- [ ] **Session Init Hook**: Implement SessionStart hook to auto-load context
- [ ] **Sub-Agent Registry Automation**: Auto-remind orchestrator of available agents
