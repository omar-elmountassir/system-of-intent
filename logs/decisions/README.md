# Decision Log

## Purpose

This file records all decisions made.

## 2026-01-04: Initial System Setup

- Configured VS Code to force Bash terminal (already present in settings.json)
- Created agent tracking system (AGENTS.md)
- Established "Everything-as-Code" principle

## 2026-01-05: System Consolidation & Discipline Enforcement

### Infrastructure

- Git repository re-initialized after .git loss
- GitHub remote established: <https://github.com/omar-elmountassir/system-of-intent>
- Legacy Zsh files archived to ~/legacy_zsh_archive/
- Repository made public for Mind access

### Golden Rules Enacted

- Rule #1: Persistence First
- Rule #2: Zero Silent Failures
- Rule #3: Halt on Uncertainty
- Rule #4: Mandatory Initialization
- Rule #5: ROADMAP First (ZERO TOLERANCE)
- Rule #6: Sub-Agent Context Responsibility
- Rule #7: Flag It. Log It. Fix It.

### Agent Verification

- Gemini CLI: Verified functional (v0.22.5)
- OpenAI Codex: Verified functional (v0.77.0)

### Bash Configuration

- Added aliases: goto-soi, soi
- Location: ~/.bashrc

### Technical Discoveries

- `source ~/.bashrc` fails from Zsh (shopt is bash-only)
- Non-interactive bash (`bash -c`) doesn't load .bashrc
- Interactive bash (`bash -i -c`) required for alias testing
- ble.sh requires bash context for initialization

### Anti-Pattern Identified: "Heuristique de la Facilite"

Agent tendency to fill unknowns with probabilities instead of stopping:

1. "C'est rien" hypothesis - Assuming errors are benign
2. Context hypothesis - Assuming environment without verification
3. Causality hypothesis - Deducing without formal proof

### Orchestrator Role Established

- Claude Code designated as Lead Orchestrator
- Zero self-work rule: delegate everything to sub-agents
- Incident log created at [Logs - Incidents](/logs/incidents/README.md)
