import unittest

from office.api.testApi.ruiming import screen_unmarked_image, change_label_in_xml


class TestExcel(unittest.TestCase):
    def test_screen_unmarked_image(self):
        screen_unmarked_image(dir_path='')

    def test_change_label_in_xml(self):
        change_label_in_xml(dir_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\xml",
                            old_label="测试", new_label="测试1")
