import unittest

from office.api.markdown import markdown_link_image_to_base64


class TestMarkdown(unittest.TestCase):
    def test_markdown_link_image_to_base64(self, ):
        markdown_link_image_to_base64(
            markdown_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\markdown\test.md")
