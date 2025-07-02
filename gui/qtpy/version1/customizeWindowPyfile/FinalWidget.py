# coding:utf-8
# 用于监听拖动文件事件，可以通过鼠标拖动来获取文件路径
from PyQt5 import QtGui
from PyQt5.QtCore import QDir, pyqtSlot
# 引入产生的子窗口
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox

# 鼠标拖动事件管理器
from .ui.ui_Widget import Ui_Widget
# 导入文件功能文件


class FinalWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle('python-office')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/picture/office365.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    ##定义选择路径的槽函数


    @pyqtSlot()
    def on_chooseButtonPPT2PDF_clicked(self):
        print('poppt to popdf path chosen btn')
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathPPT2PDF.setText(aDir)
