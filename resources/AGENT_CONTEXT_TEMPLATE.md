# Agent Context Template

This template is used by the Lead Orchestrator (Claude Code) to prepare comprehensive prompts for sub-agents. Sub-agents are BLANK SLATES - they have no shared context.

---

## Template Structure

When launching a sub-agent, the orchestrator MUST include ALL of the following sections:

### 1. Mission Statement

```
You are executing [TASK NAME] for the System of Intent. You are a BLANK SLATE - you have no prior context.

## YOUR MISSION
[Clear, specific description of what the sub-agent must accomplish]
```

### 2. Repository Context

```
## REPOSITORY LOCATION
`/home/omar/system-of-intent`

## CRITICAL CONSTRAINTS
1. ALL files must be in ENGLISH
2. Follow existing file patterns/formatting
3. Commit with proper message format
4. Push to origin main after commit
```

### 3. Golden Rules Summary

Include relevant rules for the task:

- **Rule #1 - Persistence First**: Record everything to files immediately
- **Rule #2 - Zero Silent Failures**: Report ALL errors to the Mind
- **Rule #3 - Halt on Uncertainty**: STOP and ASK, never guess
- **Rule #5 - ROADMAP First**: ALL work must be in ROADMAP.md first
- **Rule #7 - Flag It. Log It. Fix It.**: Document all incidents

### 4. File Context

For each file the sub-agent will modify:

```
## FILE: [path]
**Current content** (relevant lines):
[Include actual file content so sub-agent knows what to edit]

**Required changes**:
[Specific instructions for what to change]
```

### 5. Task Details

Break down into numbered tasks:

```
## TASK 1: [Name]
**File**: [path]
**Action**: [Create/Edit/Delete]
**Details**: [Specific instructions]
```

### 6. Git Instructions

```
## COMMIT AND PUSH
After completing all tasks:
git add [files]
git commit -m "[conventional commit message]

Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
git push origin main
```

### 7. Verification

```
## VERIFICATION
After completing, run:
git status
git log -1
[any other verification commands]
Report the results.
```

### 8. Prohibitions

```
## DO NOT
- Do NOT assume anything not explicitly stated
- Do NOT skip any task
- Do NOT modify files other than the ones listed
- Do NOT ask questions - execute the plan
```

---

## Checklist Before Launching Sub-Agent

- [ ] Mission is clear and specific
- [ ] Repository location is included
- [ ] Relevant Golden Rules are summarized
- [ ] All file contents are provided (sub-agents can't see our context)
- [ ] Tasks are numbered and detailed
- [ ] Git commit message follows conventional format
- [ ] Verification steps are included
- [ ] Prohibitions are listed

---

## Example Minimal Prompt

```
You are executing [TASK] for the System of Intent. You are a BLANK SLATE.

## YOUR MISSION
[Description]

## REPOSITORY LOCATION
`/home/omar/system-of-intent`

## CONSTRAINTS
1. ALL files in ENGLISH
2. Commit and push after changes

## TASK 1: [Name]
**File**: [path]
**Current content**: [content]
**Change to**: [new content]

## COMMIT
git add [file] && git commit -m "type: description" && git push origin main

## VERIFY
git status && git log -1

## DO NOT
- Assume anything not stated
- Modify other files
```

---

_Last updated: 2026-01-05_
