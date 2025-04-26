# -*- coding: UTF-8 -*-

# 导入这个库：python-office，简写为office
import office

# 一行代码，实现转换
office.pdf.pdf2imgs(
    pdf_path='D://程序员晚枫的文件夹//程序员晚枫.pdf',
    out_dir='./点赞+关注文件夹'
)
# 参数说明：
# pdf_path = 你的PDF文件的地址
# out_dir = 转换后的图片存放地址，可以不填，默认是PDF的地址