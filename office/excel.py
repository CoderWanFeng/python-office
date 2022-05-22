#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: excel.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 excel 的自动化操作
#############################################

import os
from faker import Faker
import pandas as pd
from alive_progress import alive_bar

from utils import pandas_mem


def fake2excel(columns=['name'], rows=1, language='zh_CN', path='./fake2excel.xlsx', ):
    """
    @Author & Date  : CoderWanFeng 2022/5/13 0:12
    @Desc  : columns:list，每列的数据名称，默认是名称
            rows：多少行，默认是1
            language：什么语言，可以填english，默认是中文
            path：输出excel的位置，有默认值
    """
    # 可以选择英语
    if language.lower() == 'english':
        language = 'en_US'
    # 开始造数
    fake = Faker(language)
    excel_dict = {}
    with alive_bar(len(columns) * rows) as bar:
        for column in columns:
            excel_dict[column] = list()
            # excel_dict[column] = map(lambda x: eval('fake.{func}()'.format(func=x)), [column] * rows) # 使用map，会报错
            while len(excel_dict[column]) < rows:
                excel_dict[column].append(eval('fake.{func}()'.format(func=column)))
                bar()
        # 用pandas，将模拟数据，写进excel里面
        writer = pd.ExcelWriter(path)
        data = pd.DataFrame(excel_dict)
        data = pandas_mem.reduce_pandas_mem_usage(data)
        data.to_excel(writer, index=False)
        writer.save()


def concat(file_dir:str, out_path:str="./merged.xlsx"):
    """to concatenate all excel sheets in one folder into one excel sheet
       将一个文件夹内所有的excel文件全部合并为一个文件, 通过增加行进行操作。
    
    Author: Bob, 2022/5/22

    Args:
        file_dir (str): the folder path containing all excel
        out_path (str, optional): the output path. Defaults to "./merged.xlsx".

    Example: 
        >>> concat("./documents", "test.xlsx")
    """
    assert isinstance(file_dir, str)
    assert isinstance(out_path, str)
    assert out_path.endswith("xlsx")
    
    if not os.path.exists(file_dir):
        raise ValueError(f"{file_dir} does not exist!")
    if not os.path.isdir(file_dir):
        raise ValueError(f"{file_dir} must be a dir(folder)!")

    path_list = os.listdir(file_dir)
    excel_list = (
        pd.read_excel(path).astype(str)
        for path in path_list if path.endswith("xlsx")
        )

    if len(excel_list) == 0:
        raise ValueError(f"there is no excel file in {file_dir}")

    data_frame = pd.concat(excel_list)
    data_frame.to_excel(out_path, index=False)


def merge(file_dir:str, out_path:str="./merged.xlsx"):
    """to merge several sheets colomns by essential key word 
    将拥有同样关键字段的例如(名字、学号)等将多个表格的列进行融合
    
    Author: Bob, 2022/5/22

    Args:
        file_dir (str): the folder path containing all excel
        out_path (str, optional): the output path. Defaults to "./merged.xlsx".

    """
    ...



# def merge():
if __name__ == "__main__":
    path1 = "/Users/bob/Desktop/test1.xlsx"
    path2 = "/Users/bob/Desktop/test2.xlsx"
    concat(path1, path2)