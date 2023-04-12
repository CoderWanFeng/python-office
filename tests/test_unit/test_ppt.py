import unittest

from office.api.ppt import *


class TestPPT(unittest.TestCase):
    def test_ppt2pdf(self):
        ppt2pdf(path=r'D:\workplace\code\github\poppt\tests\ppt',
                output_path=r'D:\workplace\code\github\poppt\tests\ppt\abc')

    def test_ppt2img(self):
        ppt2img(input_path=r'../test_files/ppt/ppt2img/程序员晚枫的文档.pptx',
                output_path=r'../test_files/ppt/ppt2img', img_type='jpg')
