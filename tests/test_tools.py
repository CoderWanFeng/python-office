import unittest

from office.api.image import add_watermark
from office.api.tools import url2ip, weather, lottery8ticket


class TestTools(unittest.TestCase):

    def test_weather(self):
        weather()

    def test_url2ip(self):
        url2ip('www.python-office.com')

    def test_image_watermark(self):
        add_watermark(file=r'.\目录结构.jpg', mark='程序员晚枫')

    def test_lottery8ticket(self):
        lottery8ticket()


