import unittest

from office.api.file import *
from tests.test_utils.comm_utils import *

ORIGIN_FILE_NAME = '../test_files/file/add_fix/aabbccddeeffgghhppddaacc.docx'


class TestFile(unittest.TestCase):

    def test_replace4filename(self):
        touch_file(ORIGIN_FILE_NAME)
        replace4filename(path='../test_files/file/add_fix', del_content='dd', replace_content='pp')
        # 检查文件存在
        self.assertTrue(file_exist('../test_files/file/add_fix/aabbccppeeffgghhppppaacc.docx'))
        # 删除文件
        delete_file('../test_files/file/add_fix/aabbccppeeffgghhppppaacc.docx')

    def test_file_name_insert_content(self):
        touch_file(ORIGIN_FILE_NAME)
        file_name_insert_content(file_path=r"../test_files/file/add_fix",
                                 insert_position=1, insert_content="111")
        # 检查文件存在
        self.assertTrue(file_exist('../test_files/file/add_fix/a111abbccddeeffgghhppddaacc.docx'))
        # 删除文件
        delete_file('../test_files/file/add_fix/a111abbccddeeffgghhppddaacc.docx')

    def test_file_name_add_prefix(self):
        touch_file(ORIGIN_FILE_NAME)
        file_name_add_prefix(file_path=r'../test_files/file/add_fix', prefix_content='2022')
        # 检查文件存在
        self.assertTrue(file_exist('../test_files/file/add_fix/2022aabbccddeeffgghhppddaacc.docx'))
        # 删除文件
        delete_file('../test_files/file/add_fix/2022aabbccddeeffgghhppddaacc.docx')

    def test_file_name_add_postfix(self):
        touch_file(ORIGIN_FILE_NAME)
        file_name_add_postfix(file_path=r"../test_files/file/add_fix",
                              postfix_content="5555")
        # 检查文件存在
        self.assertTrue(file_exist('../test_files/file/add_fix/aabbccddeeffgghhppddaacc5555.docx'))
        # 删除文件
        delete_file('../test_files/file/add_fix/aabbccddeeffgghhppddaacc5555.docx')

    def test_search_specify_type_file(self):
        search_specify_type_file(file_path=r'../test_files/docx', file_type='.docx')

    def test_output_file_list_to_excel(self):
        output_file_list_to_excel("../test_files")
        # 检查文件是否存在
        self.assertTrue(file_exist('../test_files/本目录文件列表.xlsx'))
        # 删除文件
        delete_file('../test_files/本目录文件列表.xlsx')

    def test_search_by_content(self):
        search_by_content(search_path=r'../test_files/docx', content='程序')

    def test_get_files(self):
        f = get_files(path=r'../test_files/docx')
        self.assertEqual(len(f), 1)
