# -*- coding: UTF-8 -*-


# pip install python-office
import office

office.ppt.ppt2img(input_path=r'./test_files/ppt2img/程序员晚枫-2.pptx',
                   output_path=r'./test_files/ppt2img/output',
                   merge=True)

"""
PPT转图片
Args:
    input_path: 存放PPT的位置，
                转换单个文件 → 可以写文件的路径
                转换单个文件 → 写文件夹的路径
    output_path: 结果图片的存储位置，可以不写，默认代码目录
    merge: True → 转为1张图片
        False → PPT有多少张，就转为多少张图片

Returns: None

"""
