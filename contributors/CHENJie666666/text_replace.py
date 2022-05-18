"""
功能：批量实现文本内容替换功能
"""

import re
import os

def _replace_word(file_path, word, new_word, count, coverd):
    """
    单个文件全文替换
    参数：
    file_path: 文件路径
    word: 替换前的单词
    new_word: 替换后的单词
    count: 替换次数（默认为0，即全部替换）
    coverd: 是否覆盖原文件（默认为否，即创建新文件）
    """
    with open(file_path, 'r', encoding='utf-8') as r:
        text = r.read()
    
    replaced_text, replace_count = re.subn(word, new_word, text, count)

    if coverd:
        new_file_path = file_path
    else:
        new_file_path = os.path.splitext(file_path)[0] + '_replaced' + os.path.splitext(file_path)[1]
    
    with open(new_file_path, 'w', encoding='utf-8') as w:
        w.write(replaced_text)

    print(f'{file_path}中共有{replace_count}个{word}被替换')
    print(f'新文件被保存在{new_file_path}')


def replace_word(dir_or_path, word, new_word, count=0, coverd=False):
    """
    批量替换文件内容
    参数：
    dir_or_path: 文件路径或目录
    word: 替换前的单词
    new_word: 替换后的单词
    count: 替换次数（默认为0，即全部替换）
    coverd: 是否覆盖原文件（默认为否，即创建新文件）
    """
    # 对目录下的所有txt文件进行批量处理
    if os.path.isdir(dir_or_path):
        files = [i for i in os.listdir(dir_or_path) if i.endswith('.txt')]
        
        for file in files:
            _replace_word(os.path.join(dir_or_path, file), word, new_word, count, coverd)
    
    # 对单个txt文件进行处理
    else:
        _replace_word(dir_or_path, word, new_word, count, coverd)

if __name__ == '__main__':

    # 对单个文件进行替换
    replace_word('a.txt', 'Hello', '你好')

    # # 对目录下所有txt文件进行替换
    # replace_word('C:/Users/Andrew/Desktop/my_dir', 'Hello', '你好')

