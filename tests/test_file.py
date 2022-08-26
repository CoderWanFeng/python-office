import unittest

from office.api.file import file_name_add_prefix


class TestExcel(unittest.TestCase):
    def test_file_name_add_prefix(self):
        file_name_add_prefix(file_path=r'D:\workplace\code\test\output\test', prefix_content='2022')
