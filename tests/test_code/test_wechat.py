"""微信功能测试模块。

该模块包含对python-office库中微信相关功能的单元测试。
"""

import unittest

from office.api.wechat import *


class TestWechat(unittest.TestCase):
    """微信功能测试类。
    
    该类包含对微信相关API的单元测试方法。
    """
    def test_send_file(self):
        send_file(who='文件传输助手', file=r'../test_files/images/0816.jpg')

    def test_receive_message(self):
        receive_message(who='程序员晚枫')
