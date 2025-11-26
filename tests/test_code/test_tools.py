"""工具功能测试模块。

该模块包含对python-office库中工具相关功能的单元测试。
"""

import unittest

import pytest

from office.api.tools import *
from tests.test_utils.test_input import stub_stdin


class TestTools(unittest.TestCase):
    """工具功能测试类。

    该类包含对工具相关API的单元测试方法。
    """
    @pytest.mark.skip(reason="交互式功能，暂时跳过")
    def test_weather(self):
        stub_stdin(self, '重庆\ny\nq\n')  # 依次输入
        weather()

    def test_url2ip(self):
        url2ip('www.python-office.com')

    @pytest.mark.skip(reason="交互式功能，暂时跳过")
    def test_lottery8ticket(self):
        stub_stdin(self, '12\n0\n')  # 依次输入
        lottery8ticket()

    def test_create_article(self):
        create_article('生日快乐', line_num=2000)

    def test_open_soft(self):
        soft_path = r'D:\software\wechat\WeChat.exe'
        wftools.open_soft(soft_path, num=2)

    def test_net_speed_test(self):
        net_speed_test()
