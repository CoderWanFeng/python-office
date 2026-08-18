# -*- coding: utf-8 -*-
"""python-office 顶层入口。

采用 PEP 562 (3.7+) 的模块级 ``__getattr__`` 实现按需懒加载：
用户 ``import office`` 之后，仅在真正访问 ``office.pdf`` /
``office.excel`` 等子模块时才会触发对应子包 import，避免一次性
拉起全部第三方依赖。

副作用清理:
    不再在 import 阶段自动调用 ``check_compatibility()``。如需检查，
    显式执行 ``from office.compatibility import check_compatibility;
    check_compatibility()``，或运行 ``python -m office.compatibility``。
"""

from __future__ import annotations

import importlib
from types import ModuleType
from typing import Any

__version__ = "1.0.6"

__doc__ = """【python-office库】，功能持续更新中
使用有问题 or 提交你的功能需求 or 参与项目开发
1、项目【官方文档】：https://www.python-office.com
2、请+【项目交流群】：https://www.python4office.cn/wechat-group
3、本开源项目的【源代码】：https://github.com/CoderWanFeng/python-office"""

# 子模块名 -> "office.api.<name>" 的映射。访问 office.pdf 时才会真正 import。
_LAZY_SUBMODULES = {
    "pdf": "office.api.pdf",
    "excel": "office.api.excel",
    "word": "office.api.word",
    "ppt": "office.api.ppt",
    "image": "office.api.image",
    "file": "office.api.file",
    "video": "office.api.video",
    "email": "office.api.email",
    "ocr": "office.api.ocr",
    "markdown": "office.api.markdown",
    "tools": "office.api.tools",
    "wechat": "office.api.wechat",
    "web": "office.api.web",
    "finance": "office.api.finance",
    "testApi": "office.api.testApi",
}

__all__ = sorted(list(_LAZY_SUBMODULES.keys()) + ["__version__"])


def __getattr__(name: str) -> Any:
    if name in _LAZY_SUBMODULES:
        full_name = _LAZY_SUBMODULES[name]
        module = importlib.import_module(full_name)
        globals()[name] = module
        return module
    raise AttributeError(f"module 'office' has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(list(globals().keys()) + list(_LAZY_SUBMODULES.keys()))
