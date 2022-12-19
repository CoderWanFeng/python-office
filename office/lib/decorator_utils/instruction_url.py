#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: instruction_url.py
# Mail: 1957875073@qq.com
# Created Time:  2022-12-17 08:14:34
# Description: 有关 方法说明 的装饰器
#############################################

# 每个文件的具体方法说明
from functools import wraps

from office.lib.conf.CONST import SPLIT_LINE

email_dict = {}
import os

excel_dict = {"fake2excel": "https://www.bilibili.com/video/BV1wr4y1b7uk",
              "find_excel_data": "https://www.bilibili.com/video/BV1Bd4y1B7yr",
              "merge2excel": "https://www.bilibili.com/video/BV1714y147Ao",
              "merge2sheet": "",
              "sheet2excel": "https://mp.weixin.qq.com/s/dAx6JEbj5OlVnCcxokCzTQ",
              "split_excel_by_column": "",
              }
image_dict = {"add_watermark": "https://www.bilibili.com/video/BV1jT411T7n9",
              "decode_qrcode": "https://mp.weixin.qq.com/s/Z_RcTRYxUFpCQBGpShO0ig",
              "down4img": "https://mp.weixin.qq.com/s/P6pRm1VX8bGYepC8O4Bt4Q",
              "image2gif": "",
              "img2Cartoon": "https://mp.weixin.qq.com/s/5Eyk2j20jzSaVcr1DTsfvw",
              "pencil4img": "https://www.bilibili.com/video/BV1rP411N7ao",
              "txt2wordcloud": "https://www.bilibili.com/video/BV1Me4y1h7Ku/?spm_id_from=333.999.0.0",
              }
md_dict = {}
ocr_dict = {}
pdf_dict = {"add_img_water": "",
            "add_watermark": "https://www.bilibili.com/video/BV1Se411T7au",
            "add_watermark_by_parameters": "",
            "decrypt4pdf": "https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA",
            "encrypt4pdf": "https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA",
            "merge2pdf": "https://mp.weixin.qq.com/s/9erh3W3WCD36Axj70pRvog",
            "pdf2docx": "https://mp.weixin.qq.com/s/eTwtTXLAudRQmyhE4LY_Dg",
            "pdf2imgs": "https://mp.weixin.qq.com/s/tvHZIBGcrMBLTLB4u23Mow",
            "txt2pdf": "", }
ppt_dict = {"ppt2pdf": "https://mp.weixin.qq.com/s/T31F-U5AdDd3D-61b_K5Qg", }
tools_dict = {"create_article": "https://mp.weixin.qq.com/s/guBtZHyUyybGNOqzZke1kQ",
              "lottery8ticket": "https://mp.weixin.qq.com/s/Q6JgW06hMUSik0DqGD0rOA",
              "net_speed_test": "https://www.bilibili.com/video/BV1fD4y1x7ZE",
              "passwordtools": "https://www.bilibili.com/video/BV1Ce4y1p7iV",
              "pwd4wifi": "https://blog.csdn.net/weixin_42321517/article/details/126677254",
              "qrcodetools": "https://www.bilibili.com/video/BV1pd4y1b716/?spm_id_from=333.999.0.0",
              "transtools": "https://www.bilibili.com/video/BV11d4y1k7Mn",
              "url2ip": "https://cloud.tencent.com/developer/article/2022777",
              "weather": "https://mp.weixin.qq.com/s/NVn8NNtOS3AfOyl75JTaNg",
              }
video_dict = {"audio2txt": "https://mp.weixin.qq.com/s/Ug_IFSEQBzDshe7KuFckTQ",
              "video2mp3": "https://mp.weixin.qq.com/s/Ug_IFSEQBzDshe7KuFckTQ",
              }
web_dict = {}
wechat_dict = {"chat_by_keywords": "https://www.bilibili.com/video/BV1fV4y1M7ju",
               "receive_message": "",
               "send_file": "https://www.bilibili.com/video/BV1te4y1y7Ro",
               "send_message": "https://www.bilibili.com/video/BV1Jt4y1j7F1",
               "send_message_by_time": "https://www.bilibili.com/video/BV1m8411b7LZ", }
word_dict = {"docx2pdf": "https://mp.weixin.qq.com/s/eBn3N_FEx1dlC_-ttmlOwg", }

file_dict = {"search_by_content": "https://mp.weixin.qq.com/s/rvU7O3zHJ-YEd2YU0Z4pew",
             "add_line_by_type": "",
             "file_name_add_postfix": "",
             "file_name_add_prefix": "",
             "file_name_insert_content": "",
             "output_file_list_to_excel": "",
             "replace4filename": "https://www.bilibili.com/video/BV12r4y187Yj",
             "search_specify_type_file": "",
             }

# 有多少文件需要说明
instruction_file_dict = {
    "excel.py": excel_dict,
    "image.py": image_dict,
    "pdf.py": pdf_dict,
    "ppt.py": ppt_dict,
    "tools.py": tools_dict,
    "video.py": video_dict,
    "wechat.py": wechat_dict,
    "word.py": word_dict,
    "file.py": file_dict,
}


def instruction(func):
    @wraps(func)
    def instruction_wrapper(*args, **kwargs):
        func_filename = os.path.basename(func.__code__.co_filename)  # 取出方法所在的文件名
        # 如果有这个文件，并且已经配置了方法名对应的说明链接，则打印出来
        if func_filename in instruction_file_dict.keys() and instruction_file_dict[func_filename][func.__name__]:
            print(
                f'正在运行：office.{os.path.basename(func_filename)[:-3]}.{func.__name__} , 这个方法的使用说明：{instruction_file_dict[func_filename][func.__name__]}')
            print(SPLIT_LINE)
        instruction_res = func(*args, **kwargs)
        return instruction_res

    return instruction_wrapper


#############################################
# 以下是本文件的工具模块，用来更新方法和链接
from inspect import getmembers, isfunction, ismethod, isclass


# 获取模块包含的方法名
def get_method_name(file):
    for method_name in getmembers(file):
        if isfunction(method_name[1]):
            print(f'"{method_name[0]}":"",')


from office import api

if __name__ == '__main__':  # TODO:完善这个装饰器
    get_method_name(file=api.word)
