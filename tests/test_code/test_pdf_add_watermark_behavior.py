"""Behavioral tests for ``pdf_add_watermark`` (no real PDF deps required).

Covers the two fixes in office/lib/pdf/add_watermark_service.py:
  1. input/mark streams are always closed, including early-return paths;
  2. an empty (0-page) watermark PDF is handled gracefully instead of raising
     IndexError from ``pdf_watermark.pages[0]``.

Dependencies (PyPDF2/reportlab/tqdm) are mocked, following the convention of
``test_pdf_add_watermark_imports.py``.
"""

import builtins
import importlib.util
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest import mock


class FakePage:
    def merge_page(self, watermark):
        pass

    def compress_content_streams(self):
        pass


class FakePdfReader:
    def __init__(self, pages=None, is_encrypted=False, decrypt_fails=False):
        self.pages = pages if pages is not None else [FakePage()]
        self.is_encrypted = is_encrypted
        self.decrypt_fails = decrypt_fails

    def decrypt(self, password):
        if self.decrypt_fails:
            raise Exception("解密失败")
        return 1


class FakePdfWriter:
    def __init__(self):
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def write(self, file_obj):
        file_obj.write(b"")


class TestPdfAddWatermarkBehavior(unittest.TestCase):
    """Behavioral tests for the fixed pdf_add_watermark function."""

    MODULE_PATH = (
        Path(__file__).resolve().parents[2]
        / "office"
        / "lib"
        / "pdf"
        / "add_watermark_service.py"
    )

    def setUp(self):
        self._original_modules = {}
        for name in ("PyPDF2", "reportlab", "reportlab.pdfgen",
                     "reportlab.pdfbase", "reportlab.pdfbase.ttfonts",
                     "reportlab.pdfbase.pdfmetrics", "tqdm"):
            self._original_modules[name] = sys.modules.get(name)

        pypdf2 = types.ModuleType("PyPDF2")
        self._pdf_reader_mock = mock.Mock()
        pypdf2.PdfReader = self._pdf_reader_mock
        pypdf2.PdfWriter = FakePdfWriter
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
        for name, module in self._original_modules.items():
            if module is not None:
                sys.modules[name] = module
            else:
                sys.modules.pop(name, None)

    def _load_module(self):
        spec = importlib.util.spec_from_file_location(
            "pdf_add_watermark_service_behavior_test",
            self.MODULE_PATH,
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module

    @staticmethod
    def _track_open():
        """Return (patcher, list_of_opened_file_objects) for builtins.open."""
        real_open = builtins.open
        opened = []

        def tracking_open(*args, **kwargs):
            f = real_open(*args, **kwargs)
            opened.append(f)
            return f

        return mock.patch("builtins.open", side_effect=tracking_open), opened

    def test_empty_watermark_returns_false_without_crashing(self):
        module = self._load_module()
        self._pdf_reader_mock.side_effect = [
            FakePdfReader(pages=[FakePage(), FakePage()]),
            FakePdfReader(pages=[]),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            src = str(Path(tmp) / "source.pdf")
            mark = str(Path(tmp) / "mark_empty.pdf")
            out = str(Path(tmp) / "out.pdf")
            Path(src).write_bytes(b"fake")
            Path(mark).write_bytes(b"fake")

            patcher, opened = self._track_open()
            with patcher:
                result = module.pdf_add_watermark(src, mark, out)

        self.assertFalse(result)
        self.assertTrue(all(f.closed for f in opened), "streams must be closed")

    def test_normal_path_returns_true_and_closes_streams(self):
        module = self._load_module()
        self._pdf_reader_mock.side_effect = [
            FakePdfReader(pages=[FakePage(), FakePage()]),
            FakePdfReader(pages=[FakePage()]),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            src = str(Path(tmp) / "source.pdf")
            mark = str(Path(tmp) / "mark.pdf")
            out = str(Path(tmp) / "out.pdf")
            Path(src).write_bytes(b"fake")
            Path(mark).write_bytes(b"fake")

            patcher, opened = self._track_open()
            with patcher:
                result = module.pdf_add_watermark(src, mark, out)
            self.assertTrue(Path(out).exists())

        self.assertTrue(result)
        self.assertTrue(all(f.closed for f in opened), "streams must be closed")

    def test_encrypted_decrypt_failure_closes_input_stream(self):
        module = self._load_module()
        self._pdf_reader_mock.side_effect = [
            FakePdfReader(pages=[FakePage()], is_encrypted=True, decrypt_fails=True),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            src = str(Path(tmp) / "source.pdf")
            mark = str(Path(tmp) / "mark.pdf")
            out = str(Path(tmp) / "out.pdf")
            Path(src).write_bytes(b"fake")
            Path(mark).write_bytes(b"fake")

            patcher, opened = self._track_open()
            with mock.patch("builtins.input", return_value="wrong-password"), patcher:
                result = module.pdf_add_watermark(src, mark, out)

        self.assertFalse(result)
        self.assertTrue(all(f.closed for f in opened), "input stream must be closed on early return")


if __name__ == "__main__":
    unittest.main()
