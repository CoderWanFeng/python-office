# 导入re模块
import re

strs = '''17:28
          检测结果查询
          检测结果【阴性】
          姓名 朱卫军
          采样时间 2022-04-08 12：28
          试剂编码 48
          检测项目 新冠抗原'''

name = re.findall('(?<=姓名 ).*',strs)
time = re.findall('(?<=采样时间 ).*',strs)
result = re.findall('(?<=【).*(?=】)',strs)
print(name)
print(time)
print(result)