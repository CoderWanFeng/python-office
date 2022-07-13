import unittest
import pandas as pd
from office.api.excel import fake2excel


class TestExcel(unittest.TestCase):
    def test_fake2excel(self):
        fake2excel(language='fdsa')

    def test_merge2sheet(self):
        """
        https://blog.csdn.net/xue_11/article/details/118424380
        https://www.jb51.net/article/214868.htm
        """
        dir_path = './'

        single_df_1 = pd.read_excel(r'./excel/1月.xls')
        print(single_df_1)
        single_df_2 = pd.read_excel(r'./excel/2月.xls')
        single_df_3 = pd.read_excel(r'./excel/3月.xls')
        single_df_4 = pd.read_excel(r'./excel/4月.xls')
        res = pd.concat([single_df_1, single_df_2,single_df_3,single_df_4])
        res.to_excel(
            R"./excel/output_file1.xlsx",
            sheet_name="手机商品",
            index=False,  # 不保留index
        )
