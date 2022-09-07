import unittest

from office.api.testApi.ruiming import screen_unmarked_image, change_label_in_xml, screen_without_label_json_file


class TestExcel(unittest.TestCase):
    def test_screen_unmarked_image(self):
        screen_unmarked_image(dir_path='')

    def test_change_label_in_xml(self):
        change_label_in_xml(dir_path=r".\xml", old_label="测试", new_label="测试1")

    def test_screen_without_label_json_file(self):
        screen_without_label_json_file(dir_path="./test_files/json")
        # 预期结果：除1.json外均被移动到”无标签json文件“文件夹中