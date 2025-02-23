import unittest

from office.api.ppt import *
from test_excel_utils import *


class TestPPT(unittest.TestCase):
    def test_ppt2pdf(self):
        ppt2pdf(path=r'../test_files/ppt/程序员晚枫的文档.pptx',
                output_path=r'../test_files/ppt/ppt2pdf')
        self.assertTrue(file_exist('../test_files/ppt/ppt2pdf/程序员晚枫的文档.pdf'))

    def test_ppt2img(self):
        ppt2img(input_path=r'../test_files/ppt/程序员晚枫的文档.pptx',
                output_path=r'../test_files/ppt/ppt2img')
