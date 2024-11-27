import unittest

from office.api import web


class TestWechat(unittest.TestCase):
    def test_url2ebook(self):
        web.url2ebook('https://www.zhihu.com/question/36810597', title='测试')


