# -*- coding: utf-8 -*-
# @Time : 2020/8/20 19:10
# @公众号 :Python自动化办公社区 
# @File : word_table.py
# @Software: PyCharm
# @Description:

import zipfile

word_book = zipfile.ZipFile('word_table.docx')
xml = word_book.read("word/document.xml").decode('utf-8')
# print(xml)
xml_list = xml.split('<w:t>')
print(xml_list)
text_list = []
for i in xml_list:
    if i.find('</w:t>') + 1:
        text_list.append(i[:i.find('</w:t>')])
    else:
        pass
text = "".join(text_list)
print(text)
