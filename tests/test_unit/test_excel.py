import unittest
from tests.test_utils.comm_utils import *
from office.api.excel import *


class TestExcel(unittest.TestCase):
    def test_fake2excel(self):
        test_file_name = './fake2excel.xlsx'
        fake2excel(language='sdag')
        # 检查文件是否存在
        self.assertTrue(file_exist(test_file_name))
        # 检查文件标题
        self.assertEqual("name", get_colum_content(test_file_name, 0))
        # 检查文件内容
        self.assertTrue(is_chinese_chars_regex(get_content(test_file_name, 0, 0)))

    def test_split_excel_by_column(self):
        test_origin_file_name = '../../contributors/bulabean/sedemo.xls'
        split_excel_by_column(filepath=test_origin_file_name,
                              column=6)
        last_file_name = get_latest_file('../../contributors/bulabean')
        res = get_filter_names(test_origin_file_name, 5)
        # 检查拆分后内容
        sheet_names = get_all_sheet_names(last_file_name)
        for sheet_name in res:
            self.assertIn(sheet_name, sheet_names)

    def test_sheet2excel(self):
        test_file_name = '../test_files/excel/fake2excel.xlsx'
        sheet2excel(file_path=test_file_name)
        sheet_names = get_all_sheet_names(test_file_name)

        for sheet_name in sheet_names:
            # 检查文件是否存在
            self.assertTrue(file_exist(f'./{sheet_name}.xlsx'))
            # 检查拆分文件的标题
            self.assertEqual(get_colum_content(test_file_name, 0, sheet_name),
                             get_colum_content(f'./{sheet_name}.xlsx', 0, sheet_name))
            # 检查拆分文件的内容
            self.assertEqual(get_content(test_file_name, 0, 0, sheet_name),
                             get_content(f'./{sheet_name}.xlsx', 0, 0, sheet_name))

    # TODO: 没有搞明白规则
    def test_merge2sheet(self):
        merge2sheet(dir_path=r'../test_files/excel/merge2sheet')
        # 检查文件是否存在
        self.assertTrue(file_exist('merge2sheet.xlsx'))

    def test_merge2excel(self):
        test_file_name = 'test_merge2excel.xlsx'
        merge2excel(dir_path=r'../../contributors/bulabean', output_file=test_file_name)
        # 检查文件是否存在
        self.assertTrue(file_exist(test_file_name))
        # 检查所有sheet名称
        self.assertIn("SEdemo_Split_2022-09-08_162027", get_all_sheet_names(test_file_name))
        self.assertIn("SEdemo_Split_2022-09-08_162113", get_all_sheet_names(test_file_name))
        self.assertIn("SEdemo_Split_2022-09-09_215031", get_all_sheet_names(test_file_name))
        self.assertIn("SEdemo_Split_2022-09-09_215121", get_all_sheet_names(test_file_name))
        self.assertNotIn("sedemo_Split_2022-08-23_203413", get_all_sheet_names(test_file_name))
        self.assertNotIn("sedemo_Split_2022-08-23_203011", get_all_sheet_names(test_file_name))
        self.assertNotIn("sedemo_Split_2022-09-17_154536", get_all_sheet_names(test_file_name))

    def test_find_excel_data(self):
        find_excel_data(search_key='程序员晚枫', target_dir=r'../../contributors/bulabean')