# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/16 19:44 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV1A84y1N7or/
'''

import office

# 假设Excel共有3个工作表,表名分别为 sheet1 sheet2 sheet3

# 下列的路径应该是到目录而非文件.excel_path到文件不影响使用.pdf_path到文件实际会多一层目录
# 例如下面的示例,最终生成的pdf文件路径为 D:\test\程序员晚枫.pdf\程序员晚枫.pdf

# 转换整个工作簿
office.excel.excel2pdf(excel_path=r"D:\test\程序员晚枫.xlsx",
                       pdf_path=r"D:\test\程序员晚枫.pdf")

# 仅转换第一个工作表 方法1
office.excel.excel2pdf(excel_path=r"D:\test\程序员晚枫.xlsx",
                       pdf_path=r"D:\test\程序员晚枫.pdf",
                       include=1)

# 仅转换第一个工作表 方法2
office.excel.excel2pdf(excel_path=r"D:\test\程序员晚枫.xlsx",
                       pdf_path=r"D:\test\程序员晚枫.pdf",
                       exclude=[2, 3])

# 仅转换第一个工作表 方法3
office.excel.excel2pdf(excel_path=r"D:\test\程序员晚枫.xlsx",
                       pdf_path=r"D:\test\程序员晚枫.pdf",
                       exclude=["sheet2", "sheet3"]  # 这里也可以是 [ 2 , "sheet3"]
                       )

# 仅转换第一和第三个工作表 方法1
office.excel.excel2pdf(excel_path=r"D:\test\程序员晚枫.xlsx",
                       pdf_path=r"D:\test\程序员晚枫.pdf",
                       include=[1, 3])

# 仅转换第一和第三个工作表 方法2
office.excel.excel2pdf(excel_path=r"D:\test\程序员晚枫.xlsx",
                       pdf_path=r"D:\test\程序员晚枫.pdf",
                       include=["sheet1", "sheet3"]  # 这里也可以是 [ 1 , "sheet3"]
                       )

# 仅转换第一和第三个工作表 方法3
office.excel.excel2pdf(excel_path=r"D:\test\程序员晚枫.xlsx",
                       pdf_path=r"D:\test\程序员晚枫.pdf",
                       exclude=2
                       )
