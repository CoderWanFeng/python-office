# -*- coding:utf-8 -*-

import hashlib
import os


# 文件md5校验
# source_file:文件1
# target_file:文件2
def file_compare(source_file,target_file):
    s = open(source_file, "br")
    t = open(target_file, "br")
    md5_source_file = hashlib.md5(s.read()).hexdigest()
    md5_target_file = hashlib.md5(t.read()).hexdigest()
    if md5_source_file == md5_target_file:
        print("文件%s和文件%s\tmd5值相同" % (source_file, target_file))
    else:
        print("文件%s和文件%s\tmd5值不相同" % (source_file, target_file))


# 文件夹(子目录)md5校验。生成.csv文档,用于查看对比结果(使用excel打开即可)
# 目前校验相同和不相同都在同一文件下,后续优化
# source_folder:文件夹1
# target_folder:文件夹2
# result.csv生成在执行目录下
def folder_compare(source_folder,target_folder):
    output_file = os.getcwd() + "\\result.csv"
    # 判断是否已指定的路径分隔符结尾
    if source_folder.endswith(os.path.sep) and len(source_folder) > 1:
        source_folder = source_folder[:-1]
    if target_folder.endswith(os.path.sep) and len(target_folder) > 1:
        target_folder = target_folder[:-1]
    # 遍历文件或者目录
    t = os.walk(source_folder, topdown=True)
    # os.walk返回一个三元组
    # path:当前正在遍历的这个文件夹的本身的地址, 
    # dirs:是一个list,内容是该文件夹中所有的目录的名字(不包括子目录), 
    # file_names:是一个list,内容是该文件夹中所有的文件(不包括子目录),
    # topdown参数为真，walk会遍历source_folder文件夹,与source_folder文件夹中每一个子目录
    output_file = open(output_file, "w+")
    for path, dirs, file_names in t:
        for filename in file_names:
            source_file = os.path.join(path, filename)
            # 链接路径
            target_file = source_file.replace(source_folder, target_folder)
            f = open(source_file, "br")
            # print(source_file)
            # md5值
            md5_source_file = hashlib.md5(f.read()).hexdigest()
            f.close()
            if os.path.exists(target_file):
                f = open(target_file, "br")
                md5_target_file = hashlib.md5(f.read()).hexdigest()
                f.close()
                if md5_source_file == md5_target_file:
                    try:
                        output_file.write(
                            "%s,%s,%s,%s,%s\n" % (source_file, md5_source_file, target_file, md5_target_file, "true")
                        )
                    except:
                        output_file.write(
                            ",%s,,%s,%s\n" % ("", md5_source_file, "", md5_target_file, "true")
                        )
                    print("%s 和 %s 相等,记录在校验结果中" % (source_file, target_file))
                else:
                    try:
                        output_file.write(
                            "%s,%s,%s,%s,%s\n" % (source_file, md5_source_file, target_file, md5_target_file, "false")
                        )
                    except:
                        output_file.write(
                            ",%s,,%s,%s\n" % ("", md5_source_file, "", md5_target_file, "false")
                        )
                    print("%s 和 %s 不相等,记录在校验结果中" % (source_file, target_file))
            else:
                try:
                    output_file.write(
                        "%s,%s,%s,%s,%s\n" % (source_file, md5_source_file, "not exists", "", "false")
                        )
                except:
                    output_file.write(
                        ",%s,,%s,%s\n" % ("", md5_source_file, "", "not exists", "false")
                    )
                print("%s不存在target(目标文件夹),记录在校验结果中" % source_file)
    output_file.close()
    print("校验完成,结果请查看%s文件" % (output_file.name))

# file_compare("D:\\blog\\bin\\yarn","C:\\Users\\DUZUN\\Desktop\\bin\\yarn")
# folder_compare("D:\\blog\\bin","C:\\Users\\DUZUN\\Desktop\\bin")