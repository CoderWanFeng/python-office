import os
from alive_progress import alive_bar


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

