#!/bin/bash
# Data Analyst Plugin - Session Start Hook
# Loads environment config if exists and provides context to Claude

set -euo pipefail

CONFIG_FILE=".claude/data-analyst.local.md"
SESSION_LOG=".claude/session-log.md"

# Build system message
message=""

# Check for config file
if [ -f "$CONFIG_FILE" ]; then
    # Extract key info from YAML frontmatter
    if command -v yq &> /dev/null; then
        env_name=$(yq -r '.environment.name // empty' "$CONFIG_FILE" 2>/dev/null || echo "")
        sql_dialect=$(yq -r '.environment.sql_dialect // empty' "$CONFIG_FILE" 2>/dev/null || echo "")
    else
        # Fallback: simple grep
        env_name=$(grep -m1 "name:" "$CONFIG_FILE" 2>/dev/null | sed 's/.*name: *"\?\([^"]*\)"\?.*/\1/' || echo "")
        sql_dialect=$(grep -m1 "sql_dialect:" "$CONFIG_FILE" 2>/dev/null | sed 's/.*sql_dialect: *"\?\([^"]*\)"\?.*/\1/' || echo "")
    fi

    if [ -n "$env_name" ] || [ -n "$sql_dialect" ]; then
        message="[Data Analyst] Config loaded"
        [ -n "$env_name" ] && message="$message - Environment: $env_name"
        [ -n "$sql_dialect" ] && message="$message - SQL: $sql_dialect"
        message="$message. Use /data-analyst:resume to see full context."
    fi
fi

# Check for session log
if [ -f "$SESSION_LOG" ]; then
    last_session=$(grep -m1 "## Last Session:" "$SESSION_LOG" 2>/dev/null | sed 's/## Last Session: //' || echo "")
    if [ -n "$last_session" ]; then
        if [ -n "$message" ]; then
            message="$message Previous session: $last_session."
        else
            message="[Data Analyst] Previous session found: $last_session. Use /data-analyst:resume to continue."
        fi
    fi
fi

# Output JSON response
if [ -n "$message" ]; then
    cat << EOF
{
  "continue": true,
  "systemMessage": "$message"
}
EOF
else
    echo '{"continue": true}'
fi
