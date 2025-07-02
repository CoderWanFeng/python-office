import unittest

from office.api.markdown import *
from tests.test_utils.comm_utils import *


class TestMarkdown(unittest.TestCase):

    def test_excel2markdown(self):
        excel2markdown(input_file=r'../test_files/excel/fake2excel.xlsx', output_file=r'../test_files/markdown/test.md',
                       sheet_name=None)
        self.assertTrue(file_exist('../test_files/markdown/test.md'))
        delete_file('../test_files/markdown/test.md')
