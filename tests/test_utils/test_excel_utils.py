import pandas as pd
import os
import re

"""
    此类为excel测试用例的工具类
"""


def file_exist(file_path):
    """
    判断文件是否存在

    Args:
        file_path: 文件路径  str
    """
    return os.path.exists(file_path)


def get_colum_content(file_path, column_index, sheet_name='Sheet1'):
    """
    获取excel中

    Args:
        file_path: 文件路径  str
        column_index: 需要查询标题的列索引，从0开始 int
        sheet_name: sheet名称 str
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    headers = df.columns.tolist()
    return headers[column_index]


def is_chinese_chars_regex(s):
    """
    字符串是否是全中文

    Args:
        s: 字符串 str
    """
    pattern = re.compile(r'[\u4e00-\u9fff]')
    matches = pattern.findall(s)
    return len(matches) > 1


def get_content(file_path, row_index, col_index, sheet_name='Sheet1'):
    """
    获取excel文件具体行列的值

    Args:
        file_path: 文件路径  str
        row_index: 需要查询的行索引，从0开始 int
        col_index: 需要查询的列索引，从0开始 int
        sheet_name: sheet名称 str
    """
    df = pd.read_excel(file_path, sheet_name)
    first_value = df.iloc[row_index, col_index]
    return first_value


def delete_file(file_path):
    """
    删除文件

    Args:
        file_path: 需要删除的文件路径  str
    """
    os.remove(file_path)


def get_file_by_suffix(dir_path, suffix):
    """
    获取目录下固定后缀的文件名

    Args:
        dir_path: 目录名称 str
        suffix: 后缀名称 str
    """
    xlsx_files = []
    file_names = os.listdir(dir_path)
    for file_name in file_names:
        if file_name.endswith(suffix):
            xlsx_files.append(file_name)
    return xlsx_files


def get_all_sheet_names(file_path):
    """
    获取excel文件的所有sheet名称

    Args:
        file_path: 文件路径  str
    """
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    return sheet_names


def get_filter_names(file_path, column_index):
    """
    获取excel文件中某列的所有值分类

    Args:
       file_path: 文件路径  str
       column_index: 需要筛选的列索引，从0开始 int
   """
    df = pd.read_excel(file_path)
    column_name = df.columns[column_index]
    # 除去残留nan值
    df = df.dropna(subset=[column_name])
    categories = df[column_name].unique().tolist()
    return categories


def get_latest_file(dir_path):
    """
    获取目录下最新生成的文件路径

    Args:
       dir_path: 目录路径  str
   """
    latest_file = None
    latest_ctime = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            ctime = os.path.getctime(file_path)
            if ctime > latest_ctime:
                latest_ctime = ctime
                latest_file = file_path
    return latest_file

