import unittest

from office.api.ppt import *
from tests.test_utils.comm_utils import *


class TestPPT(unittest.TestCase):
    def test_ppt2pdf(self):
        ppt2pdf(path=r'../test_files/ppt/程序员晚枫的ppt.pptx',
                output_path=r'../test_files/ppt/ppt2pdf')
        self.assertTrue(file_exist('../test_files/ppt/ppt2pdf/程序员晚枫的文档.pdf'))

    # todo: 文件打开有异常
    def test_ppt2img(self):
        ppt2img(input_path=r'../test_files/ppt/程序员晚枫的ppt.pptx',
                output_path=r'../test_files/ppt/ppt2img')
