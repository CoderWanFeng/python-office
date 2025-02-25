import unittest

from office.api.file import *


class TestSBC(unittest.TestCase):
    def test_search_by_content(self):
        search_by_content(search_path=r'../test_files/', content='python-office')
