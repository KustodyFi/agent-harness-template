#!/bin/bash
# Agent Harness Template — First-Run Setup
# This script initializes the harness for your project.

set -e

echo ""
echo "🔧 Agent Harness Template — Setup"
echo "=================================="
echo ""

# Collect project info
read -p "Project name (e.g., FX-Town): " PROJECT_NAME
read -p "Project description: " PROJECT_DESCRIPTION
read -p "Tech stack (e.g., Python 3.11 · Redis · Docker): " TECH_STACK
read -p "Current phase (e.g., Phase 1 — Foundation): " CURRENT_PHASE

PROJECT_NAME_LOWER=$(echo "$PROJECT_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
DATE=$(date +%Y-%m-%d)

# Escape special characters for sed replacement strings
escape_sed() {
  printf '%s' "$1" | sed 's/[\/&\\]/\\&/g'
}

PROJECT_NAME_ESC=$(escape_sed "$PROJECT_NAME")
PROJECT_NAME_LOWER_ESC=$(escape_sed "$PROJECT_NAME_LOWER")
PROJECT_DESCRIPTION_ESC=$(escape_sed "$PROJECT_DESCRIPTION")
TECH_STACK_ESC=$(escape_sed "$TECH_STACK")
CURRENT_PHASE_ESC=$(escape_sed "$CURRENT_PHASE")

echo ""
echo "📝 Applying to template files..."

# OS-portable sed in-place: macOS uses `sed -i ''`, Linux uses `sed -i`
if [[ "$OSTYPE" == "darwin"* ]]; then
  SED_INPLACE=(sed -i '')
else
  SED_INPLACE=(sed -i)
fi

# Replace placeholders in templated files
for file in AGENTS.md agent.project.md README.template.md .cowork/STATUS.md .agent.default/shared/log.md; do
  if [ -f "$file" ]; then
    "${SED_INPLACE[@]}" "s/{{PROJECT_NAME}}/$PROJECT_NAME_ESC/g" "$file"
    "${SED_INPLACE[@]}" "s/{{PROJECT_NAME_LOWER}}/$PROJECT_NAME_LOWER_ESC/g" "$file"
    "${SED_INPLACE[@]}" "s/{{PROJECT_DESCRIPTION}}/$PROJECT_DESCRIPTION_ESC/g" "$file"
    "${SED_INPLACE[@]}" "s/{{TECH_STACK}}/$TECH_STACK_ESC/g" "$file"
    "${SED_INPLACE[@]}" "s/{{CURRENT_PHASE}}/$CURRENT_PHASE_ESC/g" "$file"
    "${SED_INPLACE[@]}" "s/{{DATE}}/$DATE/g" "$file"
  fi
done

# Swap template README → project README
if [ -f "README.template.md" ]; then
  mv README.template.md README.md
  echo "✅ README.template.md → README.md (project README)"
fi

# Remove auto-bootstrap workflow (manual setup replaces it)
if [ -f ".github/workflows/bootstrap.yml" ]; then
  rm -f .github/workflows/bootstrap.yml
  rmdir .github/workflows 2>/dev/null || true
  rmdir .github 2>/dev/null || true
  echo "✅ Removed bootstrap.yml (not needed after manual setup)"
fi

echo "✅ Placeholders replaced"

# Bootstrap .agent/ from .agent.default/
if [ ! -d ".agent" ]; then
  cp -r .agent.default .agent
  echo "✅ Copied .agent.default/ → .agent/ (your local working copy)"
else
  echo "⚠️  .agent/ already exists — skipping copy"
fi

echo ""
echo "🎉 Harness initialized for $PROJECT_NAME"
echo ""
echo "Next steps:"
echo "  1. Edit agent.project.md — fill in your architectural invariants"
echo "  2. Read AGENTS.md — your AI agent entry point"
echo "  3. Start working!"
echo ""
