"""Tests for the web API wrapper."""

import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch


def load_web_api():
    module_path = Path(__file__).resolve().parents[2] / "office" / "api" / "web.py"
    spec = importlib.util.spec_from_file_location("web_api_under_test", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestWeb(unittest.TestCase):
    def test_url2ebook_delegates_to_pospider(self):
        web = load_web_api()
        url2ebook = Mock()
        pospider = SimpleNamespace(url=SimpleNamespace(url2ebook=url2ebook))

        with patch.object(web, "_load_pospider", return_value=pospider):
            web.url2ebook("https://example.com/article", tile="测试")

        url2ebook.assert_called_once_with(
            url="https://example.com/article",
            tile="测试",
        )

    def test_loader_reports_incompatible_pospider(self):
        web = load_web_api()

        with patch("builtins.__import__", return_value=SimpleNamespace()):
            with self.assertRaises(ImportError) as error:
                web._load_pospider()

        self.assertIn("不提供 url.url2ebook", str(error.exception))


if __name__ == "__main__":
    unittest.main()
