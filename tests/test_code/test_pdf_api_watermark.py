# -*- coding: utf-8 -*-
"""`office.api.pdf` 水印相关函数的回归测试。

背景：``popdf.add_watermark()`` 自 1.0.2 起已被改为零参数的“功能已迁移”提示
函数，真正带参数的实现是 ``popdf.add_text_watermark()``。``office.api.pdf``
此前错误地调用了 ``popdf.add_watermark(input_file=..., ...)``，导致
``office.pdf.add_text_watermark()`` 必然抛出 TypeError。

本测试不依赖真实 popdf：导入被测模块前注入一个记录调用的假 popdf。
"""

import sys
import types
import unittest
import warnings
from unittest import mock


def _install_fake_popdf():
    """注入记录调用的假 popdf 模块，返回其 mock 字典。"""
    calls = {}

    def _record(name):
        def _fn(**kwargs):
            calls[name] = kwargs
            return None
        return _fn

    fake = types.ModuleType("popdf")
    for name in (
        "add_text_watermark",
        "add_watermark",
        "add_img_water",
        "add_watermark_by_parameters",
    ):
        setattr(fake, name, _record(name))
    fake.__path__ = []

    original = sys.modules.get("popdf")
    sys.modules["popdf"] = fake
    return fake, calls, original


class TestPdfApiWatermark(unittest.TestCase):
    """office.api.pdf 的水印接口必须转发到 popdf 的正确函数。"""

    def setUp(self):
        self._fake, self._calls, self._original_popdf = _install_fake_popdf()
        # 重新加载被测模块，确保其绑定的 popdf 是本次注入的假模块
        sys.modules.pop("office.api.pdf", None)
        import office.api.pdf as pdf_api
        self.pdf_api = pdf_api

    def tearDown(self):
        sys.modules.pop("office.api.pdf", None)
        if self._original_popdf is not None:
            sys.modules["popdf"] = self._original_popdf
        else:
            sys.modules.pop("popdf", None)

    def test_add_text_watermark_calls_add_text_watermark(self):
        """add_text_watermark 必须调用 popdf.add_text_watermark，而不是 add_watermark。"""
        self.pdf_api.add_text_watermark(
            input_file="in.pdf",
            point=(10, 20),
            text="hello",
            output_file="out.pdf",
        )

        self.assertIn("add_text_watermark", self._calls)
        self.assertNotIn("add_watermark", self._calls)
        self.assertEqual(self._calls["add_text_watermark"]["input_file"], "in.pdf")
        self.assertEqual(self._calls["add_text_watermark"]["point"], (10, 20))
        self.assertEqual(self._calls["add_text_watermark"]["text"], "hello")
        self.assertEqual(self._calls["add_text_watermark"]["output_file"], "out.pdf")

    def test_add_text_watermark_supplies_default_point(self):
        """point 缺省时必须补上 (x, y)，否则 PyMuPDF 的 insert_text 会失败。"""
        self.pdf_api.add_text_watermark(input_file="in.pdf")

        kwargs = self._calls["add_text_watermark"]
        self.assertIsInstance(kwargs["point"], tuple)
        self.assertEqual(len(kwargs["point"]), 2)
        self.assertEqual(kwargs["output_file"], "./pdf_watermark.pdf")

    def test_add_watermark_is_a_working_alias(self):
        """add_watermark 不得再是空函数：应委托 add_text_watermark 并提示弃用。"""
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            self.pdf_api.add_watermark(input_file="in.pdf", text="legacy")

        self.assertIn("add_text_watermark", self._calls)
        self.assertEqual(self._calls["add_text_watermark"]["text"], "legacy")
        self.assertTrue(any(issubclass(w.category, DeprecationWarning) for w in caught))

    def test_add_mark_delegates_to_add_watermark_by_parameters(self):
        """add_mark 与 add_watermark_by_parameters 实现重复，应统一收敛。"""
        self.pdf_api.add_mark(input_file="in.pdf", mark_str="mark", output_path="/tmp")

        self.assertIn("add_watermark_by_parameters", self._calls)
        kwargs = self._calls["add_watermark_by_parameters"]
        self.assertEqual(kwargs["pdf_file"], "in.pdf")
        self.assertEqual(kwargs["mark_str"], "mark")
        self.assertEqual(kwargs["output_path"], "/tmp")


if __name__ == "__main__":
    unittest.main()
