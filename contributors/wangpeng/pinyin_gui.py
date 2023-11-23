# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/Nt8E8vC-ZsoN1McTOYbY2g
@个人网站      ：www.python-office.com
@代码日期    ：2023/9/26 21:46 
@本段代码的视频说明     ：
'''
import sys

import pohan
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QMessageBox
from pohan.pinyin.pinyin import Style


class PinyinConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建布局
        layout = QVBoxLayout()

        # 创建输入文本框
        self.input_text = QLineEdit()
        layout.addWidget(self.input_text)

        # 创建转换按钮
        convert_button = QPushButton('转换')
        convert_button.clicked.connect(self.convert)
        layout.addWidget(convert_button)

        # 创建输出文本框
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # 创建复制按钮
        copy_button = QPushButton('复制')
        copy_button.clicked.connect(self.copy_output)
        layout.addWidget(copy_button)

        # 创建退出按钮
        quit_button = QPushButton('退出')
        quit_button.clicked.connect(self.close)
        layout.addWidget(quit_button)

        # 创建关于按钮
        about_button = QPushButton('关于')
        about_button.clicked.connect(self.show_about)
        layout.addWidget(about_button)

        # 设置布局
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle('拼音转换器')
        self.setGeometry(300, 300, 300, 200)

    def convert(self):
        # 获取输入文本
        input_text = self.input_text.text()

        # 将汉字转换成拼音带声调的结果
        pinyin_list = pohan.pinyin.han2pinyin(input_text, style=Style.TONE)

        # 设置输出文本框显示结果
        self.output_text.setPlainText(f'带声调的结果：{pinyin_list}')

    def copy_output(self):
        # 复制输出文本到剪贴板
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_text.toPlainText())

    def show_about(self):
        QMessageBox.about(self, '关于', '谨献给一起学习的道友')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = PinyinConverter()
    converter.show()
    sys.exit(app.exec_())
