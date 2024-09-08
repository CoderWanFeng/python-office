import unittest

from office.api.word import *


class TestWechat(unittest.TestCase):
    def test_docx2pdf(self):
        docx2pdf(path=r'e://info//test//transverse2.docx')

    def test_doc2docx(self):
        doc2docx(input_path=r'../test_files/word/aaa - 副本.doc', output_path=r'../test_output/word',
                 output_name='abcd.docx')

    def test_docx2doc(self):
        docx2doc(input_path=r'../test_output/word/abcd.docx', output_path=r'../test_output/word',
                 output_name='abce')
