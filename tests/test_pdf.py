import unittest

from office.api.pdf import pdf2imgs


class TestExcel(unittest.TestCase):
    def test_pdf2imgs(self):
        pdf2imgs(
            pdf_path=r'C:\Users\lenovo\Documents\WeChat Files\wxid_4zuh1m3d6dw212\FileStorage\MsgAttach\f1f9730d6e856d01d0aa5fcba49ea770\File\2022-07\鼎朗互娱_通用版_短视频合作协议.pdf',out_dir='./images' )
