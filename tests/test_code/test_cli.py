# -*- coding: UTF-8 -*-
"""`po` 命令行（office/cli）的测试。

本文件自包含：在 import office 之前为全部 ``po*`` 依赖安装轻量 stub，
使测试无需真实安装 popdf/poexcel/wftools 等重型依赖即可运行。

运行::

    pytest tests/test_code/test_cli.py -v
"""

import argparse
import copy
import json
import runpy
import sys
import types
from unittest import mock

import pytest


# ---------------------------------------------------------------------------
# 1. 为 office 的直接依赖安装 stub（必须在 import office 之前）
# ---------------------------------------------------------------------------
def _install_stub(name):
    if name in sys.modules:
        return sys.modules[name]
    module = types.ModuleType(name)
    module.__path__ = []
    module.__getattr__ = lambda attr, _name=name: mock.MagicMock(name="%s.%s" % (_name, attr))
    sys.modules[name] = module
    return module


for _name in (
    "popdf", "poexcel", "poimage", "pofile", "wftools", "povideo", "poprogress",
    "poocr", "pocode", "pocode.api", "pocode.api.color", "poemail", "pospider",
    "pomarkdown", "poword", "poppt", "PyOfficeRobot", "search4file", "akshare",
    "moviepy",
):
    _install_stub(_name)

# stub 就位后才能导入被测代码（触发 office/__init__.py 的全量 api 导入）
from office.cli import commands, output  # noqa: E402
from office.cli.main import CliError, build_parser, dispatch, main  # noqa: E402


# ---------------------------------------------------------------------------
# 2. office 包懒加载回归（import office 不得拖入任何 po* 依赖）
# ---------------------------------------------------------------------------
import os  # noqa: E402
import subprocess  # noqa: E402


def test_office_import_is_lazy():
    code = (
        "import sys, office\n"
        "po = [m for m in sys.modules if m.split('.')[0] in "
        "('popdf','poexcel','poimage','pofile','wftools','pocode',"
        "'povideo','poocr','poemail','pospider')]\n"
        "assert not po, po\n"
        "try:\n"
        "    office.nope\n"
        "    raise SystemExit('no AttributeError for office.nope')\n"
        "except AttributeError:\n"
        "    pass\n"
    )
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    result = subprocess.run([sys.executable, "-c", code], cwd=repo_root,
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


# ---------------------------------------------------------------------------
# 3. 注册表完整性
# ---------------------------------------------------------------------------
def test_registry_modules_point_to_public_api():
    for name, module in commands.MODULES.items():
        assert module["module"].startswith("office.api."), name
        assert module["commands"], "module %s has no commands" % name
        platforms = module.get("platforms")
        assert platforms is None or (
            isinstance(platforms, list) and platforms and
            all(isinstance(p, str) for p in platforms)), name


def test_registry_params_are_wellformed():
    for module_name, module in commands.MODULES.items():
        for command_name, command in module["commands"].items():
            seen = set()
            for param in command["params"]:
                assert set(param) <= {
                    "name", "positional", "flag", "type", "nargs",
                    "default", "choices", "required", "help", "metavar",
                }, (module_name, command_name, param)
                name = param["name"]
                assert name.isidentifier(), (module_name, command_name, name)
                assert name not in seen, "duplicate param %s" % name
                seen.add(name)
                if param.get("flag"):
                    assert not param.get("positional")
                    assert "default" not in param
                if "type" in param:
                    assert callable(param["type"]) or param["type"] == "bool", \
                        (module_name, command_name, name)


def test_registry_covers_core_modules():
    # 第一波 7 个跨平台核心模块 + 第二波逐步加入的 Windows-only 模块
    # word 是第二波加入的，依赖 poword（仅 Windows）
    assert set(commands.MODULES) == {
        "pdf", "excel", "tools", "image", "file", "markdown", "finance", "word",
    }
    total = sum(len(m["commands"]) for m in commands.MODULES.values())
    assert total == 47  # 42 (first wave) + 5 (word)


def test_registry_core_modules_are_cross_platform():
    # 第一波 7 个核心模块必须是跨平台的
    core = {"pdf", "excel", "tools", "image", "file", "markdown", "finance"}
    for name in core:
        assert commands.MODULES[name]["platforms"] is None, name


def test_registry_word_is_windows_only():
    word = commands.MODULES["word"]
    assert word["platforms"] == ["win32"]
    assert set(word["commands"]) == {
        "docx2pdf", "merge4docx", "doc2docx", "docx2doc", "docx4imgs",
    }


# ---------------------------------------------------------------------------
# 4. 解析器：--help 冒烟 + 参数解析抽查
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("module_name", sorted(commands.MODULES))
@pytest.mark.parametrize("help_level", ["module", "command"])
def test_help_smoke(module_name, help_level, capsys):
    parser = build_parser()
    if help_level == "module":
        argv = [module_name, "--help"]
    else:
        command_name = sorted(commands.MODULES[module_name]["commands"])[0]
        argv = [module_name, command_name, "--help"]
    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(argv)
    assert excinfo.value.code == 0
    out = capsys.readouterr().out
    assert module_name in out


def test_parse_merge2pdf_positionals_and_default():
    args = build_parser().parse_args(
        ["pdf", "merge2pdf", "a.pdf", "b.pdf"])
    assert args.input_file_list == ["a.pdf", "b.pdf"]
    assert args.output_file == "merged.pdf"
    assert args.module == "pdf" and args.command == "merge2pdf"


def test_parse_split4pdf_types():
    args = build_parser().parse_args(
        ["pdf", "split4pdf", "x.pdf", "--from-page", "1", "--to-page", "3"])
    assert args.input_file == "x.pdf"
    assert args.from_page == 1 and args.to_page == 3


def test_parse_pdf2imgs_flag():
    off = build_parser().parse_args(["pdf", "pdf2imgs", "x.pdf"])
    on = build_parser().parse_args(["pdf", "pdf2imgs", "x.pdf", "--merge"])
    assert off.merge is False and on.merge is True


def test_parse_del4pdf_requires_page_nums():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["pdf", "del4pdf", "x.pdf"])
    args = build_parser().parse_args(
        ["pdf", "del4pdf", "x.pdf", "--page-nums", "0", "2"])
    assert args.page_nums == [0, 2]


def test_parse_fake2excel_defaults_and_options():
    default = build_parser().parse_args(["excel", "fake2excel"])
    assert default.columns == ["name"] and default.rows == 1
    assert default.language == "zh_CN"
    custom = build_parser().parse_args(
        ["excel", "fake2excel", "--columns", "name", "age", "--rows", "5",
         "--language", "english"])
    assert custom.columns == ["name", "age"] and custom.rows == 5
    assert custom.language == "english"


def test_parse_language_choices_rejected():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["excel", "fake2excel", "--language", "xx"])


def test_parse_excel2pdf_two_positionals():
    args = build_parser().parse_args(
        ["excel", "excel2pdf", "a.xlsx", "b.pdf", "--sheet-id", "2"])
    assert (args.excel_path, args.pdf_path, args.sheet_id) == ("a.xlsx", "b.pdf", 2)


def test_parse_tools_commands():
    args = build_parser().parse_args(["tools", "passwordtools", "--len", "12"])
    assert args.len == 12
    args = build_parser().parse_args(
        ["tools", "transtools", "english", "你好", "--from-lang", "zh"])
    assert (args.to_lang, args.content, args.from_lang) == ("english", "你好", "zh")


# ---------------------------------------------------------------------------
# 5. 分发：经 stub 依赖直达 office.api → po* 层
# ---------------------------------------------------------------------------
def _configure_wftools(**attrs):
    wftools = sys.modules["wftools"]
    for key, value in attrs.items():
        setattr(wftools, key, value)
    return wftools


def test_dispatch_url2ip_text_mode(capsys):
    _configure_wftools(url2ip=lambda url: "93.184.216.34")
    code = main(["tools", "url2ip", "example.com"])
    assert code == 0
    assert "93.184.216.34" in capsys.readouterr().out


def test_dispatch_url2ip_json_mode(capsys):
    _configure_wftools(url2ip=lambda url: "93.184.216.34")
    code = main(["--json", "tools", "url2ip", "example.com"])
    assert code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload == {"ok": True, "result": "93.184.216.34"}


def test_dispatch_json_mode_keeps_stdout_clean_when_library_prints(capsys):
    def noisy_url2ip(url):
        print("progress: 50%")  # 模拟库内部的进度输出
        return "1.1.1.1"

    _configure_wftools(url2ip=noisy_url2ip)
    code = main(["--json", "tools", "url2ip", "example.com"])
    captured = capsys.readouterr()
    assert code == 0
    assert json.loads(captured.out) == {"ok": True, "result": "1.1.1.1"}
    assert "progress" in captured.err  # 库的输出被重定向到 stderr


def test_dispatch_merge2pdf_delegates_to_popdf(capsys):
    popdf = sys.modules["popdf"]
    popdf.merge2pdf = mock.MagicMock(return_value=None)
    code = main(["pdf", "merge2pdf", "a.pdf", "b.pdf"])
    assert code == 0
    popdf.merge2pdf.assert_called_once_with(
        input_file_list=["a.pdf", "b.pdf"], output_file="merged.pdf")
    assert capsys.readouterr().out == ""  # 返回 None 时文本模式不输出


def test_dispatch_runtime_error_text_mode(capsys):
    _configure_wftools(url2ip=mock.MagicMock(side_effect=ValueError("boom")))
    code = main(["tools", "url2ip", "example.com"])
    assert code == 1
    captured = capsys.readouterr()
    assert "ValueError" in captured.err and "boom" in captured.err
    assert captured.out == ""


def test_dispatch_runtime_error_json_mode(capsys):
    _configure_wftools(url2ip=mock.MagicMock(side_effect=ValueError("boom")))
    code = main(["--json", "tools", "url2ip", "example.com"])
    assert code == 1
    captured = capsys.readouterr()
    assert json.loads(captured.err) == {"ok": False, "error": "ValueError: boom"}
    assert captured.out == ""


# ---------------------------------------------------------------------------
# 5. 平台守卫
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# 6. 输出层
# ---------------------------------------------------------------------------
def test_jsonable_handles_common_types():
    from pathlib import Path

    value = output._jsonable({"path": Path("/tmp/a"), "items": (1, "x"),
                              "flag": True, "none": None, "obj": object()})
    assert value["path"] == "/tmp/a"
    assert value["items"] == [1, "x"]
    assert value["flag"] is True and value["none"] is None
    assert isinstance(value["obj"], str)


def test_emit_result_text_mode_silent_on_none(capsys):
    output.emit_result(None, as_json=False)
    assert capsys.readouterr().out == ""
    output.emit_result("hello", as_json=False)
    assert capsys.readouterr().out == "hello\n"


def test_emit_result_json_mode_always_one_line(capsys):
    output.emit_result(None, as_json=True)
    assert json.loads(capsys.readouterr().out) == {"ok": True, "result": None}
    output.emit_result("你好", as_json=True)
    assert json.loads(capsys.readouterr().out) == {"ok": True, "result": "你好"}


def test_emit_error_returns_nonzero(capsys):
    assert output.emit_error("bad thing", as_json=False) == 1
    assert "po: error: bad thing" in capsys.readouterr().err
