# -*- coding: UTF-8 -*-
"""`po` 命令的输出层：文本模式与 ``--json`` 机器可读模式。

文本模式下只有 api 函数的返回值非 None 才打印；``--json`` 模式下
stdout 只输出一行 JSON，库内部的 print / 进度条由 main 层重定向到
stderr，保证 stdout 可被脚本和 agent 直接解析。
"""

import json
import sys
from pathlib import Path


def _jsonable(value):
    """把任意返回值转换为可 JSON 序列化的结构。"""
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(v) for v in value]
    return str(value)


def emit_result(result, as_json=False, stream=None):
    """输出命令结果。"""
    stream = stream or sys.stdout
    if as_json:
        print(json.dumps({"ok": True, "result": _jsonable(result)}, ensure_ascii=False),
              file=stream)
    elif result is not None:
        print(result, file=stream)


def emit_error(message, as_json=False, stream=None):
    """输出错误信息到 stderr，返回非零退出码供 main 使用。"""
    stream = stream or sys.stderr
    if as_json:
        print(json.dumps({"ok": False, "error": str(message)}, ensure_ascii=False),
              file=stream)
    else:
        print("po: error: %s" % message, file=stream)
    return 1
