import unittest
from office.excel import fake2excel


class TestExcel(unittest.TestCase):
    def test_fake2excel(self):
        fake2excel()
