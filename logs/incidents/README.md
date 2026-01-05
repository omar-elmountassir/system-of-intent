# Incident Log

This file records all incidents where agent behavior violated or nearly violated the Golden Rules.

---

## Incident #001 - Near Rule Violation
**Date**: 2026-01-05
**Severity**: CRITICAL
**Status**: Prevented by Mind

**What happened**:
- Claude was about to launch Explore sub-agents
- Did NOT consider that sub-agents are BLANK SLATES (no shared context)
- Did NOT prepare proper context/prompts with rules
- Did NOT add research tasks to ROADMAP.md first
- Would have ignored this violation if the Mind hadn't stopped

**Root cause**: "Heuristique de la Facilite" - assumed sub-agents would "just work"

**Corrective actions**:
1. Incident documented
2. Golden Rules 5-7 added
3. Agent orchestration protocols updated
4. Never launch sub-agents without explicit context preparation

---

## Incident #002 - Executor Instead of Orchestrator
**Date**: 2026-01-05
**Severity**: CRITICAL
**Status**: Prevented by Mind

**What happened**:
- Plan was approved, Claude started execution
- Began reading files and preparing to EDIT THEM DIRECTLY
- Was about to do the work instead of DELEGATING to sub-agents
- Forgot role: ORCHESTRATOR, not EXECUTOR

**Root cause**: Default behavior pattern - doing work instead of delegating

**Corrective actions**:
1. Incident documented
2. Zero self-work rule confirmed
3. Role clarified: Plan -> Prepare Context -> Launch Agents -> Monitor -> Synthesize
