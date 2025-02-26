import unittest

from office.api.image import *
from tests.test_utils.comm_utils import *


class TestImage(unittest.TestCase):
    def test_add_watermark(self):
        add_watermark(file='../test_files/images/0816.jpg', mark='python-office',
                      output_path=r'../test_output/img_output')
        self.assertTrue(file_exist('../test_output/img_output/0816.jpg'))
        delete_file('../test_output/img_output/0816.jpg')

    def test_com_img(self):
        compress_image(input_file='../test_files/images/0816.jpg',
                       output_file='../test_output/img_output/0816.jpg', quality=50)
        self.assertTrue(file_exist('../test_output/img_output/0816.jpg'))
        delete_file('../test_output/img_output/0816.jpg')

    def test_down4img(self):
        down4img(url='https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/python-office-qr.jpg',
                 output_path=r'../test_files/images')
        self.assertTrue(file_exist('../test_files/images/down4img.jpg'))
        delete_file('../test_files/images/down4img.jpg')

    def test_txt2wordcloud(self):
        txt2wordcloud(filename=r'../test_files/md/test.txt')
        self.assertTrue(file_exist('your_wordcloud.png'))
        delete_file('your_wordcloud.png')

    def test_pencil4img(self):
        pencil4img(input_img=r'../test_files/images/pencil4img.jpg')
        self.assertTrue(file_exist('pencil4img.jpg'))
        delete_file('pencil4img.jpg')
