import unittest

import pytest

from office.api.tools import *
from tests.test_utils.test_input import stub_stdin


class TestTools(unittest.TestCase):
    @pytest.mark.skip(reason="交互式功能，暂时跳过")
    def test_weather(self):
        stub_stdin(self, '北京\ny\nq\n')  # 依次输入
        weather()

    def test_url2ip(self):
        ip_str = url2ip('www.python-office.com')
        self.assertEqual(ip_str, "2408:877a:2000:f::11")

    @pytest.mark.skip(reason="交互式功能，暂时跳过")
    def test_lottery8ticket(self):
        stub_stdin(self, '12\n0\n')  # 依次输入
        lottery8ticket()

    def test_create_article(self):
        create_article('生日快乐', line_num=2000)

    # def test_pwd4wifi(self):
    #     stub_stdin(self, '1\ny\n')  #依次输入
    #     pwd4wifi(pwd_list=['12345678', 'CoderWanFeng'])
    def test_open_soft(self):
        soft_path = r'D:\software\wechat\WeChat.exe'
        wftools.open_soft(soft_path, num=2)
