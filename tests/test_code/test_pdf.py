"""PDF功能测试模块。

该模块包含对python-office库中PDF相关功能的单元测试。
"""

import unittest

from office.api.pdf import *
from tests.test_utils.test_input import stub_stdin


class TestPDF(unittest.TestCase):
    """PDF功能测试类。
    
    该类包含对PDF相关API的单元测试方法。
    """

    @classmethod
    def setUpClass(cls):
        cls.INPUT_PDF = './tests/test_files/pdf/程序员晚枫.pdf'

    def test_add_watermark(self):
        stub_stdin(self, f'{self.INPUT_PDF}\npython-office\n')  # 依次输入
        add_watermark()

    def test_add_watermark_by_parameters(self):
        add_watermark_by_parameters(
            input_file=self.INPUT_PDF,
            mark_str='python-office',
            output_file='./tests/test_files/pdf/test_add_watermark_by_parameters/参数-水印-测试.pdf')

    def test_pdf2imgs(self):
        pdf2imgs(
            input_file=self.INPUT_PDF,
            output_file='./tests/test_files/pdf/test_pdf2imgs')

    # def test_file2pdf(self):
    #     file2pdf(
    #         file_type='txt',
    #         path=r'./test_files/popdf/in.popdf',
    #     )

    def test_pdf2docx(self):
        pdf2docx(
            input_file=self.INPUT_PDF,
            output_file=r'./tests/test_files/pdf/test_pdf2docx/out.docx'
        )

    def test_pdf2docx_path(self):
        pdf2docx(
            input_path=r'./tests/test_files/pdf/',
            output_path=r'./tests/test_files/pdf/test_pdf2docx_path/'
        )

    def test_merge2pdf(self):
        merge2pdf(
            input_file_list=[self.INPUT_PDF, self.INPUT_PDF],
            output_file=r'./tests/test_files/pdf/test_merge2pdf/merge2pdf.pdf'
        )

    def test_single_encrypt4pdf(self):
        """
        测试单个PDF文件加密功能

        该函数测试encrypt4pdf函数对单个PDF文件进行加密的能力，
        将指定的输入PDF文件加密后保存到指定输出路径
        """
        encrypt4pdf(
            input_file=self.INPUT_PDF,
            output_file=r'./tests/test_files/pdf/test_single_encrypt4pdf/encrypted.pdf',
            password='123456'
        )

    def test_batch_encrypt4pdf(self):
        """
        测试批量PDF文件加密功能

        该函数测试encrypt4pdf函数对多个PDF文件进行批量加密的能力，
        将指定输入目录下的所有PDF文件加密后保存到指定输出目录
        """
        encrypt4pdf(
            input_path=r'./tests/test_files/pdf/',
            output_path=r'./tests/test_files/pdf/test_batch_encrypt4pdf/',
            password='123456'
        )

    def test_single_decrypt4pdf(self):
        decrypt4pdf(
            input_file=r'./tests/test_files/pdf/test_single_encrypt4pdf/encrypted.pdf',
            output_file=r'./tests/test_files/pdf/test_single_decrypt4pdf/decrypted.pdf',
            password='123456')

    def test_batch_decrypt4pdf(self):
        decrypt4pdf(
            input_path=r'./tests/test_files/pdf/test_batch_encrypt4pdf/',
            output_path=r'./tests/test_files/pdf/test_batch_decrypt4pdf/',
            password='123456'
        )

    def test_pdf2imgs_alt(self):
        pdf2imgs(
            input_file=self.INPUT_PDF,
            output_file=r'./tests/test_files/pdf/test_pdf2imgs_alt'
        )

    def test_add_img_water(self):
        add_img_water(
            input_file=self.INPUT_PDF,
            mark_file=self.INPUT_PDF,
            output_file='./tests/test_files/pdf/test_add_img_water/add_img_res.pdf'
        )
