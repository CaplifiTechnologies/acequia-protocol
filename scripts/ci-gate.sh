#!/usr/bin/env bash
# ci-gate.sh — Automated safety checks for Ditch AI contributions.
#
# Runs the egress headgate checks that protect the commons:
#   1. IP fence       — held IP markers must not cross into the package
#   2. House paths    — no references to private infrastructure
#   3. Secret scan    — no keys, tokens, or credentials
#   4. DCO sign-off   — every commit in the PR must be signed
#   5. Test suite     — all tests must pass
#
# Usage:
#   ./scripts/ci-gate.sh              # run all gates
#   ./scripts/ci-gate.sh --skip-dco   # skip DCO check (local dev)
#
# Exit codes:
#   0  all gates passed
#   1  a gate failed (details printed)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FAIL=0
SKIP_DCO=false

for arg in "$@"; do
    case "$arg" in
        --skip-dco) SKIP_DCO=true ;;
    esac
done

red()   { printf '\033[1;31m%s\033[0m\n' "$1"; }
green() { printf '\033[1;32m%s\033[0m\n' "$1"; }
header(){ printf '\n\033[1;36m── %s ──\033[0m\n' "$1"; }

# ── Gate 1: IP fence ──
header "Gate 1: IP fence"

IP_MARKERS=(
    "ipc_0670fb9609"
)

ip_hits=""
for marker in "${IP_MARKERS[@]}"; do
    found=$(grep -rn --exclude-dir='__pycache__' --exclude='*.pyc' "$marker" \
        "$REPO_ROOT/app/" "$REPO_ROOT/tests/" "$REPO_ROOT/specs/" "$REPO_ROOT/docs/" \
        2>/dev/null || true)
    if [ -n "$found" ]; then
        ip_hits="$ip_hits\n$found"
    fi
done

if [ -n "$ip_hits" ]; then
    red "FAIL: Held IP markers found in public paths:"
    echo -e "$ip_hits"
    FAIL=1
else
    green "PASS: No held IP markers in public paths"
fi

# ── Gate 2: House path scan ──
header "Gate 2: House path scan"

HOUSE_PATTERNS=(
    '~/ALMI/'
    '~/esoteric-kb/'
    '~/command-almi/'
    '~/ui-hub/'
    '~/agent-spend-spine/'
    '~/headgate-egress/'
    '~/house-mail/'
    '~/goal-bot/'
    '/Users/matthewgallegos/'
    'gallegoshouse.com'
    'matt@'
    'sirgrok@'
)

house_hits=""
for pattern in "${HOUSE_PATTERNS[@]}"; do
    found=$(grep -rn --exclude-dir='__pycache__' --exclude='*.pyc' "$pattern" \
        "$REPO_ROOT/app/" \
        "$REPO_ROOT/tests/" \
        "$REPO_ROOT/specs/" \
        "$REPO_ROOT/docs/" \
        "$REPO_ROOT/pyproject.toml" \
        2>/dev/null || true)
    if [ -n "$found" ]; then
        house_hits="$house_hits\n$found"
    fi
done

if [ -n "$house_hits" ]; then
    red "FAIL: House-specific paths found in public code:"
    echo -e "$house_hits"
    FAIL=1
else
    green "PASS: No house-specific paths in public code"
fi

# ── Gate 3: Secret scan ──
header "Gate 3: Secret scan"

SECRET_PATTERNS=(
    'PRIVATE KEY'
    'sk-[a-zA-Z0-9]'
    'sk_live_'
    'sk_test_'
    'xai-[a-zA-Z0-9]'
    'ghp_[a-zA-Z0-9]'
    'gho_[a-zA-Z0-9]'
    'AKIA[A-Z0-9]'
    'password\s*='
    'api_key\s*='
    'secret_key\s*='
    'token\s*=\s*"'
    'Bearer [a-zA-Z0-9]'
)

secret_hits=""
for pattern in "${SECRET_PATTERNS[@]}"; do
    found=$(grep -rn -E --exclude-dir='__pycache__' --exclude='*.pyc' "$pattern" \
        "$REPO_ROOT/app/" \
        "$REPO_ROOT/tests/" \
        "$REPO_ROOT/specs/" \
        "$REPO_ROOT/scripts/" \
        "$REPO_ROOT/docs/" \
        2>/dev/null || true)
    if [ -n "$found" ]; then
        secret_hits="$secret_hits\n$found"
    fi
done

if [ -n "$secret_hits" ]; then
    red "FAIL: Possible secrets or credentials found:"
    echo -e "$secret_hits"
    FAIL=1
else
    green "PASS: No secrets detected"
fi

# ── Gate 4: DCO sign-off ──
header "Gate 4: DCO sign-off"

if [ "$SKIP_DCO" = true ]; then
    green "SKIP: DCO check skipped (--skip-dco)"
elif git rev-parse --git-dir > /dev/null 2>&1; then
    BASE="${CI_MERGE_REQUEST_TARGET_BRANCH_SHA:-${GITHUB_BASE_REF:-main}}"
    if git rev-parse "$BASE" > /dev/null 2>&1; then
        unsigned=$(git log "$BASE"..HEAD --format='%H %s' | while read hash msg; do
            if ! git log -1 --format='%b' "$hash" | grep -q '^Signed-off-by:'; then
                echo "  $hash $msg"
            fi
        done)
        if [ -n "$unsigned" ]; then
            red "FAIL: Commits missing DCO sign-off:"
            echo "$unsigned"
            FAIL=1
        else
            green "PASS: All commits signed off"
        fi
    else
        green "SKIP: Base branch '$BASE' not found (initial repo)"
    fi
else
    green "SKIP: Not a git repository"
fi

# ── Gate 5: Test suite ──
header "Gate 5: Test suite"

cd "$REPO_ROOT"
if python3 -m pytest tests/test_acequia.py tests/test_headgate.py -v --tb=short 2>&1; then
    green "PASS: Core tests passed"
else
    red "FAIL: Tests failed"
    FAIL=1
fi

# ── Summary ──
echo ""
if [ "$FAIL" -eq 0 ]; then
    green "All gates passed."
else
    red "One or more gates failed. Fix the issues above before submitting."
fi

exit $FAIL
