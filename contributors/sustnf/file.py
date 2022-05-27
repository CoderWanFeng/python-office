# -*- coding:utf-8 -*-

import os
import shutil
import sys
from typing import List

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout



# 判断文件夹中是否有超过固定大小的文件
# 可对超过具体大小的文件做删除,移动等操作,后续优化
# folder:文件夹
# size:大小(M)
def screen_file(folder, size:int):
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



# 判断文件夹中指定后缀的文件(后缀可多写List类型)['.exe','.txt','.md']
def screen_suffix(folder, suffix:List):
    reslist = []
    for s in range(len(suffix)):
            # with HiddenPrints():
                one_suffix(folder, suffix[s], reslist)
    for r in reslist:
        print(r)
        

# 判断文件夹中指定后缀的文件
def one_suffix(folder, suf, res=None):
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
