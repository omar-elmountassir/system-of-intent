# Compact Command Template

> **PURPOSE**: Copy-paste this into the /compact command to ensure perfect session continuity.

---

## How to Use

1. Run `/compact` in Claude Code
2. When prompted, paste the **COMPACT INSTRUCTIONS** below
3. Claude will compress context while preserving critical memory

---

## COMPACT INSTRUCTIONS

```text
CRITICAL MEMORY PRESERVATION INSTRUCTIONS:

After this compact, you MUST:

1. IMMEDIATELY READ these files in order:
   - /home/omar/system-of-intent/.memory/CONTEXT.md (FULL STATE)
   - /home/omar/system-of-intent/SYSTEM_OF_INTENT.md
   - /home/omar/system-of-intent/ROADMAP.md

2. REMEMBER the 4 Golden Rules:
   - Persistence First: Record everything to files, nothing stays in chat
   - Zero Silent Failures: Report ALL errors to the Mind
   - Halt on Uncertainty: STOP and ASK, never guess
   - Mandatory Initialization: Read docs before acting

3. FORBIDDEN BEHAVIOR - "Heuristique de la Facilité":
   - Never assume errors are benign
   - Never assume environment context
   - Never deduce without proof
   - ALWAYS: Know or Ask, NEVER Guess

4. IDENTITY:
   - Repository: https://github.com/omar-elmountassir/system-of-intent
   - Local path: /home/omar/system-of-intent
   - Quick nav: goto-soi or soi (bash aliases)

5. CURRENT STATE:
   - Shell context is ZSH (pop-os% prompt), VS Code uses Bash
   - source ~/.bashrc fails from Zsh (shopt is bash-only)
   - Use bash -i -c "command" to test bash things
   - Legacy Zsh archived to ~/legacy_zsh_archive/

6. WORKFORCE:
   - Claude Code: Active (primary)
   - Gemini CLI: Verified
   - OpenAI Codex: Verified

7. PENDING TASKS (check .memory/CONTEXT.md for updates):
   - Complete persistence audit
   - Update ROADMAP after Mind confirms Repo Sharing

8. PARADIGM:
   - Mind-Body architecture (Omar = Mind, Agents = Body)
   - OODA Loop enforcement: Halt at Orient if uncertain
   - Mind approval required for uncertainty resolution

AFTER READING .memory/CONTEXT.md, update it if any new information was learned during this session before the compact.
```

---

## Alternative: Quick Compact

For faster compacts when less context is needed:

```text
MEMORY: Read /home/omar/system-of-intent/.memory/CONTEXT.md immediately after compact. Follow the 4 Golden Rules. Never assume - always verify or ask. Repository: https://github.com/omar-elmountassir/system-of-intent
```

---

## Post-Compact Verification

After compact completes, verify Claude remembers by asking:
- "What are the 4 Golden Rules?"
- "What is the Heuristique de la Facilité?"
- "What is the GitHub repository URL?"

If Claude doesn't know, instruct it to read `.memory/CONTEXT.md`.
