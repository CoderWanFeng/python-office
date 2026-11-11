# -*- coding: UTF-8 -*-
"""`finance_t0_fix` 与 `split_excel_fix` 的单元测试。

每个用例都对应上游 `office.api.finance.t0` / `office.lib.excel.SplitExcel`
中的一个具体缺陷，失败即为回归。
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import xlrd
import xlwt
import openpyxl

from finance_t0_fix import RATE_LINE, t0, t0_safe
from split_excel_fix import (
    build_split_path,
    process_xls,
    process_xlsx,
    split_excel_by_column,
    validate_column,
)

ROWS = [("h1", "h2", "h3"), ("a", "1", "X"), ("b", "2", "Y"), ("c", "3", "X")]


class TestFinanceT0Fix(unittest.TestCase):
    """对应上游缺陷：min_rate 未做 Decimal 规范化；返回值是 Decimal 而非 float。"""

    def test_accepts_float_min_rate(self):
        """传 float 型 min_rate 不应抛 TypeError（上游此调用必崩）。"""
        result = t0(11.99, 12.26, 700, min_rate=5.0)

        self.assertAlmostEqual(170.418, result, places=5)

    def test_accepts_int_min_rate(self):
        result = t0(11.99, 12.26, 700, min_rate=5)

        self.assertAlmostEqual(170.418, result, places=5)

    def test_returns_float_not_decimal(self):
        """返回值类型必须与 -> float 标注一致。"""
        result = t0(11.99, 12.26, 700)

        self.assertIsInstance(result, float)

    def test_result_is_json_serializable(self):
        """Decimal 无法 json 序列化，float 可以。"""
        payload = json.dumps({"profit": t0(11.99, 12.26, 700)})

        self.assertAlmostEqual(170.418, json.loads(payload)["profit"], places=5)

    def test_large_trade_uses_proportional_commission(self):
        """买入金额超过 RATE_LINE 时按比例计佣。"""
        result = t0(100, 110, 700)

        self.assertAlmostEqual(6886.25, result, places=5)
        self.assertGreater(100 * 700, RATE_LINE)

    def test_custom_commission_rate(self):
        result = t0(100, 110, 700, w_rate=1 / 10000)

        self.assertAlmostEqual(6908.3, result, places=5)

    def test_negative_shares_raises_value_error(self):
        with self.assertRaises(ValueError):
            t0(11.99, 12.26, -1)

    def test_t0_safe_returns_none_on_bad_input(self):
        """容错包装遇到脏数据返回 None，不抛异常。"""
        self.assertIsNone(t0_safe("不是数字", 12.26, 700))

    def test_t0_safe_returns_value_on_good_input(self):
        self.assertAlmostEqual(170.418, t0_safe(11.99, 12.26, 700), places=5)


class TestSplitOutputPath(unittest.TestCase):
    """对应上游缺陷 1：filepath.replace('.xls', ...) 会破坏含 .xls 的目录名。"""

    def test_directory_containing_dot_xls_is_preserved(self):
        path = os.path.join("data", "archive.xls.v2", "demo.xls")

        result = build_split_path(path)

        self.assertIn("archive.xls.v2", result)
        self.assertNotIn("archive_Split", result)
        self.assertTrue(result.endswith(".xls"))

    def test_directory_containing_dot_xlsx_is_preserved(self):
        path = os.path.join("data", "book.xlsx.old", "demo.xlsx")

        result = build_split_path(path)

        self.assertIn("book.xlsx.old", result)
        self.assertNotIn("book_Split", result)

    def test_output_name_keeps_stem_and_extension(self):
        result = build_split_path(os.path.join("d", "report.xlsx"))

        self.assertTrue(os.path.basename(result).startswith("report_Split_"))
        self.assertTrue(result.endswith(".xlsx"))


class TestColumnValidation(unittest.TestCase):
    """对应上游缺陷 3 与 4：列号越界抛 IndexError；column=0 静默拆错列。"""

    def test_zero_column_is_rejected(self):
        self.assertIn("从1开始", validate_column(0, 3))

    def test_negative_column_is_rejected(self):
        self.assertIn("从1开始", validate_column(-1, 3))

    def test_column_beyond_max_is_rejected(self):
        self.assertIn("最大列数是3", validate_column(99, 3))

    def test_valid_column_passes(self):
        for column in (1, 2, 3):
            with self.subTest(column=column):
                self.assertEqual('', validate_column(column, 3))


class SplitExcelEndToEndTest(unittest.TestCase):
    """端到端：真实读写 .xls / .xlsx，验证修复后行为。"""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = self._tmp.name
        self.xls = os.path.join(self.tmp, "demo.xls")
        self.xlsx = os.path.join(self.tmp, "demo.xlsx")
        self._write_xls(self.xls)
        self._write_xlsx(self.xlsx)

    @staticmethod
    def _write_xls(path):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("S1")
        for row_index, row in enumerate(ROWS):
            for col_index, value in enumerate(row):
                worksheet.write(row_index, col_index, value)
        workbook.save(path)

    @staticmethod
    def _write_xlsx(path):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        for row in ROWS:
            worksheet.append(list(row))
        workbook.save(path)

    def _splits_in(self, directory):
        return sorted(n for n in os.listdir(directory) if "_Split_" in n)

    def test_xls_split_succeeds_when_dir_contains_dot_xls(self):
        """上游此处抛 FileNotFoundError。"""
        sub = os.path.join(self.tmp, "archive.xls.v2")
        os.makedirs(sub)
        source = os.path.join(sub, "demo.xls")
        self._write_xls(source)

        split_excel_by_column(source, 1)

        produced = self._splits_in(sub)
        self.assertEqual(1, len(produced))
        self.assertTrue(produced[0].startswith("demo_Split_"))

    def test_xlsx_split_succeeds_when_dir_contains_dot_xlsx(self):
        sub = os.path.join(self.tmp, "book.xlsx.old")
        os.makedirs(sub)
        source = os.path.join(sub, "demo.xlsx")
        self._write_xlsx(source)

        split_excel_by_column(source, 1)

        self.assertEqual(1, len(self._splits_in(sub)))

    def test_xls_bad_sheet_name_returns_message(self):
        """对应上游缺陷 2：上游抛 XLRDError。"""
        message = process_xls(self.xls, 1, "Nope")

        self.assertIn("异常", message)

    def test_xls_column_beyond_max_returns_message(self):
        """对应上游缺陷 3：上游抛 IndexError。"""
        self.assertIn("最大列数是", process_xls(self.xls, 99))

    def test_xls_column_zero_returns_message(self):
        """对应上游缺陷 4：上游会静默按最后一列拆分。"""
        self.assertIn("从1开始", process_xls(self.xls, 0))

    def test_xlsx_column_zero_returns_message(self):
        self.assertIn("从1开始", process_xlsx(self.xlsx, 0))

    def test_xls_column_one_groups_by_first_column(self):
        process_xls(self.xls, 1)
        produced = self._splits_in(self.tmp)
        names = xlrd.open_workbook(os.path.join(self.tmp, produced[-1])).sheet_names()

        self.assertEqual(["h1", "a", "b", "c"], names)

    def test_xls_column_three_groups_by_third_column(self):
        process_xls(self.xls, 3)
        produced = self._splits_in(self.tmp)
        names = xlrd.open_workbook(os.path.join(self.tmp, produced[-1])).sheet_names()

        self.assertEqual(["h3", "X", "Y"], names)

    def test_missing_file_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            split_excel_by_column(os.path.join(self.tmp, "nope.xlsx"), 1)

    def test_unsupported_extension_returns_message(self):
        """不支持的扩展名：文件存在时返回提示，而不是静默什么都不做。"""
        path = os.path.join(self.tmp, "a.csv")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write("h1,h2\n")

        message = split_excel_by_column(path, 1)

        self.assertIn("文件格式不对", message)


if __name__ == "__main__":
    unittest.main(verbosity=2)
