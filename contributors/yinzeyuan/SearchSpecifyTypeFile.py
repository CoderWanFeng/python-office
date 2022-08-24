import os
import pathlib


def SearchSpecifyTypeFile(Path, FileType: str):
    '''

    :param Path:目标路径
    :param FileType:需要查找的文件类型
    '''
    Path = pathlib.Path(Path).resolve()
    if Path.is_dir():
        FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
        for FileName in FileNameList:
            FileNameExtension = "".join(list(FileName.suffixes))
            if FileNameExtension == FileType:
                print(f"找到了，文件名为{FileName.name}")
    else:
        print("请输入文件夹路径")


if __name__ == '__main__':
    SearchSpecifyTypeFile("./test/", ".txt")
'''
test目录下有如下文件：'1234tyu', 'ta111test1t.txt', 'taa111test2t.txt', 'taaa111test1t.txt'
输出为：
找到了，文件名为ta111test1t.txt
找到了，文件名为taa111test2t.txt
找到了，文件名为taaa111test1t.txt
'''
