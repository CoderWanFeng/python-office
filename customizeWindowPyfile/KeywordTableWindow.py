# coding:utf-8
from customizeWindowPyfile.ui2pyFile.ui_keywordtablewindow import Ui_keywordTableWindow
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal

class KeywordTableWindow(QDialog):
    confirmSignal = pyqtSignal(dict)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_keywordTableWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('请输入关键词和替换词')
        self.ui.confirmButton.clicked.connect(self.sendKeywordDir)

    def test(self):
        print('debug1')
        print(str(self.ui.tableWidget.item(0, 0).text()))

    def sendKeywordDir(self):
        print('字典发送成功')
        keywordDir = self.getValue()
        self.confirmSignal.emit(keywordDir)
        self.destroy()

    def getValue(self):
        colom = list(range(9))
        row = list(range(2))
        print(colom)
        print(row)
        dir = {}
        print(type(dir))
        j = 0
        for i in colom:
            # for j in row:
            if self.ui.tableWidget.item(i,j) != None:
                dir[self.ui.tableWidget.item(i,j).text()] = self.ui.tableWidget.item(i,j+1).text()
        print(dir)
        return dir



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = KeywordTableWindow()
    form.show()
    form.test()
    sys.exit(app.exec_())