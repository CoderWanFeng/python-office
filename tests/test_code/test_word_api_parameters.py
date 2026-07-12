import importlib.util
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


def load_word_api():
    fake_poword = types.ModuleType("poword")
    fake_poword.doc2docx = Mock()

    module_path = Path(__file__).parents[2] / "office" / "api" / "word.py"
    spec = importlib.util.spec_from_file_location("word_api_under_test", module_path)
    module = importlib.util.module_from_spec(spec)

    with patch.dict(sys.modules, {"poword": fake_poword}):
        spec.loader.exec_module(module)

    return module, fake_poword


class TestDoc2DocxParameters(unittest.TestCase):
    def setUp(self):
        self.word_api, self.poword = load_word_api()

    def test_keeps_default_call_compatible(self):
        self.word_api.doc2docx("source.doc", "output", "result.docx")

        self.poword.doc2docx.assert_called_once_with(
            input_path="source.doc",
            output_path="output",
            output_name="result.docx",
        )

    def test_forwards_hidden_progress_option(self):
        self.word_api.doc2docx(
            "source.doc",
            "output",
            "result.docx",
            show_progress=False,
        )

        self.poword.doc2docx.assert_called_once_with(
            input_path="source.doc",
            output_path="output",
            output_name="result.docx",
            show_progress=False,
        )


if __name__ == "__main__":
    unittest.main()
