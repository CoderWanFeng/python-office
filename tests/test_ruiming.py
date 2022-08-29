import unittest

from office.api.testApi.ruiming import screen_unmarked_image


class TestExcel(unittest.TestCase):
    def test_screen_unmarked_image(self):
        screen_unmarked_image(dir_path='')
