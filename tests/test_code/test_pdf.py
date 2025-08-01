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

    def test_single_encrypt4pdf(self):
        """
        测试单个PDF文件加密功能

        该函数测试encrypt4pdf函数对单个PDF文件进行加密的能力，
        将指定的输入PDF文件加密后保存到指定输出路径
        """
        encrypt4pdf(
            input_file=r'../test_files\pdf\encrypt4pdf\in\程序员晚枫1.pdf',
            output_file=r'../test_files\pdf\encrypt4pdf\out\a.pdf',
            password='123456'
        )

    def test_batch_encrypt4pdf(self):
        """
        测试批量PDF文件加密功能

        该函数测试encrypt4pdf函数对多个PDF文件进行批量加密的能力，
        将指定输入目录下的所有PDF文件加密后保存到指定输出目录
        """
        encrypt4pdf(
            input_path=r'../test_files\pdf\encrypt4pdf\in\o',
            output_path=r'../test_files\pdf\encrypt4pdf\out',
            password='123456'
        )


    def test_decrypt4pdf(self):
        decrypt4pdf(
            path=r'./test_files/popdf/encrypt.popdf',
            password='123456'
        )

    def test_pdf2imgs(self):
        pdf2imgs(
            pdf_path=r'./test_files/popdf/in.popdf',
            out_dir=r'./test_files/popdf'
        )

    def test_add_img_water(self):
        add_img_water(pdf_file_in='./test_files/popdf/add_img.popdf', pdf_file_mark='./test_files/popdf/in.popdf',
                      pdf_file_out='add_img_res.popdf')
