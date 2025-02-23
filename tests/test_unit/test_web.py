import unittest

from office.api import web


# todo: 功能暂时未实现
class TestWechat(unittest.TestCase):
    def test_url2ebook(self):
        web.url2ebook('https://www.zhihu.com/question/36810597', title='测试')
