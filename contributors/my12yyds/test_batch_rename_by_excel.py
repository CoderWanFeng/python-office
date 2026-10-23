# -*- coding: UTF-8 -*-
"""batch_rename_by_excel 的单元测试。

运行方式（在仓库根目录）：
    pytest contributors/my12yyds/test_batch_rename_by_excel.py -v
"""

import importlib.util
import os
from pathlib import Path
import tempfile
import unittest

import openpyxl


def _load_module():
    """按文件路径加载同目录下的 batch_rename_by_excel 模块。"""
    module_path = Path(__file__).resolve().parent / "batch_rename_by_excel.py"
    spec = importlib.util.spec_from_file_location("batch_rename_by_excel_under_test", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


batch_rename_by_excel = _load_module().batch_rename_by_excel


def _make_excel(path, rows, header=("原文件名", "新文件名")):
    """生成一个用于测试的映射 Excel 文件。"""
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(list(header))
    for old_name, new_name in rows:
        worksheet.append([old_name, new_name])
    workbook.save(path)
    return path


class TestBatchRenameByExcel(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.folder = self.tmp / "files"
        self.folder.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def _touch(self, *names):
        for name in names:
            (self.folder / name).write_text("x", encoding="utf-8")

    def test_renames_files_following_the_mapping(self):
        self._touch("a.txt", "b.txt")
        excel = _make_excel(self.tmp / "map.xlsx", [("a.txt", "报告.txt"), ("b.txt", "汇总.txt")])

        result = batch_rename_by_excel(str(excel), str(self.folder))

        self.assertEqual(
            sorted(result["renamed"]),
            [("a.txt", "报告.txt"), ("b.txt", "汇总.txt")],
        )
        self.assertTrue((self.folder / "报告.txt").exists())
        self.assertTrue((self.folder / "汇总.txt").exists())
        self.assertFalse((self.folder / "a.txt").exists())

    def test_dry_run_does_not_touch_files(self):
        self._touch("a.txt")
        excel = _make_excel(self.tmp / "map.xlsx", [("a.txt", "b.txt")])

        result = batch_rename_by_excel(str(excel), str(self.folder), dry_run=True)

        self.assertEqual(result["renamed"], [("a.txt", "b.txt")])
        self.assertTrue((self.folder / "a.txt").exists())
        self.assertFalse((self.folder / "b.txt").exists())

    def test_missing_source_file_is_reported(self):
        self._touch("a.txt")
        excel = _make_excel(self.tmp / "map.xlsx", [("a.txt", "b.txt"), ("不存在.txt", "c.txt")])

        result = batch_rename_by_excel(str(excel), str(self.folder))

        self.assertEqual(result["renamed"], [("a.txt", "b.txt")])
        self.assertEqual(result["missing"], ["不存在.txt"])

    def test_existing_target_is_skipped_to_avoid_overwrite(self):
        self._touch("a.txt", "b.txt")
        excel = _make_excel(self.tmp / "map.xlsx", [("a.txt", "b.txt")])

        result = batch_rename_by_excel(str(excel), str(self.folder))

        self.assertEqual(result["renamed"], [])
        self.assertEqual(result["conflicts"], ["a.txt"])
        self.assertEqual((self.folder / "b.txt").read_text(encoding="utf-8"), "x")

    def test_blank_and_identical_rows_are_skipped(self):
        self._touch("a.txt")
        excel = _make_excel(
            self.tmp / "map.xlsx",
            [("a.txt", ""), ("a.txt", "a.txt")],
        )

        result = batch_rename_by_excel(str(excel), str(self.folder))

        self.assertEqual(result["renamed"], [])
        self.assertEqual(len(result["skipped"]), 2)

    def test_custom_column_names(self):
        self._touch("a.txt")
        excel = _make_excel(
            self.tmp / "map.xlsx",
            [("a.txt", "b.txt")],
            header=("old", "new"),
        )

        result = batch_rename_by_excel(
            str(excel),
            str(self.folder),
            old_name_column="old",
            new_name_column="new",
        )

        self.assertEqual(result["renamed"], [("a.txt", "b.txt")])

    def test_missing_column_raises_value_error(self):
        excel = _make_excel(self.tmp / "map.xlsx", [], header=("旧的", "新的"))

        with self.assertRaises(ValueError):
            batch_rename_by_excel(str(excel), str(self.folder))

    def test_missing_excel_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            batch_rename_by_excel(str(self.tmp / "nope.xlsx"), str(self.folder))


if __name__ == "__main__":
    unittest.main()
