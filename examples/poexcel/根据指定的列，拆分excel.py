# -*- coding: UTF-8 -*-

# 导入处理 Excel 的模块（poexcel 是一个用于操作 Excel 的 Python 工具库）
import poexcel

# 调用 poexcel 模块中的函数：split_excel_by_column
# 该函数的作用是根据指定列的值，将一个 Excel 文件拆分成多个子文件
# 参数说明：
#   - filepath: 待拆分的原始 Excel 文件路径（必须为字符串，使用原始字符串 r'' 避免转义问题）
#   - column: 根据哪一列进行拆分（索引从 0 开始，column=1 表示第二列）
#   - worksheet_name: 指定要操作的工作表名称，默认为所有工作表，若指定则只处理该工作表
poexcel.split_excel_by_column(
    filepath=r'D:\workplace\code\github\python-office\demo\poexcel\excel\split_excel_by_column.xlsx',
    column=1,
    worksheet_name='platform'
)