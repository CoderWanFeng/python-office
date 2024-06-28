import unittest

from office.api.wechat import *


class TestWechat(unittest.TestCase):
    def test_send_file(self):
        send_file(who='文件传输助手', file=r'./test_files/images/0816.jpg')

    def test_receive_message(self):
        receive_message(who='程序员晚枫')
