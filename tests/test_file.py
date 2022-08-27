import unittest

from office.api.file import file_name_add_prefix, search_specify_type_file


class TestExcel(unittest.TestCase):
    def test_file_name_add_prefix(self):
        file_name_add_prefix(file_path=r'D:\workplace\code\test\output\test', prefix_content='2022')

    def test_search_specify_type_file(self):
        search_specify_type_file(file_path=r'./pdf', file_type='.pdf')
