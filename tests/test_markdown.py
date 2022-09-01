import unittest

from office.api.markdown import markdown_link_image_to_base64, check_local_dir_image_link_markdown


class TestMarkdown(unittest.TestCase):
    def test_markdown_link_image_to_base64(self, ):
        markdown_link_image_to_base64(
            markdown_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\markdown\test.md")

    def test_check_local_dir_image_link_markdown(self):
        check_local_dir_image_link_markdown(
            markdown_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\markdown\test.md",
            image_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\markdown\test.assets")
