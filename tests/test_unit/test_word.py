import unittest

from office.api.word import docx2pdf

from office.api.wechat import send_file


class TestWechat(unittest.TestCase):
    def test_docx2pdf(self):
        docx2pdf(path=r'e://info//test//transverse2.docx')
