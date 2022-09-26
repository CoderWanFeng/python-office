import unittest

from office.api.file import *


class TestFile(unittest.TestCase):
    def test_replace4filename(self):
        replace4filename(path='./test_files/file/add_fix', del_content='dd', replace_content='pp')

    def test_file_name_insert_content(self):
        file_name_insert_content(file_path=r"./test_files/file/add_fix",
                                 insert_position=1, insert_content="插入内容测试")

    def test_file_name_add_prefix(self):
        file_name_add_prefix(file_path=r'./test_files/file/add_fix', prefix_content='2022')

    def test_file_name_add_postfix(self):
        file_name_add_postfix(file_path=r"./test_files/file/add_fix",
                              postfix_content="添加后缀测试")

    def test_search_specify_type_file(self):
        search_specify_type_file(file_path=r'./test_files/pdf', file_type='.pdf')

    def test_output_file_list_to_excel(self):
        output_file_list_to_excel("./test_files")

    def test_search_by_content(self):
        search_by_content(search_path=r'D:\workplace\code\github\search4file\tests\docs', content='小')
