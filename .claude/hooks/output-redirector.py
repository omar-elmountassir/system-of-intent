#!/usr/bin/env python3
"""
UserPromptSubmit Hook: Injects context to redirect substantial outputs to files.

This hook detects when users request reports, synthesis, or analysis and
injects additional context telling Claude to save to files instead of chat.

Part of System of Intent - Golden Rule #1: Persistence First
"""
import json
import sys

def main():
    try:
        hook_input = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(1)

    prompt = hook_input.get('prompt', '').lower()

    # Detect substantial output requests
    substantial_keywords = [
        'report', 'synthesis', 'summary', 'analysis', 'documentation',
        'plan', 'proposal', 'review', 'audit', 'findings', 'results',
        'comprehensive', 'detailed', 'full', 'complete'
    ]

    is_substantial = any(keyword in prompt for keyword in substantial_keywords)

    if is_substantial:
        additional_context = """
## IMPORTANT: Output Persistence Reminder

You are operating under the System of Intent's Golden Rule #1: Persistence First.

When generating substantial outputs (reports, synthesis, analysis, documentation):
1. SAVE the output to a file in the appropriate directory:
   - Reports → `/reports/`
   - Proposals → `/docs/proposals/`
   - Analysis → `/reports/`
2. Include a reference to the file path in your response
3. Provide a brief summary in chat, NOT the full content
4. Example: "I've saved the analysis to reports/analysis_2026-01-05.md"

NEVER output substantial content directly in chat - it violates Golden Rule #1.
"""
        output = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": additional_context
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
