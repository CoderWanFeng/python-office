# -*- coding: UTF-8 -*-
"""贡献者 Skill 在「安装包环境」下的兜底行为测试。

背景
----
``setup.cfg`` 的 ``packages = find:`` 只收集带 ``__init__.py`` 的目录，因此
``contributors/`` 目录**不随 pip install python-office 一起发布**。各 Skill 的
``__init__.py`` 都用 try/except 兜底：源码仓库里能正常 import，装包后调用时
应给出明确的 ImportError 提示。

历史 Bug
--------
兜底实现最初写成 ``except ImportError as _import_error:`` 并在闭包里
``raise ... from _import_error``。但 Python 3 在 except 块结束后会自动
``del`` 掉 ``as`` 绑定的异常名，导致闭包引用未定义名字，实际抛出的是
``NameError: name '_import_error' is not defined``，而不是预期的 ImportError。

由于该分支只在「contributors 不可用」时触发，源码仓库内的常规测试永远走不到，
因此这里显式模拟该场景做回归覆盖。
"""

import builtins
import importlib
import sys
import unittest
from unittest import mock


# (模块路径, 兜底函数名)
FALLBACK_SKILLS = (
    ("skills.file.batch_rename_by_excel", "batch_rename_by_excel"),
    ("skills.excel.excel_diff", "excel_diff"),
    ("skills.excel.excel_dedupe", "excel_dedupe"),
    ("skills.excel.excel_column_stats", "excel_column_stats"),
    ("skills.excel.excel2json", "excel2json"),
    ("skills.excel.excel2csv", "excel2csv"),
)

_REAL_IMPORT = builtins.__import__


def _import_without_contributors(name, *args, **kwargs):
    """模拟安装包环境：contributors 目录不存在。"""
    if name == "contributors" or name.startswith("contributors."):
        raise ImportError("No module named %r（模拟：contributors 不随包发布）" % name)
    return _REAL_IMPORT(name, *args, **kwargs)


class TestContributorSkillFallback(unittest.TestCase):
    """兜底分支必须抛出 ImportError，而不是 NameError 等意外异常。"""

    def _reload_without_contributors(self, module_path):
        """在 contributors 不可用的前提下重新导入指定模块。"""
        # 清掉缓存，确保走 except 分支
        for key in list(sys.modules):
            if key == module_path or key.startswith(module_path + "."):
                del sys.modules[key]
        with mock.patch("builtins.__import__", _import_without_contributors):
            return importlib.import_module(module_path)

    def test_fallback_raises_importerror(self):
        for module_path, func_name in FALLBACK_SKILLS:
            with self.subTest(skill=func_name):
                module = self._reload_without_contributors(module_path)
                fallback = getattr(module, func_name)
                self.assertTrue(callable(fallback))
                with self.assertRaises(ImportError) as ctx:
                    fallback()
                message = str(ctx.exception)
                self.assertIn("contributors", message)
                self.assertIn("python-office", message)

    def test_fallback_keeps_original_exception_chain(self):
        """兜底异常应保留原始 ImportError 作为 __cause__，便于排查。"""
        for module_path, func_name in FALLBACK_SKILLS:
            with self.subTest(skill=func_name):
                module = self._reload_without_contributors(module_path)
                with self.assertRaises(ImportError) as ctx:
                    getattr(module, func_name)()
                self.assertIsInstance(ctx.exception.__cause__, ImportError)


if __name__ == "__main__":
    unittest.main()
