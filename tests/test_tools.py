import unittest

from office.image import add_watermark
from office.tools import url2ip, weather



class TestTools(unittest.TestCase):

    def test_weather(self):
        weather()

    def test_url2ip(self):
        url2ip('www.python-office.com')

    def test_image_watermark(self):
        add_watermark(file=r'.\目录结构.jpg',mark='程序员晚枫')
