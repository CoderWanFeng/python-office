# -*- coding: UTF-8 -*-
"""Tests for the url2ebook Skill wrapper."""

import ast
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


def _assigned_all(source: str):
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    return ast.literal_eval(node.value)
    return None


class TestUrl2ebookSkill(unittest.TestCase):
    def test_web_category_exports_url2ebook(self):
        source = (ROOT / "skills" / "web" / "__init__.py").read_text(encoding="utf-8")
        self.assertEqual(_assigned_all(source), ["url2ebook"])

    def test_skill_reexports_web_api(self):
        source = (ROOT / "skills" / "web" / "url2ebook" / "__init__.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("from office.api.web import url2ebook", source)
        self.assertEqual(_assigned_all(source), ["url2ebook"])

    def test_skill_doc_covers_triggers_and_tile_param(self):
        skill_md = (ROOT / "skills" / "web" / "url2ebook" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("name: url2ebook", skill_md)
        self.assertIn("网页转电子书", skill_md)
        self.assertIn("`tile`", skill_md)
        self.assertIn("office.api.web.url2ebook", skill_md)


if __name__ == "__main__":
    unittest.main()
