"""Tests for doc2docx output path handling."""

import unittest
from unittest.mock import Mock, patch

from office.api import word as word_api


class TestDoc2DocxOutputPath(unittest.TestCase):
    def test_doc2docx_accepts_full_output_file_path(self):
        poword = Mock()

        with patch.object(word_api, "_load_poword", return_value=poword):
            word_api.doc2docx(
                input_path="source.doc",
                output_path="converted/result.docx",
            )

        poword.doc2docx.assert_called_once_with(
            input_path="source.doc",
            output_path="converted",
            output_name="result.docx",
        )

    def test_doc2docx_keeps_directory_output_path(self):
        poword = Mock()

        with patch.object(word_api, "_load_poword", return_value=poword):
            word_api.doc2docx(
                input_path="source.doc",
                output_path="converted",
                output_name="result.docx",
            )

        poword.doc2docx.assert_called_once_with(
            input_path="source.doc",
            output_path="converted",
            output_name="result.docx",
        )


if __name__ == "__main__":
    unittest.main()
