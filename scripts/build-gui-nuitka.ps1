param(
    [switch]$OneFile,
    [switch]$AssumeYesForDownloads,
    [switch]$SkipDependencyCopy
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Entry = Join-Path $Root "gui\run.py"
$OutDir = Join-Path $Root "dist-nuitka"
$CacheDir = Join-Path $Root ".nuitka-cache"
$IconPath = Join-Path $Root "gui\assets\python-office.ico"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
New-Item -ItemType Directory -Force -Path $CacheDir | Out-Null

$env:NUITKA_CACHE_DIR = $CacheDir
$env:PYTHONPATH = $Root

$modeArgs = @("--standalone")
if ($OneFile) {
    $modeArgs = @("--onefile")
}

$downloadArgs = @()
if ($AssumeYesForDownloads) {
    $downloadArgs += "--assume-yes-for-downloads"
}

$PreviousErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = "Continue"
python -m nuitka `
    $Entry `
    @modeArgs `
    @downloadArgs `
    --mingw64 `
    --enable-plugin=pyside6 `
    --windows-console-mode=disable `
    --windows-icon-from-ico=$IconPath `
    --output-dir=$OutDir `
    --output-filename=python-office-gui `
    --include-data-file="$IconPath=gui/assets/python-office.ico" `
    --show-progress `
    --show-memory `
    --include-module=gui.run `
    --include-module=gui.app `
    --include-module=gui.main_window `
    --include-module=gui.panels `
    --include-module=gui.registry `
    --include-module=gui.styles `
    --include-module=gui.workers `
    --include-module=gui.widgets `
    --include-module=gui.widgets.param_form `
    --include-module=office `
    --include-module=office.api `
    --include-module=office.api.pdf `
    --include-module=office.api.excel `
    --include-module=office.api.word `
    --include-module=office.api.ppt `
    --include-module=office.api.image `
    --include-module=office.api.file `
    --include-module=office.api.video `
    --include-module=office.api.email `
    --include-module=office.api.ocr `
    --include-module=office.api.markdown `
    --include-module=office.api.tools `
    --include-module=office.api.finance `
    --include-module=office.lib.decorator_utils `
    --include-package=ctypes `
    --include-package=email.mime `
    --include-package=http `
    --include-package=logging `
    --include-package=urllib `
    --include-package=xml `
    --include-module=secrets `
    --include-module=smtplib `
    --include-module=socket `
    --nofollow-import-to=gui.pdf2word `
    --nofollow-import-to=gui.qtpy `
    --nofollow-import-to=popdf `
    --nofollow-import-to=poexcel `
    --nofollow-import-to=pofile `
    --nofollow-import-to=poimage `
    --nofollow-import-to=poocr `
    --nofollow-import-to=pomarkdown `
    --nofollow-import-to=poemail `
    --nofollow-import-to=povideo `
    --nofollow-import-to=wftools `
    --nofollow-import-to=poprogress `
    --nofollow-import-to=pocode `
    --nofollow-import-to=poppt `
    --nofollow-import-to=poword `
    --nofollow-import-to=search4file `
    --nofollow-import-to=loguru `
    --nofollow-import-to=you_get `
    --nofollow-import-to=openpyxl `
    --nofollow-import-to=pandas `
    --nofollow-import-to=numpy `
    --nofollow-import-to=requests `
    --nofollow-import-to=xlrd `
    --nofollow-import-to=xlwt `
    --nofollow-import-to=xlwings `
    --nofollow-import-to=pdf2docx `
    --nofollow-import-to=pypdf `
    --nofollow-import-to=PyPDF2 `
    --nofollow-import-to=reportlab `
    --nofollow-import-to=pymupdf `
    --nofollow-import-to=fitz `
    --nofollow-import-to=fontTools `
    --nofollow-import-to=PIL `
    --nofollow-import-to=cv2 `
    --nofollow-import-to=moviepy `
    --nofollow-import-to=wordcloud `
    --nofollow-import-to=PyQt5 `
    --nofollow-import-to=PyQt6 `
    --nofollow-import-to=qfluentwidgets `
    --nofollow-import-to=scrapy `
    --nofollow-import-to=PyOfficeRobot `
    --nofollow-import-to=pospider `
    --nofollow-import-to=matplotlib `
    --nofollow-import-to=scipy `
    --nofollow-import-to=tkinter `
    --remove-output
$NuitkaExitCode = $LASTEXITCODE
$ErrorActionPreference = $PreviousErrorActionPreference

if ($NuitkaExitCode -ne 0) {
    exit $NuitkaExitCode
}

if ($SkipDependencyCopy) {
    exit 0
}

$DistRuntime = Join-Path $OutDir "run.dist"
$DistLib = Join-Path $DistRuntime "lib"
New-Item -ItemType Directory -Force -Path $DistLib | Out-Null

$UsageGuide = Join-Path $Root "docs\使用教程.md"
if (Test-Path $UsageGuide) {
    Copy-Item -LiteralPath $UsageGuide -Destination (Join-Path $DistRuntime "使用教程.md") -Force
}

$copyDepsScript = @'
import importlib.metadata as md
import re
import shutil
import sys
from pathlib import Path

try:
    from packaging.requirements import Requirement
except Exception:
    Requirement = None

target = Path(sys.argv[1])
roots = sys.argv[2:]
target.mkdir(parents=True, exist_ok=True)

name_re = re.compile(r"^\s*([A-Za-z0-9_.-]+)")
seen = set()
queue = list(roots)
copied = []

def normalize(name: str) -> str:
    return name.lower().replace("_", "-")

def iter_runtime_requirements(requires):
    for req in requires or []:
        if Requirement is not None:
            try:
                parsed = Requirement(req)
            except Exception:
                parsed = None
            if parsed is not None:
                if parsed.marker and not parsed.marker.evaluate({"extra": ""}):
                    continue
                yield parsed.name
                continue

        match = name_re.match(req)
        if match:
            yield match.group(1)

def safe_target_path(record_file):
    rel = Path(record_file)
    if rel.is_absolute() or any(part in ("..", "") for part in rel.parts):
        print(f"[skip] unsafe RECORD path: {record_file}")
        return None
    return target / rel

def should_skip_package_file(record_file):
    rel = Path(record_file)
    rel_text = rel.as_posix().lower()
    if rel_text == "pandas/util/_tester.py" or rel_text.startswith("pandas/_testing/"):
        return False
    parts = {part.lower() for part in rel.parts}
    if parts & {"__pycache__", "test", "tests", "testing", "doc", "docs", "example", "examples", "sample", "samples"}:
        return True
    name = rel.name.lower()
    if name.endswith((".pyc", ".pyo", ".c", ".cpp", ".h", ".hpp", ".pxd", ".pyx")):
        return True
    if name in {"license", "copying", "authors", "contributors", "changelog"}:
        return True
    if name.endswith((".md", ".rst")):
        return True
    return False

while queue:
    raw_name = queue.pop(0)
    key = normalize(raw_name)
    if key in seen:
        continue
    try:
        dist = md.distribution(raw_name)
    except md.PackageNotFoundError:
        print(f"[skip] distribution not found: {raw_name}")
        seen.add(key)
        continue

    seen.add(normalize(dist.metadata["Name"]))
    files = list(dist.files or [])
    if not files:
        print(f"[warn] no RECORD files for: {dist.metadata['Name']}")
    for file in files:
        if should_skip_package_file(file):
            continue
        src = Path(dist.locate_file(file))
        if not src.exists():
            continue
        dst = safe_target_path(file)
        if dst is None:
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            if dst.exists():
                continue
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            if dst.exists() and dst.stat().st_size == src.stat().st_size:
                continue
            shutil.copy2(src, dst)
    copied.append(dist.metadata["Name"])

    for dep in iter_runtime_requirements(dist.requires):
        if normalize(dep) not in seen:
            queue.append(dep)

print(f"Copied {len(copied)} distributions into {target}")
for name in sorted(copied, key=str.lower):
    print(f"  - {name}")
'@

$roots = @(
    "popdf", "poexcel", "pofile", "poimage", "poocr", "pomarkdown",
    "poemail", "povideo", "wftools", "poprogress", "pocode", "poppt",
    "poword", "search4file", "loguru"
)

$copyDepsScript | python - $DistLib @roots
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

$copyStdlibScript = @'
import shutil
import sys
import sysconfig
from pathlib import Path

target = Path(sys.argv[1])
stdlib = Path(sysconfig.get_paths()["stdlib"])
dlls = Path(sys.base_prefix) / "DLLs"

skip_dirs = {
    "__pycache__", "site-packages", "idlelib", "tkinter", "turtledemo",
    "ensurepip", "venv", "lib2to3", "distutils", "test", "tests",
}

def should_skip(path: Path) -> bool:
    return any(part in skip_dirs for part in path.parts)

def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and dst.stat().st_size == src.stat().st_size:
        return
    shutil.copy2(src, dst)

count = 0
for src in stdlib.rglob("*"):
    rel = src.relative_to(stdlib)
    if should_skip(rel):
        continue
    if src.is_dir():
        continue
    if src.suffix.lower() not in {".py", ".pyi", ".txt", ".dat", ".pem"}:
        continue
    copy_file(src, target / rel)
    count += 1

if dlls.is_dir():
    for src in dlls.iterdir():
        if src.name.lower().startswith(("_test", "_ctypes_test", "_tkinter")):
            continue
        if src.name.lower() in {"tcl86t.dll", "tk86t.dll"}:
            continue
        if src.is_file() and src.suffix.lower() in {".pyd", ".dll"}:
            copy_file(src, target / src.name)
            count += 1

print(f"Copied Python stdlib runtime files into {target}: {count}")
'@

$copyStdlibScript | python - $DistLib
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

$pruneScript = @'
import shutil
import sys
from pathlib import Path

target = Path(sys.argv[1])
remove_dirs = [
    "site-packages", "__pycache__", "idlelib", "tkinter", "turtledemo",
    "ensurepip", "venv", "lib2to3", "distutils", "test", "tests",
]
remove_file_prefixes = ("_test", "_ctypes_test", "_tkinter")
remove_file_names = {"tcl86t.dll", "tk86t.dll", "pywin32.chm"}
remove_suffixes = {".pyc", ".pyo", ".c", ".cpp", ".h", ".hpp", ".pxd", ".pyx", ".md", ".rst"}

removed = 0
for name in remove_dirs:
    path = target / name
    if path.exists():
        shutil.rmtree(path, ignore_errors=True)
        removed += 1

for path in list(target.rglob("*")):
    if not path.exists():
        continue
    if path.is_dir():
        rel_text = path.relative_to(target).as_posix().lower()
        if path.name.lower() == "__pycache__":
            shutil.rmtree(path, ignore_errors=True)
            removed += 1
            continue
        if rel_text.startswith("pandas/_testing"):
            continue
        if path.name.lower() in {"__pycache__", "test", "tests", "testing", "doc", "docs", "example", "examples", "sample", "samples"}:
            shutil.rmtree(path, ignore_errors=True)
            removed += 1
        continue
    rel_text = path.relative_to(target).as_posix().lower()
    if rel_text == "使用教程.md":
        continue
    if rel_text == "pandas/util/_tester.py" or rel_text.startswith("pandas/_testing/"):
        continue
    name = path.name.lower()
    if name in remove_file_names or name.startswith(remove_file_prefixes) or path.suffix.lower() in remove_suffixes:
        try:
            path.unlink()
            removed += 1
        except OSError:
            pass

print(f"Pruned runtime payload entries: {removed}")
'@

$pruneScript | python - $DistLib
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

$copyUsageGuideScript = @'
import shutil
import sys
from pathlib import Path

root = Path(sys.argv[1])
dist_runtime = Path(sys.argv[2])
name = "\u4f7f\u7528\u6559\u7a0b.md"
source = root / "docs" / name
target = dist_runtime / name
if source.exists():
    shutil.copy2(source, target)
    print(f"Copied usage guide: {target}")
else:
    print(f"[warn] usage guide not found: {source}")
'@

$copyUsageGuideScript | python - $Root $DistRuntime
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
