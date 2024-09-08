# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/8/22 23:28
'''

"""
🌈Python自动化办公--Pandas玩转Excel（全30集）
https://www.bilibili.com/video/BV1hk4y1C73S/
"""
import poexcel

# @except_dec()
from office.lib.decorator_utils.instruction_url import instruction


# @instruction
def fake2excel(columns=['name'], rows=1, path='./fake2excel.xlsx', language='zh_CN'):
    """
    自动创建Excel，并且模拟数据
    Args:
        columns: 列名。可以模拟的列有：http://python4office.cn/python-office/fake2excel/
        rows: 生成多少行数据。默认值：1
        path: 生成的Excel的位置和名称。
        language: 数据用什么语言，默认是中文，可以填english，

    Returns:

    """
    poexcel.fake2excel(columns, rows, path, language)


# 多个excel，合并到一个excel的不同sheet中
# @except_dec()
# @instruction
def merge2excel(dir_path, output_file='merge2excel.xlsx'):
    """
    :param dir_path:
    :param output_file:
    :return:
    """
    poexcel.merge2excel(dir_path, output_file)


# 同一个excel里的不同sheet，拆分为不同的excel文件
# @except_dec()
# @instruction
def sheet2excel(file_path, output_path='./'):
    poexcel.sheet2excel(file_path, output_path)


# @except_dec()
# @instruction
def merge2sheet(dir_path, output_sheet_name: str = 'Sheet1', output_excel_name: str = 'merge2sheet'):
    poexcel.merge2sheet(dir_path, output_sheet_name, output_excel_name)


# 搜索excel中指定内容的文件、行数、内容详情
# PR内容 & 作者：https://gitee.com/CoderWanFeng/python-office/pulls/10
# @except_dec()
# @instruction
def find_excel_data(search_key: str, target_dir: str):
    poexcel.find_excel_data(search_key, target_dir)


# 按指定列的内容，拆分excel
# PR内容 & 作者：：https://gitee.com/CoderWanFeng/python-office/pulls/11
# @except_dec()
# @instruction
def split_excel_by_column(filepath: str, column: int, worksheet_name: str = None):
    poexcel.split_excel_by_column(filepath, column, worksheet_name)


# @instruction
def excel2pdf(excel_path, pdf_path, sheet_id: int = 0):
    """
    将指定的Excel文件的指定工作表转换为PDF文件。
    视频：https://www.bilibili.com/video/BV1A84y1N7or/
    :param excel_path: str, Excel文件的路径。
    :param pdf_path: str, 转换后生成的PDF文件的路径。
    :param sheet_id: int, 工作表的索引，默认为0，表示第一个工作表。
    :return: None
    """
    poexcel.excel2pdf(excel_path, pdf_path, sheet_id)


# @instruction
def merge2excel(excel_path, output='merge2excel.xlsx'):
    poexcel.merge2excel(excel_path, output)
