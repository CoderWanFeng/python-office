"""Markdown功能测试模块。

该模块包含对python-office库中Markdown相关功能的单元测试。
"""

import unittest

from office.api.markdown import *
from tests.test_utils.comm_utils import *


class TestMarkdown(unittest.TestCase):
    """Markdown功能测试类。
    
    该类包含对Markdown相关API的单元测试方法。
    """

    def test_excel2markdown(self):
        excel2markdown(input_file=r'../test_files/excel/fake2excel.xlsx', output_file=r'../test_files/markdown/test.md',
                       sheet_name=None)
        self.assertTrue(file_exist('../test_files/markdown/test.md'))
        delete_file('../test_files/markdown/test.md')
