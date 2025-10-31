"""PPT功能测试模块。

该模块包含对python-office库中PPT相关功能的单元测试。
"""

import unittest

from office.api.ppt import *
from tests.test_utils.comm_utils import *


class TestPPT(unittest.TestCase):
    """PPT功能测试类。
    
    该类包含对PPT相关API的单元测试方法。
    """
    def test_ppt2pdf(self):
        ppt2pdf(path=r'../test_files/ppt/程序员晚枫的ppt.pptx',
                output_path=r'../test_files/ppt/ppt2pdf')
        self.assertTrue(file_exist('../test_files/ppt/ppt2pdf/程序员晚枫的文档.pdf'))

    # todo: 文件打开有异常
    def test_ppt2img(self):
        ppt2img(input_path=r'../test_files/ppt/程序员晚枫的ppt.pptx',
                output_path=r'../test_files/ppt/ppt2img')
