# -*- coding: UTF-8 -*-
"""Tests for the public ``skills.<category>`` import surface."""

import importlib
import unittest


CATEGORIES = (
    "excel",
    "file",
    "finance",
    "image",
    "markdown",
    "ocr",
    "pdf",
    "ppt",
    "ruiming",
    "tools",
    "video",
    "wechat",
    "word",
)


class TestSkillsImports(unittest.TestCase):
    def test_category_exports_are_importable(self):
        for category in CATEGORIES:
            with self.subTest(category=category):
                module = importlib.import_module(f"skills.{category}")
                self.assertTrue(module.__all__)
                for name in module.__all__:
                    self.assertTrue(
                        callable(getattr(module, name, None)),
                        f"skills.{category}.{name} is not callable",
                    )


if __name__ == "__main__":
    unittest.main()
