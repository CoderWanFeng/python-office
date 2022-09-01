import unittest

from office.api.pdf import *


class TestExcel(unittest.TestCase):
    def test_pdf2imgs(self):
        pdf2imgs(
            pdf_path=r'C:\Users\lenovo\Documents\WeChat Files\wxid_4zuh1m3d6dw212\FileStorage\MsgAttach\f1f9730d6e856d01d0aa5fcba49ea770\File\2022-07\鼎朗互娱_通用版_短视频合作协议.pdf',
            out_dir='./images')

    def test_pdf2docx(self):
        pdf2docx(
            file_path=r'D:\如何利用Python进行自动化办公.pdf',
            output_path=r'C:\output\test'
        )

    def test_add_img_water(self):
        add_img_water(pdf_file_in='./pdf/add_img.pdf', pdf_file_mark='./pdf/in.pdf', pdf_file_out='add_img.pdf')

    def test_add_watermark_by_parameters(self):
        add_watermark_by_parameters(
            pdf_file=r'C:\Users\Lenovo\Documents\WeChat Files\wxid_z91t05fqtrry22\FileStorage\MsgAttach\7ae419aa6a5f7c2fc32c594a69e28c6d\File\2022-06\2022眼科行业研究报告-动脉网-2022-52页.pdf',
            mark_str='abc',
            output_file_name='测试.pdf')
