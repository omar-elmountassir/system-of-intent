# System of Intent

## Core

### Philosophy

This workstation operates on a "Mind-Body" paradigm:

- **Mind**: Omar - Strategic direction and intent
- **Body**: AI Agents - Execution and implementation

## Principles

### Architectural

#### 1. Everything-as-Code

All system configurations, workflows, and decisions are documented and version-controlled.

#### 2. Agent Orchestration

Multiple AI agents work in concert, each with specialized capabilities:

- Claude Code: System configuration, code implementation
- Gemini CLI: TBD
- OpenAI Codex: TBD

#### 3. Intentional Computing

Every action traces back to explicit user intent. No implicit behaviors.

## Rules

### Golden Rules [MANDATORY]

#### 1. Persistence First

**Nothing remains in chat. Every decision, status change, or new information MUST be recorded in the repository files immediately.**

#### 2. Zero Silent Failures

**Any warning, error, or unexpected output (stderr) must be REPORTED to the Mind immediately. Do not assume 'it's fine'. Let the Mind decide.**

#### 3. Halt on Uncertainty

**If a command fails, returns unexpected data, or displays a warning, or if functionality is ambiguous, STOP immediately. Do not guess the cause. Do not assume it is benign. Report the anomaly to the Mind and ask for clarification.**

#### 4. Mandatory Initialization

- If NEVER READ, ALWAYS START BY READING ONCE:
  - [System of Intent](SYSTEM_OF_INTENT.md)
  - [Roadmap](ROADMAP.md)
- ALL WORK IN HAND MUST BE ENTER IN / ADDED TO OUR ROADMAP FIRST!
- AGENTS MUST MAINTAIN THE ROADMAP UPDATING IT EACH TIME A PROGRESS IS MADE!

#### 5. ROADMAP First (ZERO TOLERANCE)

**ALL work must be registered in ROADMAP.md BEFORE execution.**
- No exceptions - even simple Read operations
- All agents must migrate their work plans to ROADMAP.md
- Work must be atomically broken down
- Systematically registered for tracking
- This enables proper tracking and continuous improvement

#### 6. Sub-Agent Context Responsibility

**Sub-agents are BLANK SLATES. The orchestrator MUST:**
- Prepare comprehensive context before launching
- Include ALL relevant rules, constraints, and system knowledge
- Provide specific file paths and code references
- Never assume sub-agents "know" anything
- Think hard before prompting - they have no memory

#### 7. Flag It. Log It. Fix It.

**When an issue is identified:**
1. FLAG IT - Acknowledge the issue immediately
2. LOG IT - Record in incident log with full details
3. FIX IT - Implement corrective actions
4. UPDATE - Update all relevant documentation
5. REPORT - Create comprehensive report

**Incident Log Location**: `logs/incidents/README.md`

## Current

### Configuration

#### System

- Default Shell: Zsh (`/usr/bin/zsh`)
- VS Code Terminal: Bash (configured in settings.json)
- Bash Enhancements: ble.sh + Starship prompt

### Registries

#### AI Agents Workforce Registry

| Agent        | Status   | Version | Path                                                | Role                                                                                       |
| ------------ | -------- | ------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Claude Code  | Active   | v2.0.76 | `/home/omar/.nvm/versions/node/v24.12.0/bin/claude` | Primary execution agent for system configuration, code implementation, and file operations |
| Gemini CLI   | Verified | v0.22.5 | `/home/omar/.nvm/versions/node/v24.12.0/bin/gemini` | Interactive AI agent for prompt-based tasks, MCP server management, and extensions         |
| OpenAI Codex | Verified | v0.77.0 | `/home/omar/.nvm/versions/node/v24.12.0/bin/codex`  | Code generation, review, and sandboxed execution agent with MCP support                    |

#### Environment

##### Terminal

// TODOs: TO BE VERIFIED FACTUALLY!

- **Default Shell**: Zsh (system-wide) // TODO: MUST BE SWITCHED TO BASH ONCE ZSH MIGRATION IS DONE
- **VS Code Terminal**: Bash (application-specific override)
- **Shell Enhancements**:
  - ble.sh for enhanced line editing
  - Starship for cross-shell prompts

#### Settings

##### VS Code

// TODOs: TO BE VERIFIED FACTUALLY!

- Terminal default profile: Bash
- Security: Workspace trust enabled
- Telemetry: Disabled
- Auto-save: Enabled with delay

### Tooling

- **GitHub CLI (`gh`)**: Installed and ready for use
- **Claude CLI (`claude`)**: Installed and ready for use
- **Gemini CLI (`gemini`)**: Installed and ready for use
- **Codex CLI (`codex`)**: Installed and ready for use

### Mind Connection

- **Repository**: https://github.com/omar-elmountassir/system-of-intent (Public Access Confirmed)
- **Status**: Connected and accessible to the Mind
- **Established**: 2026-01-05

## Logs

[Logs](./logs/README.md)

## Next Steps

ALL OUR NEXTS STEPS (EVEN THOSE RECOMMMANDED, SUGGESTED, ETC.. MUST BE ENTERED IN / ADDED TO OUR ROADMAP IMMEDIATLY !!! NEVER IN THE CHAT!) [ROADMAP.md](ROADMAP.md)
