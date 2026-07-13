"""Regression tests for the PDF image-watermark API wrapper."""

import importlib.util
import sys
import types
import unittest
from pathlib import Path
from unittest import mock


PDF_API_PATH = Path(__file__).parents[2] / "office" / "api" / "pdf.py"


def load_pdf_api():
    """Load the wrapper with a lightweight stand-in for the optional popdf package."""
    popdf = types.ModuleType("popdf")
    popdf.add_img_water = mock.Mock()
    spec = importlib.util.spec_from_file_location("pdf_api_under_test", PDF_API_PATH)
    module = importlib.util.module_from_spec(spec)

    with mock.patch.dict(sys.modules, {"popdf": popdf}):
        spec.loader.exec_module(module)

    return module, popdf


class TestAddImgWater(unittest.TestCase):
    def test_forwards_current_parameters_to_popdf(self):
        pdf_api, popdf = load_pdf_api()

        pdf_api.add_img_water("input.pdf", "mark.png", "output.pdf")

        popdf.add_img_water.assert_called_once_with(
            pdf_file_in="input.pdf",
            pdf_file_mark="mark.png",
            pdf_file_out="output.pdf",
        )

    def test_forwards_deprecated_parameter_aliases(self):
        pdf_api, popdf = load_pdf_api()

        with self.assertWarnsRegex(DeprecationWarning, "pdf_file_in"):
            pdf_api.add_img_water(
                pdf_file_in="legacy-input.pdf",
                pdf_file_mark="legacy-mark.png",
                pdf_file_out="legacy-output.pdf",
            )

        popdf.add_img_water.assert_called_once_with(
            pdf_file_in="legacy-input.pdf",
            pdf_file_mark="legacy-mark.png",
            pdf_file_out="legacy-output.pdf",
        )


if __name__ == "__main__":
    unittest.main()
