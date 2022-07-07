# coding:utf-8
#用于监听拖动文件事件，可以通过鼠标拖动来获取文件路径

from PyQt5.QtCore import QDir, pyqtSlot
#导入word功能文件
from function.Word.word2pdf import word2pdf
from function.Word.wordReplaceKeywords import wordReplaceKeyword
#导入ppt功能文件
from function.Ppt.ppt2jpg import ppt2jpg
from function.Ppt.ppt2pdf import ppt2pdf
from function.Ppt.pptImageExtraction import pptImageExtration
#导入文件功能文件
from function.File.cleanDuplicateFiles import cleanDuplicateFiles
from function.File.fileClassification import fileClasscation
#导入PDF功能
from function.Pdf.encryptionPDF import encryptionPDF
from function.Pdf.decryptionPDF import decryptionPDF
from function.Pdf.createWatermark4PDF import createWatermark4PDF
#鼠标拖动事件管理器
from EventHandler import QEventHandler
from customizeWindowPyfile.ui2pyFile.ui_Widget import Ui_Widget
#引入产生的子窗口
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from customizeWindowPyfile.PasswordDialog import PasswordDialog
from customizeWindowPyfile.KeywordTableWindow import KeywordTableWindow
from customizeWindowPyfile.WatermarkDialog import WatermarkDialog
from PyQt5 import QtGui


class FinalWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle('Author：TownBoats V1.5')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/picture/office365.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        #装上事件监听器
        self.ui.pathPPT2PDF.installEventFilter(QEventHandler(self))
        self.ui.pathPPT2JPG.installEventFilter(QEventHandler(self))
        self.ui.pathImageExtract.installEventFilter(QEventHandler(self))

        self.ui.pathWord2PDF.installEventFilter(QEventHandler(self))
        self.ui.pathKeywordReplace.installEventFilter(QEventHandler(self))

        self.ui.pathFileClassication.installEventFilter(QEventHandler(self))
        self.ui.pathDuplicateFile.installEventFilter(QEventHandler(self))

        self.ui.pathDecrypt.installEventFilter(QEventHandler(self))
        self.ui.pathEncryption.installEventFilter(QEventHandler(self))
        self.ui.pathAddWatermark.installEventFilter(QEventHandler(self))
        print('debug2')
        # self.app = QApplication(sys.argv)
        print('debug3')

##定义选择路径的槽函数

    @pyqtSlot()
    def on_chooseButtonWord2PDF_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录",curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathWord2PDF.setText(aDir)


    @pyqtSlot()
    def on_chooseButtonPPT2PDF_clicked(self):
        print('ppt to pdf path chosen btn')
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathPPT2PDF.setText(aDir)


    @pyqtSlot()
    def on_chooseButtonPPT2JPG_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathPPT2JPG.setText(aDir)


    @pyqtSlot()
    def on_chooseButtonImageExtract_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getOpenFileName(self, "选择一个文件", curDir,'*ppt*')
        #QFileDialog.getOpenFileName()的返回值是一个元组，只需要元组的第一个值
        self.ui.pathImageExtract.setText(aDir[0])

    @pyqtSlot()
    def on_chooseButtonFileClassification_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathFileClassication.setText(aDir)

    @pyqtSlot()
    def on_chooseDuplicateFileButton_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathDuplicateFile.setText(aDir)

    @pyqtSlot()
    def on_choosePathEncryption_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathEncryption.setText(aDir)


    @pyqtSlot()
    def on_choosePathDecryption_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathDecrypt.setText(aDir)

    @pyqtSlot()
    def on_chooseButtonKeywordReplace_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathKeywordReplace.setText(aDir)

    @pyqtSlot()
    def on_choosePathAddWatermarkButton_clicked(self):
        curDir = QDir.currentPath()
        aDir = QFileDialog.getExistingDirectory(self, "选择一个目录", curDir, QFileDialog.ShowDirsOnly)
        self.ui.pathAddWatermark.setText(aDir)


##定义开始按钮的槽函数
    @pyqtSlot()
    def on_convertButtonPPT2PDF_clicked(self):
        print('ppt to pdf convert button')
        print('选择路径' + self.ui.pathPPT2PDF.text())
        ppt2pdf(self.ui.pathPPT2PDF.text())
        QMessageBox.information(self,'提示框','ppt已经转换成pdf！')

    @pyqtSlot()
    def on_convertButtonWord2PDF_clicked(self):
        print('选择路径'+self.ui.pathWord2PDF.text())
        word2pdf(self.ui.pathWord2PDF.text())
        QMessageBox.information(self, '提示框', 'word已经转换成pdf！')

    @pyqtSlot()
    def on_convertButtonPPT2JPG_clicked(self):
        print('ppt to jpg button clicked')
        print('选择路径' + self.ui.pathPPT2JPG.text())
        ppt2jpg(self.ui.pathPPT2JPG.text())
        QMessageBox.information(self, '提示框', 'ppt已经转换成JPG！')

    @pyqtSlot()
    def on_ExtractButton_clicked(self):
        print('选择路径' + self.ui.pathImageExtract.text())
        pptImageExtration(self.ui.pathImageExtract.text())
        QMessageBox.information(self, '提示框', '选中ppt里面的图片已经被提取！！')


    @pyqtSlot()
    def on_classificationButton_clicked(self):
        fileClasscation(self.ui.pathFileClassication.text())
        QMessageBox.information(self, '提示框', '文件已完成分类！')


    @pyqtSlot()
    def on_duplicateFileButton_clicked(self):
        cleanDuplicateFiles(self.ui.pathDuplicateFile.text())
        QMessageBox.information(self,'提示框','已经找出冗余文件！！')


#以下是有产生子窗口的情况
    @pyqtSlot()
    def on_encryptionButton_clicked(self):
        passwordDialog = PasswordDialog(self)
        passwordDialog.passwordSignal.connect(self.setPassWordandEncryption)
        passwordDialog.show() #用exec()方法可以阻塞窗口
        # passwordDialog.exec_()

    @pyqtSlot()
    def on_DecryptionButton_clicked(self):
        passwordDialog = PasswordDialog(self)
        passwordDialog.passwordSignal.connect(self.setPasswordAndDecryption)
        passwordDialog.show()  # 用exec()方法可以阻塞窗口


    @pyqtSlot(str)
    def setPassWordandEncryption(self,str):
        password = str
        print('debug1:'+ str)
        encryptionPDF(self.ui.pathEncryption.text(), password)
        QMessageBox.information(self, '提示框', 'PDF加密成功！')

    @pyqtSlot(str)
    def setPasswordAndDecryption(self, str):
        password = str
        print('debug2:'+password)
        decryptionPDF(self.ui.pathDecrypt.text(), password)
        QMessageBox.information(self, '提示框', 'PDF解密成功！')

    @pyqtSlot()#这里是打开关键字的窗口
    def on_adjustButtonKeyword_clicked(self):
        keywordeywordTableWindow = KeywordTableWindow(self)
        keywordeywordTableWindow.confirmSignal.connect(self.getKeywordDictAndReplace)
        keywordeywordTableWindow.show()


    @pyqtSlot(dict)
    def getKeywordDictAndReplace(self, dict):
        dir = dict
        wordReplaceKeyword(self.ui.pathKeywordReplace.text(), dir)
        QMessageBox.information(self, '提示框', '文件中的关键字已经替换完毕！')

    @pyqtSlot()
    def on_addWatermarkButton_clicked(self):
        watermarkDialog = WatermarkDialog(self)
        print("debug0")
        watermarkDialog.confirmSignal.connect(self.getWatermarkWordAndAddWatermark)
        watermarkDialog.show()


    @pyqtSlot(list)
    def getWatermarkWordAndAddWatermark(self, list):
        print('debug2')
        print(str)
        watermarkWord = list[0]
        angkle = list[1]
        alpha = list[2]
        color = list[3]
        path = self.ui.pathAddWatermark.text()
        createWatermark4PDF(watermarkWord, path, color, angkle, alpha)
        QMessageBox.information(self, '提示框', '水印添加成功！！')

