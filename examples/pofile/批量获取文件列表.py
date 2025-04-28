# -*- coding: UTF-8 -*-


# pip install pofile
import pofile

files_list = pofile.get_files(path=r'D:\workplace\code\github\pofile\tests', name='pdf')
print(files_list)
