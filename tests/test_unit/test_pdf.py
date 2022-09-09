import unittest

from office.api.pdf import *
from tests.test_utils.test_input import stub_stdin


class TestPDF(unittest.TestCase):
    def test_add_watermark(self):
        stub_stdin(self, './test_files/pdf/in.pdf\npython-office\n')  # 依次输入
        add_watermark()

    def test_add_watermark_by_parameters(self):
        add_watermark_by_parameters(
            pdf_file=r'./test_files/pdf/in.pdf',
            mark_str='python-office',
            output_file_name='参数-水印-测试.pdf')

    def test_pdf2imgs(self):
        pdf2imgs(
            pdf_path=r'./test_files/pdf/in.pdf',
            out_dir='./images')

    def test_pdf2docx(self):
        pdf2docx(
            file_path=r'./test_files/pdf/in.pdf',
            output_path=r'./test_files/pdf/'
        )

    # def test_file2pdf(self):
    #     file2pdf(
    #         file_type='txt',
    #         path=r'./test_files/pdf/in.pdf',
    #     )

    def test_pdf2docx(self):
        pdf2docx(
            file_path=r'./test_files/pdf/in.pdf',
            output_path=r'./test_files/pdf/'
        )

    def test_merge2pdf(self):
        merge2pdf(
            one_by_one=[r'./test_files/pdf/in.pdf', r'./test_files/pdf/add_img.pdf'],
            output=r'./test_files/pdf/merge2pdf.pdf'
        )

    def test_encrypt4pdf(self):
        encrypt4pdf(
            path=r'./test_files/pdf/in.pdf',
            password='123456'
        )

    def test_decrypt4pdf(self):
        decrypt4pdf(
            path=r'./test_files/pdf/encrypt.pdf',
            password='123456'
        )
    def test_pdf2imgs(self):
        pdf2imgs(
             pdf_path =r'./test_files/pdf/in.pdf',
            out_dir=r'./test_files/pdf'
        )

    def test_add_img_water(self):
        add_img_water(pdf_file_in='./test_files/pdf/add_img.pdf', pdf_file_mark='./test_files/pdf/in.pdf',
                      pdf_file_out='add_img_res.pdf')
