# -*- coding:utf-8 -*-

import os
import shutil
import sys
from typing import List

class HiddenPrints:
    """上下文管理器，用于隐藏print输出。"""
    
    def __enter__(self):
        """进入上下文时隐藏输出。"""
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时恢复输出。"""
        sys.stdout.close()
        sys.stdout = self._original_stdout



def screen_file(folder: str, size: int) -> None:
    """筛选文件夹中超过指定大小的文件。
    
    Args:
        folder (str): 文件夹路径
        size (int): 文件大小阈值（单位：MB）
    """
    size = size *1024 *1024
    res = []
    reslist = []
    for path, dirs, file_names in os.walk(folder, topdown=True):
        for filename in file_names:
            res.append(os.path.join(path, filename))
    for r in res:
        if os.path.getsize(r) > size:
            reslist.append(r)
    if len(reslist) == 0:
        print("没有超过%sM大小的文件" % (size/1024/1024))
    else:
        print("有超过%sM大小的文件" % (size/1024/1024))
        for r in reslist:
            print(r)

# screen_file("E:\\",200)



def screen_suffix(folder: str, suffix: List[str]) -> None:
    """筛选文件夹中指定后缀的文件。
    
    Args:
        folder (str): 文件夹路径
        suffix (List[str]): 文件后缀列表
    """
    reslist = []
    for s in range(len(suffix)):
            # with HiddenPrints():
                one_suffix(folder, suffix[s], reslist)
    for r in reslist:
        print(r)
        

def one_suffix(folder: str, suf: str, res: list = None) -> None:
    """筛选文件夹中指定后缀的文件（单个后缀）。
    
    Args:
        folder (str): 文件夹路径
        suf (str): 文件后缀
        res (list, optional): 结果列表
    """
    res = []
    datanames = os.listdir(folder)
    for dataname in datanames:
        t = os.path.join(folder, dataname)
        if os.path.isfile(t):
            if dataname.endswith(suf):
                    res.append(os.path.join(folder, dataname))
        elif os.path.isdir(t):
            one_suffix(t, suf, res)
    for r in res:
        print(r)


# screen_suffix("E:\项目", ['.txt','.md','.js'])
# one_suffix("E:\项目",".md")
