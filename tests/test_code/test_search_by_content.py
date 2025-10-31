"""内容搜索功能测试模块。

该模块包含对python-office库中内容搜索相关功能的单元测试。
"""

import unittest

from office.api.file import *


class TestSBC(unittest.TestCase):
    """内容搜索功能测试类。
    
    该类包含对内容搜索相关API的单元测试方法。
    """
    def test_search_by_content(self):
        search_by_content(search_path=r'../test_files/', content='python-office')
