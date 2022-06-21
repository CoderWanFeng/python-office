import unittest

from office.api.excel import fake2excel


class TestExcel(unittest.TestCase):
    def test_fake2excel(self):
        fake2excel(language='fdsa')
