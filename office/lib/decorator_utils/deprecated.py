# -*- coding: utf-8 -*-
"""deprecated 参数兼容装饰器。

旧版 python-office 各 API 使用过许多旧参数名（file_path / pdf_path /
out_dir / one_by_one / output / pdf_file / pdf_file_in / pdf_file_out /
mark_str / ...），每个函数里都重复 5~15 行的 DeprecationWarning + 回退
映射，逻辑雷同、容易漏改。

本装饰器把"哪一组旧参数名 -> 新参数名"的映射抽出来，重复模式收敛到一处，
调用方只需要声明映射，函数体保持原本的转发逻辑。

使用示例::

    from office.lib.decorator_utils import deprecated_params

    @deprecated_params({
        'file_path': 'input_file',
        'out_dir': 'output_file',
    })
    def pdf2imgs(input_file=None, output_file=None, file_path=None,
                 out_dir=None, merge=False):
        ...

调用 ``pdf2imgs(file_path='a.pdf')`` 时会自动发出 DeprecationWarning
并把 ``file_path`` 的值映射到 ``input_file``。
"""

from __future__ import annotations

import warnings
from functools import wraps
from typing import Callable, Mapping


def deprecated_params(mapping: Mapping[str, str]) -> Callable:
    """装饰器：把一组"旧参数名 -> 新参数名"映射集中处理。

    Args:
        mapping: 旧参数名 -> 新参数名 的字典。仅当调用方传入了旧参数
            且新参数未传入时触发回退；同时会发出 DeprecationWarning，
            stacklevel=2 让警告指向调用方而非装饰器内部。

    Returns:
        Callable: 装饰后的函数，签名不变。
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for old, new in mapping.items():
                if old in kwargs and kwargs[old] is not None:
                    warnings.warn(
                        f"参数 '{old}' 已被弃用，将在后续版本中移除。"
                        f"请改用 '{new}'。",
                        DeprecationWarning,
                        stacklevel=2,
                    )
                    if new not in kwargs or kwargs[new] is None:
                        kwargs[new] = kwargs.pop(old)
                    else:
                        kwargs.pop(old)
            return func(*args, **kwargs)

        return wrapper

    return decorator


__all__ = ["deprecated_params"]
