import unittest

from office.api.pdf import pdf2imgs, pdf2docx


class TestExcel(unittest.TestCase):
    def test_pdf2imgs(self):
        pdf2imgs(
            pdf_path=r'C:\Users\lenovo\Documents\WeChat Files\wxid_4zuh1m3d6dw212\FileStorage\MsgAttach\f1f9730d6e856d01d0aa5fcba49ea770\File\2022-07\鼎朗互娱_通用版_短视频合作协议.pdf',
            out_dir='./images')

    def test_pdf2docx(self):
        pdf2docx(
            file_path=r'D:\work\BaiduNetdiskWorkspace\personal\linux\workplace\docs\we-media\自媒体素材\图片\社区\基础入门\Python 入门第一节\0705\常用素材\如何利用Python进行自动化办公.pdf',
            output_path=r'C:\Users\lenovo\Desktop\package\test\output\test'
        )
