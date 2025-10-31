# -*- coding: UTF-8 -*-
"""Excel处理功能模块。

该模块提供了丰富的Excel文件处理功能，包括数据模拟、文件合并拆分、格式转换等。

主要功能：
- fake2excel: 自动创建Excel并模拟数据
- merge2excel: 多个Excel合并到一个文件的不同sheet中
- sheet2excel: 同一个Excel的不同sheet拆分为不同文件
- merge2sheet: 多个Excel的多个sheet自动合并
- find_excel_data: 搜索Excel中指定内容
- split_excel_by_column: 按指定列拆分Excel
- excel2pdf: Excel转PDF格式

Author:
    程序员晚枫

Project:
    https://www.python-office.com
"""

import poexcel


def fake2excel(columns=['name'], rows=1, path='./fake2excel.xlsx', language='zh_CN'):
    """自动创建Excel，并且模拟数据。
    
    视频：https://www.bilibili.com/video/BV1wr4y1b7uk/
    
    Args:
        columns (list): 列名。可以模拟的列有：http://python4office.cn/python-office/fake2excel/
        rows (int): 生成多少行数据。默认值：1
        path (str): 生成的Excel的位置和名称
        language (str): 数据用什么语言，默认是中文，可以填english
    
    Returns:
        None
    """
    poexcel.fake2excel(columns, rows, path, language)


def merge2excel(dir_path, output_file='merge2excel.xlsx'):
    """多个excel，合并到一个excel的不同sheet中。
    
    文档：https://mp.weixin.qq.com/s/3ZhZZfGlpNhszCWnOBeklg
    视频：https://www.bilibili.com/video/BV1Th4y1Y7kd/
    
    Args:
        dir_path (str): 包含多个Excel文件的目录路径
        output_file (str): 合并后的Excel文件路径，默认为'merge2excel.xlsx'
    
    Returns:
        None
    """
    poexcel.merge2excel(dir_path, output_file)


#

def sheet2excel(file_path, output_path='./'):
    """同一个excel里的不同sheet，拆分为不同的excel文件。
    
    视频：https://www.bilibili.com/video/BV1714y147Ao/
    
    Args:
        file_path (str): 需要拆分的Excel文件路径
        output_path (str): 拆分后文件的输出目录，默认为当前目录
    
    Returns:
        None
    """
    poexcel.sheet2excel(file_path, output_path)


def merge2sheet(dir_path, output_sheet_name: str = 'Sheet1', output_excel_name: str = 'merge2sheet'):
    """实现多个Excel的多个sheet的自动合并。
    
    文档：https://mp.weixin.qq.com/s/qQxIsSPHfILTCxZ8PBv6QA
    
    Args:
        dir_path (str): 包含多个Excel文件的目录路径
        output_sheet_name (str): 合并后的sheet名称，默认为'Sheet1'
        output_excel_name (str): 合并后的Excel文件名，默认为'merge2sheet'
    
    Returns:
        None
    """
    poexcel.merge2sheet(dir_path, output_sheet_name, output_excel_name)


# PR内容 & 作者：https://gitee.com/CoderWanFeng/python-office/pulls/10
def find_excel_data(search_key: str, target_dir: str):
    """搜索excel中指定内容的文件、行数、内容详情。
    
    视频：https://www.bilibili.com/video/BV1Bd4y1B7yr/
    
    Args:
        search_key (str): 需要搜索的关键词
        target_dir (str): 搜索的目录路径
    
    Returns:
        None
    """
    poexcel.find_excel_data(search_key, target_dir)


# PR内容 & 作者：：https://gitee.com/CoderWanFeng/python-office/pulls/11

def split_excel_by_column(filepath: str, column: int, worksheet_name: str = None):
    """按指定列的内容，拆分excel。
    
    Args:
        filepath (str): 需要拆分的Excel文件路径
        column (int): 按哪一列的内容进行拆分
        worksheet_name (str, optional): 指定工作表名称，默认为None表示第一个工作表
    
    Returns:
        None
    """
    poexcel.split_excel_by_column(filepath, column, worksheet_name)


def excel2pdf(excel_path, pdf_path, sheet_id: int = 0):
    """将指定的Excel文件的指定工作表转换为PDF文件。
    
    视频：https://www.bilibili.com/video/BV1A84y1N7or/
    
    Args:
        excel_path (str): Excel文件的路径
        pdf_path (str): 转换后生成的PDF文件的路径
        sheet_id (int): 工作表的索引，默认为0，表示第一个工作表
    
    Returns:
        None
    """
    poexcel.excel2pdf(excel_path, pdf_path, sheet_id)
