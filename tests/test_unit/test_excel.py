import unittest
from pathlib import Path

import pandas as pd
from office.api.excel import *
import os


class TestExcel(unittest.TestCase):
    def test_fake2excel(self):
        fake2excel(language='fdsa')

    def test_split_excel_by_column(self):
        split_excel_by_column(filepath=r'../../contributors/bulabean/sedemo.xls',
                              column=6)

    def test_sheet2excel(self):
        sheet2excel(file_path=r'./test_files/excel/fake2excel.xlsx')

    def test_merge2sheet(self):
        merge2sheet(dir_path=r'./test_files/excel/merge2sheet')

    def test_merge2excel(self):
        merge2excel(dir_path=r'../../contributors/bulabean', output_file='test_merge2excel.xlsx', )

    def test_find_excel_data(self):
        find_excel_data(search_key='刘家站垦殖场', target_dir=r'../../contributors/bulabean')

    # def test_merge2sheet(self):
    #     """
    #     https://blog.csdn.net/xue_11/article/details/118424380
    #     https://www.jb51.net/article/214868.htm
    #     """
    #     dir_path = 'test_files/excel'
    #     for root, dirs, files in os.walk(dir_path):
    #         path = Path(dir_path)
    #         print(files)
    #         df_list = []
    #         for file in files:
    #             if file.endswith("xlsx") or file.endswith("xls"):
    #                 excel_path = (path / file)
    #                 df_list.append(pd.read_excel(excel_path))
    #         res = pd.concat(df_list)
    #         res.to_excel(
    #             R"./excel/output_file2.xlsx",
    #             sheet_name="手机商品",
    #             index=False  # 不保留index
    #         )

    # single_df_1 = pd.read_excel(r'./excel/1月.xls')
    # print(single_df_1)
    # single_df_2 = pd.read_excel(r'./excel/2月.xls')
    # single_df_3 = pd.read_excel(r'./excel/3月.xls')
    # single_df_4 = pd.read_excel(r'./excel/4月.xls')
    # res = pd.concat([single_df_1, single_df_2,single_df_3,single_df_4])
    # res.to_excel(
    #     R"./excel/output_file1.xlsx",
    #     sheet_name="手机商品",
    #     index=False,  # 不保留index
    # )
