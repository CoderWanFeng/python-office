# -*- coding:utf-8 -*-

# 导入处理PPT的模块
import poppt


def ppt2pdf(path: str, output_path=r'./'):
    """PPT转换为PDF。
    
    Args:
        path (str): PPT文件路径
        output_path (str, optional): 输出PDF文件路径，默认为当前目录
    
    Returns:
        None
    """
    poppt.ppt2pdf(path, output_path)


def ppt2img(input_path: str, output_path=r'./', merge: bool = False):
    """PPT转图片，可以转为长图。
    
    Args:
        input_path (str): 存放PPT的位置，转换单个文件可以写文件的路径，转换文件夹可以写文件夹的路径
        output_path (str, optional): 结果图片的存储位置，默认为当前目录
        merge (bool, optional): True转为1张图片，False转为多张图片，默认为False
    
    Returns:
        None
    """
    poppt.ppt2img(input_path, output_path, merge)


def merge4ppt(input_path: str, output_path=r'./', output_name: str = 'merge4ppt.pptx'):
    """合并多个PPT文件。
    
    Args:
        input_path (str): 输入PPT文件路径
        output_path (str, optional): 输出PPT文件路径，默认为当前目录
        output_name (str, optional): 合并后的PPT文件名，默认为'merge4ppt.pptx'
    
    Returns:
        None
    """
    poppt.merge4ppt(input_path, output_path, output_name)
