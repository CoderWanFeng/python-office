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
# 2. 注册表完整性
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


def test_registry_covers_all_modules():
    assert set(commands.MODULES) == {
        "pdf", "excel", "tools", "image", "file", "markdown", "finance",
        "video", "web", "word", "ppt", "wechat",
    }
    total = sum(len(m["commands"]) for m in commands.MODULES.values())
    assert total == 62


def test_registry_windows_only_modules_are_guared():
    for name in ("word", "ppt", "wechat"):
        assert commands.MODULES[name]["platforms"] == ["win32"], name
    for name in ("pdf", "excel", "tools", "image", "file", "markdown",
                 "finance", "video", "web"):
        assert commands.MODULES[name]["platforms"] is None, name


# ---------------------------------------------------------------------------
# 3. 解析器：--help 冒烟 + 参数解析抽查
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
# 4. 分发：经 stub 依赖直达 office.api → po* 层
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
@pytest.mark.skipif(sys.platform == "win32", reason="guards non-Windows behaviour")
def test_platform_guard_blocks_windows_only_module(capsys):
    registry = copy.deepcopy(commands.MODULES)
    registry["wechat"] = {
        "module": "office.api.wechat",
        "help": "WeChat robot (Windows only)",
        "platforms": ["win32"],
        "commands": {"send": {"help": "send message", "params": []}},
    }
    code = main(["wechat", "send"], registry=registry)
    assert code == 1
    err = capsys.readouterr().err
    assert "wechat" in err and "win32" in err


def test_platform_guard_allows_all_by_default():
    registry = copy.deepcopy(commands.MODULES)
    assert registry["tools"]["platforms"] is None  # 默认全平台，不触发守卫
    parser = build_parser(registry)
    args = parser.parse_args(["tools", "url2ip", "x"])
    assert args.url == "x"


# ---------------------------------------------------------------------------
# 6. 顶层行为：--version / 缺参 / python -m office
# ---------------------------------------------------------------------------
def test_version_flag(capsys):
    assert main(["--version"]) == 0
    out = capsys.readouterr().out
    assert out.startswith("po ") and "python-office" in out


def test_no_module_shows_help(capsys):
    assert main([]) == 2
    assert "usage" in capsys.readouterr().err.lower()


def test_unknown_command_is_usage_error(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(["pdf", "no-such-command"])
    assert excinfo.value.code == 2


def test_python_m_office_alias(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["office", "--version"])
    with pytest.raises(SystemExit) as excinfo:
        runpy.run_module("office", run_name="__main__")
    assert excinfo.value.code == 0
    assert capsys.readouterr().out.startswith("po ")


# ---------------------------------------------------------------------------
# 6b. 第二批模块（image/file/markdown/finance/video/web/word/ppt/wechat）
# ---------------------------------------------------------------------------
def test_parse_image_commands():
    parser = build_parser()
    args = parser.parse_args(
        ["image", "add_watermark", "a.jpg", "@python-office",
         "--opacity", "0.8", "--angle", "45"])
    assert (args.file, args.mark) == ("a.jpg", "@python-office")
    assert args.opacity == 0.8 and args.angle == 45
    assert args.color == "#eaeaea" and args.size == 30
    args = parser.parse_args(
        ["image", "compress_image", "big.jpg", "--output-file", "small.jpg",
         "--quality", "30"])
    assert args.output_file == "small.jpg" and args.quality == 30
    args = parser.parse_args(["image", "decode_qrcode", "q.png"])
    assert args.qrcode_path == "q.png"


def test_parse_file_replace4filename_bool_options():
    parser = build_parser()
    args = parser.parse_args(
        ["file", "replace4filename", "./docs", "副本", "--dir-rename", "false"])
    assert args.dir_rename is False      # api 默认 True，可用 --dir-rename false 关闭
    assert args.file_rename is True
    assert args.replace_content == ""
    args = parser.parse_args(
        ["file", "replace4filename", "./docs", "副本", "--suffix", ".pdf"])
    assert args.suffix == ".pdf"
    with pytest.raises(SystemExit):      # 非法布尔值报 usage error
        parser.parse_args(
            ["file", "replace4filename", "./docs", "副本", "--dir-rename", "maybe"])


def test_parse_file_get_files():
    args = build_parser().parse_args(
        ["file", "get_files", "./data", "--name", "报表", "--suffix", ".xlsx",
         "--sub", "--level", "2"])
    assert (args.name, args.suffix, args.sub, args.level) == ("报表", ".xlsx", True, 2)
    default = build_parser().parse_args(["file", "get_files", "./data"])
    assert default.sub is False and default.level == 0


def test_parse_finance_t0():
    args = build_parser().parse_args(["finance", "t0", "10.5", "11.2", "200"])
    assert (args.buy_price, args.sale_price, args.shares) == (10.5, 11.2, 200)
    assert args.w_rate == pytest.approx(2.5 / 10000)
    assert args.min_rate == pytest.approx(5)
    assert args.stamp_tax == pytest.approx(1 / 1000)


def test_parse_video_and_web():
    args = build_parser().parse_args(["video", "txt2mp3", "你好世界"])
    assert args.content == "你好世界" and args.speak is True
    args = build_parser().parse_args(
        ["video", "txt2mp3", "你好", "--speak", "false"])
    assert args.speak is False
    args = build_parser().parse_args(
        ["web", "url2ebook", "https://example.com", "My Book"])
    assert (args.url, args.tile) == ("https://example.com", "My Book")


def test_parse_windows_only_commands_parse_on_any_platform():
    args = build_parser().parse_args(
        ["word", "docx2pdf", "a.docx", "--output-path", "./out"])
    assert args.path == "a.docx" and args.output_path == "./out"
    args = build_parser().parse_args(["wechat", "send_message", "晚枫", "你好"])
    assert (args.who, args.message) == ("晚枫", "你好")
    args = build_parser().parse_args(["ppt", "merge4ppt", "./ppts"])
    assert args.output_name == "merge4ppt.pptx"


def test_dispatch_finance_t0_real_computation(capsys):
    # finance.t0 是纯标准库实现，可真实计算，无需 stub
    code = main(["--json", "finance", "t0", "10", "11", "100"])
    assert code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["ok"] is True
    # t0 实际返回 Decimal，JSON 序列化为数字字符串
    assert float(payload["result"]) == pytest.approx(88.9, abs=0.01)


def test_dispatch_image_decode_qrcode_via_stub(capsys):
    sys.modules["poimage"].decode_qrcode = mock.MagicMock(return_value=None)
    code = main(["--json", "image", "decode_qrcode", "q.png"])
    assert code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload == {"ok": True, "result": None}
    sys.modules["poimage"].decode_qrcode.assert_called_once_with(qrcode_path="q.png")


@pytest.mark.skipif(sys.platform == "win32", reason="guards non-Windows behaviour")
@pytest.mark.parametrize("argv", [
    ["word", "docx2pdf", "a.docx"],
    ["ppt", "ppt2pdf", "a.pptx"],
    ["wechat", "send_message", "晚枫", "你好"],
])
def test_platform_guard_blocks_real_windows_modules(argv, capsys):
    assert main(argv) == 1
    err = capsys.readouterr().err
    assert "only available on" in err
    assert "win32" in err


# ---------------------------------------------------------------------------
# 7. 输出层
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
