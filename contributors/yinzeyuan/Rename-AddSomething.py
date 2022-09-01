# import pathlib
#
#
# def file_name_insert_content(file_path, insert_position: int, insert_content: str):
#     """
#
#     :param Path: 文件存放路径
#     :param InsertPosition: 插入位置（内容将插入在此之后，如果输入位置大于文件主名长度将插入在末尾）
#     :param InsertContent: 插入内容
#     """
#     Path = pathlib.Path(file_path).resolve()
#     if Path.is_dir():
#         FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
#         for FileName in FileNameList:
#             if FileName.is_file():  # 判断是否为文件，只对文件进行操作
#                 FileNameExtension = "".join(list(FileName.suffixes))
#                 FileNameRoot = FileName.name.replace(FileNameExtension, "")
#                 # 分离文件主名和扩展名，防止对扩展名进行操作
#                 FileNameFormer = FileNameRoot[:insert_position:]
#                 FileNameLatter = FileNameRoot[insert_position::]
#                 # 拆分文件主名
#                 NewFileName = FileNameFormer + insert_content + FileNameLatter + FileNameExtension  # 合并文件名
#                 if not Path.joinpath(NewFileName).is_file():
#                     FileName.rename(Path.joinpath(NewFileName))
#                 else:
#                     print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
#     else:
#         print("请输入文件夹路径")
#
#
# def file_name_add_prefix(file_path, prefix_content: str):
#     """
#
#     :param Path: 文件存放路径
#     :param PrefixContent: 前缀内容
#     """
#     Path = pathlib.Path(file_path).resolve()
#     if Path.is_dir():
#         FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
#         for FileName in FileNameList:
#             if FileName.is_file():  # 判断是否为文件，只对文件进行操作
#                 NewFileName = prefix_content + FileName.name  # 合并文件名
#                 if not Path.joinpath(NewFileName).is_file():
#                     FileName.rename(Path.joinpath(NewFileName))
#                 else:
#                     print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
#     else:
#         print("请输入文件夹路径")
#
#
# def file_name_add_postfix(file_path, postfix_content: str):
#     """
#
#     :param Path: 文件存放路径
#     :param PostfixContent: 后缀内容
#     """
#     Path = pathlib.Path(file_path).resolve()
#     if Path.is_dir():
#         FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
#         for FileName in FileNameList:
#             if FileName.is_file():  # 判断是否为文件，只对文件进行操作
#                 FileNameExtension = "".join(list(FileName.suffixes))
#                 FileNameRoot = FileName.name.replace(FileNameExtension, "")
#                 # 分离文件主名和扩展名
#                 NewFileName = FileNameRoot + postfix_content + FileNameExtension  # 合并文件名
#                 if not Path.joinpath(NewFileName).is_file():
#                     FileName.rename(Path.joinpath(NewFileName))
#                 else:
#                     print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
#     else:
#         print("请输入文件夹路径")
#
#
# if __name__ == '__main__':
#     # FileNameAddPostfix(Path=r'D:\workplace\code\test\output\test', PostfixContent='2022')
#     file_name_insert_content(Path=r'D:\workplace\code\test\output\test', InsertPosition=2, InsertContent='888')
