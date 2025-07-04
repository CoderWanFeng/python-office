# -*- coding:utf-8 -*-


import poppt


# todo：输入文件路径
def ppt2pdf(path: str, output_path=r'./'):
    poppt.ppt2pdf(path, output_path)


def ppt2img(input_path: str, output_path=r'./', merge: bool = False):
    """
    PPT转图片，可以转为长图
    Args:
        input_path: 存放PPT的位置，
                    转换单个文件 → 可以写文件的路径
                    转换单个文件 → 写文件夹的路径
        output_path: 结果图片的存储位置，可以不写，默认代码目录
        merge: True → 转为1张图片
            False → PPT有多少张，就转为多少张图片

    Returns: None

    """
    poppt.ppt2img(input_path, output_path, merge)


def merge4ppt(input_path: str, output_path=r'./', output_name: str = 'merge4ppt.pptx'):
    poppt.merge4ppt(input_path, output_path, output_name)
