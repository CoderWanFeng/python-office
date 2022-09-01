# import pathlib
#
#
# def search_specify_type_file(file_path, file_type: str):
#     '''
#
#     :param file_path:目标路径
#     :param file_type:需要查找的文件类型
#     '''
#     print("开始查找")
#     i = 0  # 计数变量
#     file_path = pathlib.Path(file_path).resolve()
#     if file_path.is_dir():
#         file_name_list = list(file_path.glob("**/*"))  # 获取该路径下的文件列表
#         for file_name in file_name_list:
#             file_name_extension = "".join(list(file_name.suffixes))
#             if file_name_extension == file_type:
#                 print(f"{file_name.name}，{file_name.parent}")
#                 i = i + 1
#         print(f"查找完成，共找到{i}个文件")
#     else:
#         print("请输入文件夹路径")
#
#
# if __name__ == '__main__':
#     search_specify_type_file("./test/", ".txt")
# r'''
# test目录下有如下文件：'新建文本文档.txt', '新建文本文档 (2).txt', 并有多层子文件，子文件夹内同样有且仅有上述两个文件
# 输出为：
# 新建文本文档 (2).txt，C:\Users\37386\PycharmProjects\Python-officeDev\test
# 新建文本文档.txt，C:\Users\37386\PycharmProjects\Python-officeDev\test
# 新建文本文档 (2).txt，C:\Users\37386\PycharmProjects\Python-officeDev\test\1
# 新建文本文档.txt，C:\Users\37386\PycharmProjects\Python-officeDev\test\1
# 新建文本文档 (2).txt，C:\Users\37386\PycharmProjects\Python-officeDev\test\1\2
# 新建文本文档.txt，C:\Users\37386\PycharmProjects\Python-officeDev\test\1\2
# '''
