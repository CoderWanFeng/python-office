import unittest

from office.api.pdf import *
from tests.test_utils.test_input import stub_stdin


class TestPDF(unittest.TestCase):
    def test_add_watermark(self):
        stub_stdin(self, './test_files/popdf/in.popdf\npython-office\n')  # 依次输入
        add_watermark()

    def test_add_watermark_by_parameters(self):
        add_watermark_by_parameters(
            pdf_file=r'./test_files/popdf/in.popdf',
            mark_str='python-office',
            output_file_name='参数-水印-测试.popdf')

    def test_pdf2imgs(self):
        pdf2imgs(
            pdf_path=r'./test_files/popdf/in.popdf',
            out_dir='./images')

    def test_pdf2docx(self):
        pdf2docx(
            file_path=r'./test_files/popdf/in.popdf',
            output_path=r'./test_files/popdf/'
        )

    # def test_file2pdf(self):
    #     file2pdf(
    #         file_type='txt',
    #         path=r'./test_files/popdf/in.popdf',
    #     )

    def test_pdf2docx(self):
        pdf2docx(
            file_path=r'./test_files/popdf/in.popdf',
            output_path=r'./test_files/popdf/'
        )

    def test_merge2pdf(self):
        merge2pdf(
            one_by_one=[r'./test_files/popdf/in.popdf', r'./test_files/popdf/add_img.popdf'],
            output=r'./test_files/popdf/merge2pdf.popdf'
        )

    def test_encrypt4pdf(self):
        encrypt4pdf(
            path=r'D:\workplace\code\github\popdf\tests\test_files\pdf\32012356985422-watermark.popdf',
            password='123456'
        )

    def test_decrypt4pdf(self):
        decrypt4pdf(
            path=r'./test_files/popdf/encrypt.popdf',
            password='123456'
        )
    def test_pdf2imgs(self):
        pdf2imgs(
             pdf_path =r'./test_files/popdf/in.popdf',
            out_dir=r'./test_files/popdf'
        )

    def test_add_img_water(self):
        add_img_water(pdf_file_in='./test_files/popdf/add_img.popdf', pdf_file_mark='./test_files/popdf/in.popdf',
                      pdf_file_out='add_img_res.popdf')
