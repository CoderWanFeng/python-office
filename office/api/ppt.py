# -*- coding:utf-8 -*-

# 导入处理PPT的模块
import poppt


# PPT转换为PDF的功能函数
# todo：输入文件路径
def ppt2pdf(path: str, output_path=r'./'):
    # 调用poppt模块的ppt2pdf方法进行转换
    poppt.ppt2pdf(path, output_path)


# PPT转换为图片的功能函数
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
    # 调用poppt模块的ppt2img方法进行转换
    poppt.ppt2img(input_path, output_path, merge)


# 合并多个PPT文件的功能函数
def merge4ppt(input_path: str, output_path=r'./', output_name: str = 'merge4ppt.pptx'):
    # 调用poppt模块的merge4ppt方法进行合并
    poppt.merge4ppt(input_path, output_path, output_name)
