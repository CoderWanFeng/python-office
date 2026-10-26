# Command Line Interface

<cite>
**Files referenced in this document**
- [README.md](file://README.md)
- [setup.cfg](file://setup.cfg)
- [office/cli/main.py](file://office/cli/main.py)
- [office/cli/commands.py](file://office/cli/commands.py)
- [office/cli/output.py](file://office/cli/output.py)
- [office/__init__.py](file://office/__init__.py)
- [office/__main__.py](file://office/__main__.py)
</cite>

## Table of Contents

1. [Introduction](#introduction)
2. [Installation and Verification](#installation-and-verification)
3. [Command Structure](#command-structure)
4. [Modules and Subcommands](#modules-and-subcommands)
5. [Parameter Style](#parameter-style)
6. [Machine-Readable JSON Output](#machine-readable-json-output)
7. [Platform Guard](#platform-guard)
8. [CLI and Python Equivalence](#cli-and-python-equivalence)
9. [Architecture](#architecture)
10. [Troubleshooting](#troubleshooting)

## Introduction

Starting with **version 1.1.0**, `python-office` ships a command-line entry point called `po`. Once installed, office automation becomes available directly from the terminal, shell scripts, CI pipelines, or AI agents — no Python code required.

```bash
po pdf merge2pdf a.pdf b.pdf --output-file merged.pdf
po excel excel2pdf report.xlsx report.pdf
po tools url2ip www.python-office.com
```

**Section sources**

- [README.md](file://README.md#L155-L175)

## Installation and Verification

```bash
pip install python-office
```

Verify:

```bash
po --version
# po 1.1.0 (python-office)

po --help
```

The `po` command is registered as a console script entry point in `setup.cfg`:

```ini
[options.entry_points]
console_scripts =
    po = office.cli.main:main
```

`python -m office` is an equivalent entry point provided by `office/__main__.py`, useful in environments where `po` cannot be invoked directly.

**Section sources**

- [setup.cfg](file://setup.cfg#L47-L48)
- [office/__main__.py](file://office/__main__.py#L1-L9)

## Command Structure

Commands follow a two-level "module + subcommand" structure:

```text
po [--json] <module> <command> [positional args] [--options]
```

| Level | Description | Examples |
|---|---|---|
| Module | Corresponds to a module under `office.api` | `pdf`, `excel`, `file`, `image`, `tools`, `markdown`, `finance` |
| Subcommand | Corresponds to a specific function in that API module | `merge2pdf`, `excel2pdf`, `url2ip` |

Each level provides its own help:

```bash
po --help                  # list all modules
po pdf --help              # list all pdf subcommands
po pdf merge2pdf --help    # parameters of a single subcommand
```

**Section sources**

- [office/cli/main.py](file://office/cli/main.py#L76-L97)

## Modules and Subcommands

The first wave covers **7 cross-platform modules, 42 subcommands, and 121 parameters**.

| Module | Subcommands | Capabilities |
|---|---|---|
| `pdf` | 11 | PDF↔docx conversion, PDF to images, txt to PDF, split, merge, encrypt/decrypt, text/image/parameterized watermarks |
| `excel` | 7 | Fake data generation, merge, sheet splitting, merge into one sheet, keyword search, split by column, export to PDF |
| `file` | 8 | Replace in filenames, insert content, add prefix/postfix, export file listing, search by type, group by name, find by name/suffix |
| `image` | 8 | Compression, watermark, cartoonify, download, text to word cloud, pencil sketch, QR code generation and decoding, watermark removal |
| `tools` | 6 | URL to IP, translation, QR code, random password, lottery numbers, article generation |
| `markdown` | 1 | Excel to Markdown |
| `finance` | 1 | Stock T+0 profit calculation |

Full command tree:

```text
po
├── pdf       pdf2docx  pdf2imgs  txt2pdf  split4pdf  merge2pdf
│             del4pdf  encrypt4pdf  decrypt4pdf  add_text_watermark
│             add_img_water  add_watermark_by_parameters
├── excel     fake2excel  merge2excel  sheet2excel  merge2sheet
│             find_excel_data  split_excel_by_column  excel2pdf
├── file      replace4filename  file_name_insert_content
│             file_name_add_prefix  file_name_add_postfix
│             output_file_list_to_excel  search_specify_type_file
│             group_by_name  get_files
├── image     compress_image  add_watermark  img2Cartoon  down4img
│             txt2wordcloud  pencil4img  decode_qrcode  del_watermark
├── tools     url2ip  transtools  qrcodetools  passwordtools
│             lottery8ticket  create_article
├── markdown  excel2markdown
└── finance   t0
```

**Section sources**

- [office/cli/commands.py](file://office/cli/commands.py#L27-L521)

## Parameter Style

### Positional arguments vs options

Registry entries with `positional: True` become positional arguments; the rest appear as `--kebab-case` long options. Python's underscore naming becomes hyphens on the command line:

```bash
po file replace4filename ./dir "old text" --file-rename true --suffix .txt
```

The underlying API signature is `replace4filename(path, del_content, replace_content, dir_rename, file_rename, suffix)`.

### Boolean parameters

Parameters with `type: "bool"` accept `true/false/1/0/yes/no/on/off` and are displayed as `BOOL`:

```bash
po file replace4filename ./dir "old text" --dir-rename false
```

### Required parameters

Missing a `required: True` parameter makes argparse fail with exit code 2:

```bash
po pdf encrypt4pdf in.pdf
# po: error: the following arguments are required: --password
```

**Section sources**

- [office/cli/main.py](file://office/cli/main.py#L35-L73)

## Machine-Readable JSON Output

The `--json` flag makes stdout emit exactly one line of JSON. It is the recommended invocation for scripts, CI, and AI agents.

Success:

```json
{"ok": true, "result": "1.2.3.4"}
```

Failure (exit code 1):

```json
{"ok": false, "error": "FileNotFoundError: [Errno 2] No such file or directory: 'a.pdf'"}
```

### stdout purity

Library internals call `print` for progress bars. The dispatch layer redirects all library output to stderr, so stdout contains only the single JSON line:

```text
stdout:  {"ok": true, "result": null}
stderr:  rows: 100%|██████████| 5/5 ...
```

This boundary has dedicated test coverage (`test_dispatch_json_mode_keeps_stdout_clean_when_library_prints`).

### Exit codes

| Code | Meaning |
|---|---|
| `0` | Success |
| `1` | Runtime error (missing file, missing dependency, …) |
| `2` | Usage error (unknown module, unknown subcommand, missing required argument) |

**Section sources**

- [office/cli/output.py](file://office/cli/output.py#L27-L45)
- [office/cli/main.py](file://office/cli/main.py#L112-L156)

## Platform Guard

The dispatch layer checks platform restrictions **before importing** the target module. Windows-only modules (`poppt`, `poword`, `PyOfficeRobot`, `search4file`) are intercepted on macOS / Linux:

```text
po: error: module 'xxx' is only available on: win32 (current: darwin)
```

All 7 modules registered in the first wave are cross-platform, so their `platforms` field is `None`. Modules not yet included in this wave (`word` / `ppt` / `video` / `web` / `wechat`) simply do not exist yet:

```bash
po ppt ppt2pdf
# po: error: argument <module>: invalid choice: 'ppt' (choose from excel, file, finance, image, markdown, pdf, tools)
```

When the second wave lands, the Windows-only parts will go through the guard — **guard first, import second, so cross-platform calls trigger no import at all.**

**Section sources**

- [office/cli/main.py](file://office/cli/main.py#L112-L122)
- [office/cli/commands.py](file://office/cli/commands.py#L9-L14)

## CLI and Python Equivalence

The CLI is a thin wrapper over `office.api` and modifies no existing module, so all previous Python usage stays exactly the same:

| Command | Python |
|---|---|
| `po pdf merge2pdf a.pdf b.pdf` | `office.pdf.merge2pdf([...])` |
| `po excel excel2pdf in.xlsx out.pdf` | `office.excel.excel2pdf(...)` |
| `po tools url2ip example.com` | `office.tools.url2ip(...)` |

You can also import directly from the Skills system:

```python
from skills.pdf import pdf2docx
from skills.excel import excel_diff
```

**Section sources**

- [office/cli/__init__.py](file://office/cli/__init__.py#L1-L7)

## Architecture

### Declarative registry

`office/cli/commands.py` is a pure-data registry that carries all parameter information. Building the argparse parser imports **no `office.api` module** — the target module is loaded lazily via `importlib.import_module` only at dispatch time.

As a result, building `po --help` has zero dependencies: a user who installed only `popdf` still gets an instant help screen instead of an error about a missing heavy dependency.

Registry entry shape:

```python
"pdf2docx": {
    "help": "Convert PDF to docx",
    "params": [
        {"name": "input_file", "positional": True, "metavar": "PDF",
         "help": "input PDF file"},
        {"name": "output_file", "help": "output docx file"},
    ],
},
```

Adding a command means appending a data entry — no changes to dispatch or parsing logic.

### Signature filtering

At dispatch time, `inspect.signature` filters the arguments down to those the target function actually accepts, so extra fields in the registry never reach the API function as a `TypeError`.

### Guard and lazy-import ordering

```text
parse args → platform guard → lazy import target module → signature filter → call
```

### How lazy loading helps

`office/__init__.py` uses PEP 562 to lazily load 14 API modules on Python ≥ 3.7, so `import office` no longer drags in the whole `po*` dependency tree. This makes CLI startup faster and makes a lightweight core-only install possible.

**Section sources**

- [office/__init__.py](file://office/__init__.py#L7-L57)
- [office/cli/commands.py](file://office/cli/commands.py#L1-L25)
- [office/cli/main.py](file://office/cli/main.py#L112-L132)

## Troubleshooting

### Q1: `po` command not found

Confirm the installation:

```bash
pip show python-office
```

If the install is fine but the command is not on PATH, use the equivalent entry point:

```bash
python -m office --help
```

### Q2: `po --help` reports a missing dependency

`po --help` itself has no dependencies, so a missing-dependency error usually indicates a broken Python environment. Use JSON mode to read the exact message:

```bash
po --json pdf merge2pdf /tmp/nonexistent.pdf
```

### Q3: Problems with Chinese paths or arguments

Quote arguments containing spaces or Chinese characters:

```bash
po pdf merge2pdf "./我的 文件/a.pdf" "./我的 文件/b.pdf"
```

### Q4: Installing only the dependencies the CLI needs

```bash
pip install python-office popdf poexcel poimage pofile wftools pomarkdown
```

The 7 CLI modules depend only on these sublibraries.

### Q5: `result` is `null` in JSON output

Most API functions return nothing, so `null` on success is expected — check that the output file was created.

**Section sources**

- [office/cli/main.py](file://office/cli/main.py#L135-L156)
- [office/cli/output.py](file://office/cli/output.py#L14-L25)
