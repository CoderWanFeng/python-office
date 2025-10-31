"""Web功能测试模块。

该模块包含对python-office库中Web相关功能的单元测试。
"""

import unittest

from office.api import web


# todo: 功能暂时未实现
class TestWechat(unittest.TestCase):
    """Web功能测试类。
    
    该类包含对Web相关API的单元测试方法。
    """
    def test_url2ebook(self):
        web.url2ebook('https://www.zhihu.com/question/36810597', title='测试')
