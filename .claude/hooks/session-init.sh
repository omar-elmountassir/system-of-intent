#!/bin/bash
# SessionStart Hook: Initializes session with System of Intent context
#
# Part of System of Intent - ensures agents always have base context

# Set environment variables for the session
if [ -n "$CLAUDE_ENV_FILE" ]; then
    echo 'export SOI_ROOT="/home/omar/system-of-intent"' >> "$CLAUDE_ENV_FILE"
    echo 'export REPORTS_DIR="$SOI_ROOT/reports"' >> "$CLAUDE_ENV_FILE"
    echo 'export DOCS_DIR="$SOI_ROOT/docs"' >> "$CLAUDE_ENV_FILE"
fi

# Output context reminder (will be shown to Claude)
cat << 'EOF'
## System of Intent Session Started

Remember the Golden Rules:
1. Persistence First - Save everything to files
2. Zero Silent Failures - Report all errors
3. Halt on Uncertainty - Ask, don't guess
4. Mandatory Initialization - Read docs first
5. ROADMAP First - Register all work
6. Sub-Agent Context - They are BLANK SLATES
7. Flag It. Log It. Fix It.

Repository: /home/omar/system-of-intent
EOF

exit 0
