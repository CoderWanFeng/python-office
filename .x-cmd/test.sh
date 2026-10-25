#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# .x-cmd/test.sh — E2E smoke tests for the `po` CLI (python-office)
#
# Runs the command line the way a user does and checks exit codes, output
# shape and produced files.
#
#   .x-cmd/test.sh                  # real mode when deps are installed,
#                                    # otherwise stub mode automatically
#   PO_TEST_STUB=1 .x-cmd/test.sh   # force stub mode (no po* deps needed)
#
# Real mode exercises actual file transforms (txt2pdf → merge2pdf,
# fake2excel → excel2markdown …) and verifies the output files exist.
# Stub mode preloads MagicMock modules for the po* deps, so parser, help,
# version, platform guard and --json plumbing are still tested end-to-end.
# -----------------------------------------------------------------------------
set -u

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)
PY=${PO_PYTHON:-python3}
export PYTHONPATH="$REPO_ROOT${PYTHONPATH:+:$PYTHONPATH}"
cd "$REPO_ROOT"

PASS=0; FAIL=0; SKIP=0; N=0
WORK=$(mktemp -d /tmp/po-cli-test.XXXXXX)
trap 'rm -rf "$WORK"' EXIT

# --- helpers -------------------------------------------------------------------
result() {  # result <ok|not-ok|skip> <description>
    N=$((N + 1))
    case "$1" in
        ok)     PASS=$((PASS + 1)); printf 'ok     %3d - %s\n' "$N" "$2" ;;
        not-ok) FAIL=$((FAIL + 1)); printf 'not ok %3d - %s\n' "$N" "$2" ;;
        skip)   SKIP=$((SKIP + 1)); printf 'skip   %3d - %s\n' "$N" "$2" ;;
    esac
}

# --- mode detection & launcher --------------------------------------------------
# office/__init__ lazy-loads the api modules, so the probe imports exactly the
# modules the core battery dispatches; when that fails we run the same entry
# point through a stub-preloading launcher (mirrors pytest).
STUBS_NEEDED=0
if ! "$PY" -c "import office.api.pdf, office.api.excel, office.api.tools, office.api.image, office.api.file, office.api.markdown, office.api.finance" >/dev/null 2>&1; then
    STUBS_NEEDED=1
fi
[ "${PO_TEST_STUB:-0}" = "1" ] && STUBS_NEEDED=1

mkdir -p "$WORK/bin"
cat > "$WORK/bin/po_env.py" <<'PYEOF'
"""Shared launcher: optionally stub the po* deps, then run office.cli.main."""
import sys
from unittest import mock

STUB_NAMES = (
    "popdf", "poexcel", "poimage", "pofile", "wftools", "povideo",
    "poprogress", "poocr", "pocode", "pocode.api", "pocode.api.color",
    "poemail", "pospider", "pomarkdown", "poword", "poppt",
    "PyOfficeRobot", "search4file", "akshare", "moviepy",
)


def install_stubs():
    import types
    for name in STUB_NAMES:
        if name in sys.modules:
            continue
        module = types.ModuleType(name)
        module.__path__ = []
        module.__getattr__ = lambda attr, _n=name: mock.MagicMock(name="%s.%s" % (_n, attr))
        sys.modules[name] = module
    # deterministic error-path fixture for the --json failure test
    sys.modules["wftools"].url2ip = mock.MagicMock(side_effect=RuntimeError("stub boom"))


def main(argv):
    want_dump = "--dump-registry" in argv
    if want_dump:
        argv.remove("--dump-registry")
    if "--stub" in argv:
        argv.remove("--stub")
        install_stubs()
    import os
    if os.environ.get("PO_TEST_INJECT_GUARD") and not want_dump:
        from office.cli import commands
        commands.MODULES["wintest"] = {
            "module": "office.api.never_imported",
            "help": "platform guard probe (test only)",
            "platforms": ["win32"],
            "commands": {"probe": {"help": "probe", "params": []}},
        }
    if want_dump:
        from office.cli import commands
        for module_name in sorted(commands.MODULES):
            for command_name in sorted(commands.MODULES[module_name]["commands"]):
                print("%s %s" % (module_name, command_name))
        return 0
    from office.cli.main import main as cli_main
    return cli_main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
PYEOF

if [ "$STUBS_NEEDED" = "1" ]; then
    MODE=stub
    po() { "$PY" "$WORK/bin/po_env.py" --stub "$@"; }
else
    MODE=real
    if command -v po >/dev/null 2>&1; then
        po() { command po "$@"; }          # installed entry point
    else
        po() { "$PY" -m office "$@"; }     # repo checkout, deps installed
    fi
fi
run_python() {
    if [ "$STUBS_NEEDED" = "1" ]; then
        "$PY" "$WORK/bin/po_env.py" --stub "$@"
    else
        "$PY" "$WORK/bin/po_env.py" "$@"
    fi
}
printf '# po CLI smoke tests — mode: %s (python: %s)\n\n' "$MODE" "$("$PY" --version 2>&1)"

# --- 1. version / top-level help -------------------------------------------------
VOUT=$WORK/version.out
if po --version >"$VOUT" 2>"$WORK/version.err" && head -1 "$VOUT" | grep -q '^po '; then
    result ok "po --version prints version (exit 0)"
else
    result not-ok "po --version prints version (exit 0): $(cat "$VOUT" "$WORK/version.err" 2>/dev/null)"
fi

HOUT=$WORK/help.out
if po --help >"$HOUT" 2>&1 && grep -q "usage:" "$HOUT" \
        && grep -qw excel "$HOUT" && grep -qw image "$HOUT"; then
    result ok "po --help lists modules"
else
    result not-ok "po --help lists modules"
fi

# --- 2. per-module and per-command --help (all modules / 60+ commands) -----------
REGISTRY=$(run_python --dump-registry 2>/dev/null)
CMD_TOTAL=$(echo "$REGISTRY" | grep -c . || true)
if [ "${CMD_TOTAL:-0}" -ge 40 ]; then
    result ok "registry dumps $CMD_TOTAL commands (>= 40)"
else
    result not-ok "registry dumps >= 40 commands (got ${CMD_TOTAL:-0})"
fi

MODULE_HELP_FAIL=0
for module_name in $(echo "$REGISTRY" | awk '{print $1}' | sort -u); do
    po "$module_name" --help >/dev/null 2>&1 || MODULE_HELP_FAIL=$((MODULE_HELP_FAIL + 1))
done
if [ "$MODULE_HELP_FAIL" = 0 ]; then
    result ok "every module --help exits 0"
else
    result not-ok "module --help failures: $MODULE_HELP_FAIL"
fi

CMD_HELP_FAIL=0
while read -r module_name command_name; do
    po "$module_name" "$command_name" --help >/dev/null 2>&1 \
        || CMD_HELP_FAIL=$((CMD_HELP_FAIL + 1))
done <<EOF
$REGISTRY
EOF
if [ "$CMD_HELP_FAIL" = 0 ]; then
    result ok "all $CMD_TOTAL command --help exit 0"
else
    result not-ok "command --help failures: $CMD_HELP_FAIL/$CMD_TOTAL"
fi

# --- 3. usage errors & platform guard ---------------------------------------------
po pdf definitely-not-a-command >/dev/null 2>&1
[ $? = 2 ] && result ok "unknown command → exit 2 (usage error)" \
          || result not-ok "unknown command → exit 2 (usage error)"

po >/dev/null 2>&1
[ $? = 2 ] && result ok "no arguments → exit 2 (usage error)" \
          || result not-ok "no arguments → exit 2 (usage error)"

GUARD_ERR=$WORK/guard.err
PO_TEST_INJECT_GUARD=1 run_python wintest probe >/dev/null 2>"$GUARD_ERR"; RC=$?
if [ "$RC" = 1 ] && grep -q "only available on" "$GUARD_ERR"; then
    result ok "platform guard blocks win-only module (exit 1, clean msg, no import)"
else
    result not-ok "platform guard (rc=$RC): $(cat "$GUARD_ERR")"
fi

# --- 4. --json output shape (finance.t0 is pure stdlib → works in both modes) -----
T0=$WORK/t0.json
po --json finance t0 10 11 100 >"$T0" 2>/dev/null; RC=$?
LINES=$(wc -l < "$T0" | tr -d ' ')
if [ "$RC" = 0 ] && [ "$LINES" = 1 ] \
        && "$PY" - "$T0" <<'PYCHK'
import json, sys
d = json.load(open(sys.argv[1]))
assert d["ok"] is True and abs(float(d["result"]) - 88.9) < 0.01, d
PYCHK
then
    result ok "--json finance t0: one-line JSON, ok=true, result≈88.9"
else
    result not-ok "--json finance t0: rc=$RC $(cat "$T0")"
fi

# deterministic error path: stub mode raises via fixture; real mode feeds a
# nonexistent file to merge2pdf (popdf must raise, not silently succeed)
JERR=$WORK/jerr.json
if [ "$MODE" = stub ]; then
    po --json tools url2ip example.com >/dev/null 2>"$JERR"; RC=$?
else
    (cd "$WORK" && po --json pdf merge2pdf does-not-exist.pdf >/dev/null 2>"$JERR"); RC=$?
fi
JERR_LAST=$(tail -n 1 "$JERR")   # 末行为 JSON；前面可能有库的导入期告警
if [ "$RC" = 1 ] && "$PY" -c '
import json, sys
d = json.loads(sys.argv[1])
assert d["ok"] is False and d["error"], d
' "$JERR_LAST"; then
    result ok "--json error path: exit 1, stderr JSON ok=false (last line)"
else
    result not-ok "--json error path (rc=$RC): $(cat "$JERR")"
fi

# --- 5. real file transforms (real mode only) --------------------------------------
if [ "$MODE" = real ]; then
    cd "$WORK"

    printf 'hello python-office\nline two\n' > a.txt
    po pdf txt2pdf a.txt --output-file a.pdf >/dev/null 2>&1 \
        && [ -s a.pdf ] && result ok "pdf txt2pdf produces non-empty a.pdf" \
        || result not-ok "pdf txt2pdf produces non-empty a.pdf"

    po pdf merge2pdf a.pdf a.pdf --output-file m.pdf >/dev/null 2>&1 \
        && [ -s m.pdf ] && result ok "pdf merge2pdf produces non-empty m.pdf" \
        || result not-ok "pdf merge2pdf produces non-empty m.pdf"

    po excel fake2excel --columns name company --rows 5 --path f.xlsx >/dev/null 2>&1 \
        && [ -s f.xlsx ] && result ok "excel fake2excel produces non-empty f.xlsx" \
        || result not-ok "excel fake2excel produces non-empty f.xlsx"

    po markdown excel2markdown f.xlsx --output-file f.md >/dev/null 2>&1 \
        && [ -s f.md ] && grep -q '|' f.md \
        && result ok "markdown excel2markdown produces table" \
        || result not-ok "markdown excel2markdown produces table"

    PW=$WORK/pw.json
    if po --json tools passwordtools --len 16 >"$PW" 2>/dev/null \
            && "$PY" - "$PW" <<'PYCHK'
import json, sys
d = json.load(open(sys.argv[1]))
assert d["ok"] and len(d["result"]) == 16, d
PYCHK
    then
        result ok "tools passwordtools --json returns 16-char password"
    else
        result not-ok "tools passwordtools --json: $(cat "$PW" 2>/dev/null)"
    fi
else
    result skip "pdf txt2pdf / merge2pdf (needs real deps)"
    result skip "excel fake2excel (needs real deps)"
    result skip "markdown excel2markdown (needs real deps)"
    result skip "tools passwordtools real (needs real deps)"
fi

# --- summary -------------------------------------------------------------------------
printf '\n# %d passed, %d failed, %d skipped (mode=%s)\n' "$PASS" "$FAIL" "$SKIP" "$MODE"
[ "$FAIL" = 0 ]
