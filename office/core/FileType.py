import os
from alive_progress import alive_bar

import pathlib

from office.lib.utils.time_utils import time_count_dec


class MainFile():

    def replace4filename(self, path, del_content, replace_content):
        """
        :param path: 需要替换的文件夹路径
        :param del_content: 需要删除/替换的内容
        :param replace_content: 替换后的内容，可以不填 = 直接删除
        :return:
        """
        # 获取该目录下所有文件，存入列表中；不包含子文件夹
        fileList = os.listdir(path)
        work_count = 0
        with alive_bar(len(fileList)) as bar:
            for old_file_name in fileList:  # 依次读取该路径下的文件名
                bar()  # 进度条
                if del_content in old_file_name:

                    if replace_content:
                        new_file_name = old_file_name.replace(del_content, replace_content)
                    else:
                        new_file_name = old_file_name.replace(del_content, '')
                    os.rename(path + os.sep + old_file_name, path + os.sep + new_file_name)
                    work_count = work_count + 1
        print("当前目录下，共有{}个文件/文件夹，本次运行共进行了{}个文件/文件夹的重命名".format(len(fileList), work_count))

    @time_count_dec
    def file_name_insert_content(self, file_path, insert_position: int, insert_content: str):
        """

        :param file_path: 文件存放路径
        :param insert_position: 插入位置（内容将插入在此之后，如果输入位置大于文件主名长度将插入在末尾）
        :param insert_content: 插入内容
        """
        Path = pathlib.Path(file_path).resolve()
        if Path.is_dir():
            FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
            for FileName in FileNameList:
                if FileName.is_file():  # 判断是否为文件，只对文件进行操作
                    FileNameExtension = "".join(list(FileName.suffixes))
                    FileNameRoot = FileName.name.replace(FileNameExtension, "")
                    # 分离文件主名和扩展名，防止对扩展名进行操作
                    FileNameFormer = FileNameRoot[:insert_position:]
                    FileNameLatter = FileNameRoot[insert_position::]
                    # 拆分文件主名
                    NewFileName = FileNameFormer + insert_content + FileNameLatter + FileNameExtension  # 合并文件名
                    if not Path.joinpath(NewFileName).is_file():
                        FileName.rename(Path.joinpath(NewFileName))
                    else:
                        print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
        else:
            print("请输入文件夹路径")

    @time_count_dec
    def file_name_add_prefix(self, file_path, prefix_content: str):
        """

        :param file_path: 文件存放路径
        :param prefix_content: 前缀内容
        """
        Path = pathlib.Path(file_path).resolve()
        if Path.is_dir():
            FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
            for FileName in FileNameList:
                if FileName.is_file():  # 判断是否为文件，只对文件进行操作
                    NewFileName = prefix_content + FileName.name  # 合并文件名
                    if not Path.joinpath(NewFileName).is_file():
                        FileName.rename(Path.joinpath(NewFileName))
                    else:
                        print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
        else:
            print("请输入文件夹路径")

    @time_count_dec
    def file_name_add_postfix(self, file_path, postfix_content: str):
        """

        :param file_path: 文件存放路径
        :param postfix_content: 后缀内容
        """
        Path = pathlib.Path(file_path).resolve()
        if Path.is_dir():
            FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
            for FileName in FileNameList:
                if FileName.is_file():  # 判断是否为文件，只对文件进行操作
                    FileNameExtension = "".join(list(FileName.suffixes))
                    FileNameRoot = FileName.name.replace(FileNameExtension, "")
                    # 分离文件主名和扩展名
                    NewFileName = FileNameRoot + postfix_content + FileNameExtension  # 合并文件名
                    if not Path.joinpath(NewFileName).is_file():
                        FileName.rename(Path.joinpath(NewFileName))
                    else:
                        print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
        else:
            print("请输入文件夹路径")

    def search_specify_type_file(self, file_path, file_type: str):
        '''

        :param file_path:目标路径
        :param file_type:需要查找的文件类型
        '''
        print("开始查找")
        i = 0  # 计数变量
        file_path = pathlib.Path(file_path).resolve()
        if file_path.is_dir():
            file_name_list = list(file_path.glob("**/*"))  # 获取该路径下的文件列表
            for file_name in file_name_list:
                file_name_extension = "".join(list(file_name.suffixes))
                if file_name_extension == file_type:
                    print(f"{file_name.name}，{file_name.parent}")
                    i = i + 1
            print(f"查找完成，共找到{i}个文件")
        else:
            print("请输入文件夹路径")
