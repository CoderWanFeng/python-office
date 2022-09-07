import unittest

from office.api.file import file_name_add_prefix, search_specify_type_file, file_name_insert_content, \
    file_name_add_postfix, output_file_list_to_excel


class TestFile(unittest.TestCase):
    def test_file_name_add_prefix(self):
        file_name_add_prefix(file_path=r'D:\workplace\code\test\output\test', prefix_content='2022')

    def test_search_specify_type_file(self):
        search_specify_type_file(file_path=r'test_files/pdf', file_type='.pdf')

    def test_file_name_insert_content(self):
        file_name_insert_content(file_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\file",
                                 insert_position=1, insert_content="插入内容测试")

    def test_file_name_add_postfix(self):
        file_name_add_postfix(r"C:\Users\37386\PycharmProjects\python-office\testfile\file",
                              "添加后缀测试")

    def test_output_file_list_to_excel(self):
        output_file_list_to_excel("../testfile")