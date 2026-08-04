"""Tests for PDF watermark service imports."""

import importlib.util
from pathlib import Path
import sys
import types
import unittest


class TestPdfAddWatermarkImports(unittest.TestCase):
    def setUp(self):
        self._module_names = (
            "PyPDF2",
            "reportlab",
            "reportlab.pdfgen",
            "reportlab.pdfbase",
            "reportlab.pdfbase.ttfonts",
            "reportlab.pdfbase.pdfmetrics",
            "tqdm",
            "pdf_add_watermark_service_test",
        )
        self._original_modules = {name: sys.modules.get(name) for name in self._module_names}

        pypdf2 = types.ModuleType("PyPDF2")
        pypdf2.PdfReader = type("PdfReader", (), {})
        pypdf2.PdfWriter = type("PdfWriter", (), {})
        sys.modules["PyPDF2"] = pypdf2

        reportlab = types.ModuleType("reportlab")
        pdfgen = types.ModuleType("reportlab.pdfgen")
        pdfgen.canvas = types.SimpleNamespace(Canvas=object)
        pdfbase = types.ModuleType("reportlab.pdfbase")
        ttfonts = types.ModuleType("reportlab.pdfbase.ttfonts")
        ttfonts.TTFont = object
        pdfmetrics = types.ModuleType("reportlab.pdfbase.pdfmetrics")
        pdfmetrics.registerFont = lambda *args, **kwargs: None
        pdfbase.ttfonts = ttfonts
        pdfbase.pdfmetrics = pdfmetrics
        reportlab.pdfbase = pdfbase

        sys.modules["reportlab"] = reportlab
        sys.modules["reportlab.pdfgen"] = pdfgen
        sys.modules["reportlab.pdfbase"] = pdfbase
        sys.modules["reportlab.pdfbase.ttfonts"] = ttfonts
        sys.modules["reportlab.pdfbase.pdfmetrics"] = pdfmetrics

        tqdm_module = types.ModuleType("tqdm")
        tqdm_module.tqdm = lambda iterable: iterable
        sys.modules["tqdm"] = tqdm_module

    def tearDown(self):
        for name in self._module_names:
            sys.modules.pop(name, None)

        for name, module in self._original_modules.items():
            if module is not None:
                sys.modules[name] = module

    def test_module_imports_with_modern_pypdf2_names(self):
        module_path = (
            Path(__file__).resolve().parents[2]
            / "office"
            / "lib"
            / "pdf"
            / "add_watermark_service.py"
        )
        spec = importlib.util.spec_from_file_location(
            "pdf_add_watermark_service_test",
            module_path,
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module

        spec.loader.exec_module(module)

        self.assertTrue(hasattr(module, "pdf_add_watermark"))


if __name__ == "__main__":
    unittest.main()
