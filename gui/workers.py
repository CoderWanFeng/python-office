# -*- coding: utf-8 -*-
"""后台任务执行器 + 日志流。

设计要点：
    1. 用 ``QThread`` 把任意 Python 可调用体丢到后台线程运行，
       避免 UI 卡死；
    2. 线程内临时把 ``sys.stdout`` / ``sys.stderr`` 重定向到一个
       ``StringIO``，让子库内部的 ``print`` 输出也能被抓取；
    3. 通过 ``log`` 信号把日志增量发回主线程，避免跨线程直接操作
       QPlainTextEdit；
    4. ``finished`` 信号携带成功 / 失败状态，供主线程切换按钮状态
       与追加 "✓ 完成 / ✗ 失败" 横幅。
"""

from __future__ import annotations

import io
import sys
import traceback
from pathlib import Path
from typing import Any, Callable

from PySide6.QtCore import QObject, QThread, Signal


class _LogEmitter(QObject):
    log = Signal(str)
    finished = Signal(bool, str)  # (success, message)


class StdoutRedirector:
    """上下文管理器：临时把 stdout/stderr 重定向到 ``_buf``。"""

    def __init__(self, buf: io.StringIO):
        self._buf = buf
        self._old_stdout = None
        self._old_stderr = None

    def __enter__(self):
        self._old_stdout, self._old_stderr = sys.stdout, sys.stderr
        sys.stdout = sys.stderr = self._buf
        return self._buf

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout, sys.stderr = self._old_stdout, self._old_stderr


class JobRunner(QThread):
    """后台执行一个零参可调用。"""

    def __init__(self, func: Callable[..., Any], kwargs: dict, parent=None):
        super().__init__(parent)
        self._func = func
        self._kwargs = dict(kwargs)
        # 函数的返回值（run() 后由 result 属性访问）。
        # 注意：金融计算类函数（如 office.api.finance.t0）会返回数值，
        # 这个值原来被丢弃 —— 现在保留下来供主线程显示。
        self.result: Any = None
        # 把 emitter 设为 self 的子对象：JobRunner 销毁时 emitter 自动清理，
        # 避免 "QThread destroyed while thread is still running" 警告。
        self._emitter = _LogEmitter(self)
        self.log = self._emitter.log
        self.job_finished = self._emitter.finished

    def run(self) -> None:
        buf = io.StringIO()
        try:
            with StdoutRedirector(buf):
                # 关键：接收返回值 —— 不再丢弃
                self.result = self._func(**self._kwargs)
            output = buf.getvalue()
            if output.strip():
                self.log.emit(output)
            # 如果函数有非 None 返回值，自动追加到日志（让用户在"运行日志"区能看到结果）
            if self.result is not None:
                self.log.emit(f"✓ 结果：{self.result}")
            self.job_finished.emit(True, "✓ 执行完成")
        except Exception:
            output = buf.getvalue()
            if output.strip():
                self.log.emit(output)
            tb = traceback.format_exc()
            self.log.emit(tb)
            self.job_finished.emit(False, "✗ 执行失败，请查看下方日志")


def make_runner(func: Callable, kwargs: dict) -> JobRunner:
    """工厂函数：构造 JobRunner 实例，避免调用方直接接触 QThread。"""
    return JobRunner(func, kwargs)
