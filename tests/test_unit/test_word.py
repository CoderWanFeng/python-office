import unittest

from office.api.word import *
from tests.test_utils.comm_utils import *


class TestWechat(unittest.TestCase):
    def test_docx2pdf(self):
        docx2pdf(path=r'../test_files/docx/demo.docx')

    def test_doc2docx(self):
        doc2docx(input_path=r'../test_files/word/aaa - 副本.doc', output_path=r'../test_output/word',
                 output_name='abcd.docx')
        # 检查文件是否存在
        self.assertTrue(file_exist('../test_output/word/abcd.docx'))
        delete_file('../test_output/word/abcd.docx')

    def test_docx2doc(self):
        docx2doc(input_path=r'../test_output/word/abcd.docx', output_path=r'../test_output/word',
                 output_name='abce')
        # 检查文件是否存在
        self.assertTrue(file_exist('../test_output/word/abce.doc'))
        delete_file('../test_output/word/abce.doc')
