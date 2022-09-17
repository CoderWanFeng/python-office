import unittest

from office.api.wechat import send_file


class TestWechat(unittest.TestCase):
    def test_send_file(self):
        send_file(who='文件传输助手', file=r'./test_files/images/0816.jpg')
