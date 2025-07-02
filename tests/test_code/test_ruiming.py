import unittest

from office.api.testApi.ruiming import screen_unmarked_image, change_label_in_xml, screen_without_label_json_file
from tests.test_utils.comm_utils import *


class TestRuiming(unittest.TestCase):
    def test_screen_unmarked_image(self):
        screen_unmarked_image(dir_path='../test_files/ruiming/screen_unmarked_image')
        # 预期结果：2.jpg被移动到“未标注图片”目录下

    def test_change_label_in_xml(self):
        # TODO：相对路径问题
        change_label_in_xml(dir_path="../test_files/ruiming/change_label_in_xml", old_label="测试", new_label="测试1")
        # 预期结果：name标签内容从“测试”改为“测试1”
        file_names = get_file_by_suffix('../test_files/ruiming/change_label_in_xml', 'xml')
        for file_name in file_names:
            names = get_all_name_values('../test_files/ruiming/change_label_in_xml/' + file_name)
            self.assertNotIn('测试', names)
        # 还原
        change_label_in_xml(dir_path="../test_files/ruiming/change_label_in_xml", old_label="测试1", new_label="测试")

    def test_screen_without_label_json_file(self):
        # TODO：相对路径问题
        screen_without_label_json_file(dir_path="../test_files/ruiming/screen_without_label_json_file")
        # 预期结果：除1.json外均被移动到”无标签json文件“文件夹中
