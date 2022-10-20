import unittest

from office.api.image import *


class TestImage(unittest.TestCase):
    def test_add_watermark(self):
        add_watermark(file='./test_files/images/0816.jpg', mark='python-office')

    def test_down4img(self):
        down4img(url='https://www.python-office.com/api/img-cdn/python-office/find_excel_data/group.jpg',output_path=r'D:\download\xunlei')

    # def test_img2Cartoon(self):
    #     img2Cartoon()

    def test_txt2wordcloud(self):
        txt2wordcloud(filename=r'D:\workplace\code\test\wordcloud\test.txt', color="white",
                      result_file="your_wordcloud.png")

    def test_pencil4img(self):
        pencil4img(input_img=r'D:\workplace\code\test\down4img\girl.jpg')