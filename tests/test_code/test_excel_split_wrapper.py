"""Tests for the Excel split-by-column API wrapper."""

import importlib.util
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace
import unittest
from unittest.mock import Mock, patch


def load_excel_api(poexcel):
    module_path = Path(__file__).resolve().parents[2] / "office" / "api" / "excel.py"
    spec = importlib.util.spec_from_file_location("excel_api_under_test", module_path)
    module = importlib.util.module_from_spec(spec)

    with patch.dict(sys.modules, {"poexcel": poexcel}):
        spec.loader.exec_module(module)

    return module


class TestExcelSplitWrapper(unittest.TestCase):
    def test_delegates_to_poexcel_when_export_is_available(self):
        split_excel = Mock()
        excel = load_excel_api(
            SimpleNamespace(split_excel_by_column=split_excel)
        )

        excel.split_excel_by_column(
            filepath="orders.xlsx",
            column=2,
            worksheet_name="Orders",
        )

        split_excel.assert_called_once_with(
            filepath="orders.xlsx",
            column=2,
            worksheet_name="Orders",
        )

    def test_falls_back_to_bundled_implementation_when_export_is_missing(self):
        split_excel = Mock()
        split_module = ModuleType("office.lib.excel.SplitExcel")
        split_module.split_excel_by_column = split_excel

        modules = {
            "office": ModuleType("office"),
            "office.lib": ModuleType("office.lib"),
            "office.lib.excel": ModuleType("office.lib.excel"),
            "office.lib.excel.SplitExcel": split_module,
        }
        excel = load_excel_api(SimpleNamespace())

        with patch.dict(sys.modules, modules):
            excel.split_excel_by_column(
                filepath="orders.xlsx",
                column=2,
                worksheet_name="Orders",
            )

        split_excel.assert_called_once_with(
            filepath="orders.xlsx",
            column=2,
            worksheet_name="Orders",
        )


if __name__ == "__main__":
    unittest.main()
