# -*- coding: UTF-8 -*-

# 导入 poexcel 模块，该模块封装了对 Excel 文件的常用操作
import poexcel

# 调用 poexcel 模块中的 merge2sheet 函数
# 该函数的作用是将指定文件夹下的多个 Excel 文件合并到一个 Excel 文件的不同工作表中
# 参数说明：
#   - dir_path: 存放多个 Excel 文件的文件夹路径（原始字符串格式，避免转义问题）
#   - output_sheet_name: 输出 Excel 中每个子表的命名规则或固定名称（例如根据文件名命名或统一命名）
#   - output_excel_name: 合并后的输出 Excel 文件路径及文件名（原始字符串格式）
poexcel.merge2sheet(
    dir_path=r'D:\workplace\code\github\python-office\tests\test_files\excel\merge2sheet',
    output_sheet_name=r'platform', 
    output_excel_name=r'./output/merge2sheet'
)