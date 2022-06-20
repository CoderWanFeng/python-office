#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: excel.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 excel 的自动化操作
#############################################
import math

import numpy
from faker import Faker
import pandas as pd
from alive_progress import alive_bar

from src.utils import pandas_mem


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
        data = pd.DataFrame(excel_dict)
        data = pandas_mem.reduce_pandas_mem_usage(data)
        __excelWriter__(path=path, data=data)


#############################################
# Author: han_ying_feng
# Mail: gyuanhao@163.com
# Created Time:  2022-05-26 12:13:09
# Description: 将想要添加的DataFrame 写入到相应Path的Excel文件中
#############################################
def __excelWriter(path, data: pd.DataFrame):
    # 使用文件路径创建ExcelWriter对象
    writer = pd.ExcelWriter(path)
    # 将数据写入到writer对象中
    data.to_excel(writer, index=False)
    # 保存文件
    writer.save()
    # 关闭资源
    writer.close()


#############################################
# Author: han_ying_feng
# Mail: gyuanhao@163.com
# Created Time:  2022-05-26 12:13:09
# Description: 根据表名读取Excel数据
#############################################
def read_all_excel(excel_file_path, sheet_name='Sheet1', header=0) -> pd.DataFrame:
    return read_cols_to_name(excel_file_path, sheet_name=sheet_name, header=header)


#############################################
# Author: han_ying_feng
# Mail: gyuanhao@163.com
# Created Time:  2022-05-26 12:13:09
# Description: 读取Excel某列数据
#############################################
def read_cols_to_name(excel_file_path, cols_name=None, header=0, sheet_name='Sheet1') -> pd.DataFrame:
    return pd.read_excel(excel_file_path, usecols=cols_name, header=header, sheet_name=sheet_name)


#############################################
# Author: han_ying_feng
# Mail: gyuanhao@163.com
# Created Time:  2022-05-26 12:13:03
# Description: 计算某列数据的和，并返回
#############################################
def sum_by_cols(excel_file_path, cols_name=[], header=0, sheet_name='Sheet1'):
    # 读取数据表
    cols_data_list = read_cols_to_name(excel_file_path, cols_name=cols_name, header=header, sheet_name=sheet_name)
    # 获取数据表中的数据
    values = cols_data_list.values
    # 将获取到的数据更改为list
    num_list = []
    for item in values:
        # 判断整列中的数据是否是数字类型
        if type(item[0]) == int or type(item[0]) == numpy.int64:
            num_list.append(item[0])
    return math.fsum(num_list)


#############################################
# Author: han_ying_feng
# Mail: gyuanhao@163.com
# Created Time:  2022-05-26 12:13:03
# Description: 将一段数据添加到指定列中的单元格内
#############################################
def append_by_cols(data, excel_file_path, cols_name=[], sheet_name='Sheet1', header=0, axis=0):
    # 读取整个表的内容
    read_data = read_all_excel(excel_file_path, sheet_name, header=header)
    # 创建新数据的Frame
    df = pd.DataFrame(data=[data], columns=cols_name)
    # 新数据与读取到的整个表的数据合并
    data = pd.concat([read_data, df], ignore_index=True, axis=axis)
    # 写入原文件中
    __excelWriter__(excel_file_path, data)
