# coding:utf-8
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSignal
from customizeWindowPyfile.ui2pyFile.ui_watermarkDialog import Ui_WatermarkDialog
import sys


class WatermarkDialog(QDialog):
    confirmSignal = pyqtSignal(list)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_WatermarkDialog()
        self.ui.setupUi(self)
        self.ui.confirmButton.clicked.connect(self.sendWatermarkWord)
        self.ui.cancleButton.clicked.connect(self.close)
        # self.ui.colorComboBox.currentIndexChanged.connect(self.colorChange)

    def sendWatermarkWord(self):
        print('debug1')
        watermarkWord = self.ui.watermarkWord.text()
        angkle = float(self.ui.ankle.text())
        alpha = float(self.ui.alpha.text())
        colorStr = self.ui.colorComboBox.currentText()

        if colorStr == '红色':
            color = [250, 128, 114]
        elif colorStr == '蓝色':
            color = [100, 149, 237]
        elif colorStr == '绿色':
            color = [118, 238, 0]
        elif colorStr == '灰色':
            color = [139, 139, 122]
        getList =[watermarkWord, angkle, alpha, color]
        print(getList)
        self.confirmSignal.emit(getList)
        self.destroy()

    # self.cb.currentIndexChanged.connect(self.selectionchange)
    # @pyqtSlot(str)
    # def on_colorComboBox_currentIndexChanged(self,currtext):




if __name__ =='__main__':
    app = QApplication(sys.argv)
    form = WatermarkDialog()
    form.show()
    sys.exit(app.exec_())