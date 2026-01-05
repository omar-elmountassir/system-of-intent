# Roadmap: System of Intent

## Phase 1: Foundation & Migration (The Cleanup)

- [ ] **Finalize Bash Transition**: Confirm strictly NO dependency on Zsh remains.
- [ ] **Archive "The Ruins"**: Backup old `.zshrc` and Zsh configs into an `archive/` folder, then remove them from root.
- [ ] **Port Aliases**: Extract useful aliases/functions from old Zsh config and port them to `.bashrc` (or `~/.bash_aliases`).
- [ ] **Shortcuts**: Create `goto-soi` alias in `.bashrc` to jump to this repository immediately.

## Phase 2: Connectivity (The Bridge)

- [ ] **GitHub Sync**: Initialize remote 'origin', authenticate via `gh`, and push the initial System of Intent.
- [ ] **Repo Sharing**: Share the repository URL with the "Mind" (Gemini Web Interface) to close the loop.

## Phase 3: The Workforce (Agents)

- [ ] **Claude Optimization**: Tune settings (auto-compact, permissions) in `settings.json` or CLI config.
- [ ] **Codex Verification**: Debug `codex` CLI (it had issues locating the command previously) and verify usability.
- [ ] **Role Definition**: Update `AGENTS.md` to explicitly define what Gemini CLI and Codex are used for vs. Claude.
- [ ] **Handover Protocol**: Document how to pass context from one agent to another.

## Phase 4: Operations & Architecture

- [ ] **Everything-as-Code**: Create templates for new generic files/scripts to ensure consistency.
- [ ] **Workflow Documentation**: Document common collaboration scenarios (e.g., "How to debug a script using the Trinity").
