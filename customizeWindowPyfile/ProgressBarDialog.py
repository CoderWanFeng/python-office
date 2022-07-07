from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar

from PyQt5.QtCore import QRect
from PyQt5 import QtGui
import time



class ProgressBar(QDialog):
    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent)

        # Qdialog窗体的设置
        self.resize(500, 32)  # QDialog窗的大小
        self.setWindowTitle('启动中...')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/picture/progressbar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        # 创建并设置 QProcessbar
        self.progressBar = QProgressBar(self)  # 创建
        self.progressBar.setMinimum(0)  # 设置进度条最小值
        self.progressBar.setMaximum(100)  # 设置进度条最大值
        self.progressBar.setValue(0)  # 进度条初始值为0
        self.progressBar.setGeometry(QRect(1, 3, 499, 28))  # 设置进度条在 QDialog 中的位置 [左，上，右，下]
        self.show()


    def setValue(self, value, donevalue, totalvalue):


        if donevalue != 100:
            self.progressBar.setValue(donevalue)
        difference = value - donevalue
        QApplication.processEvents()
        for i in range(50):#此处循环用于让进度条更顺滑
            if i !=0:
                self.progressBar.setValue(i*difference / 50 + donevalue)
                QApplication.processEvents()
                time.sleep(0.007)
        QApplication.processEvents()

    def setProcessOnTiTle(self, doneTask, totalTask):
        self.setWindowTitle('正在处理第'+str(doneTask)+'/'+str(totalTask)+'个任务')






