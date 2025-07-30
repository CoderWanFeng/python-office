# -*- coding: UTF-8 -*-

# 导入 office 模块，这是一个用于处理办公文档（如 Excel、Word、PPT）的 Python 工具库
import office

# 调用 office 模块中的 excel 子模块下的 merge2excel 函数
# 该函数的作用是将指定文件夹下的所有 Excel 文件（.xlsx / .xls）合并为一个 Excel 文件
# 参数说明：
#   - dir_path: 存放多个 Excel 文件的文件夹路径，支持相对路径或绝对路径
#               此处使用的是相对路径 '../../contributors/bulabean'
#   - output_file: 合并后输出的 Excel 文件名（字符串），例如 'test_merge2excel.xlsx'
#                  输出路径默认为当前脚本所在目录，除非指定完整路径
office.excel.merge2excel(
    dir_path=r'../../contributors/bulabean',
    output_file='test_merge2excel.xlsx'
)