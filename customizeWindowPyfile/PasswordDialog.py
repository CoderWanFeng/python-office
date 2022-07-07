import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog

from customizeWindowPyfile.ui2pyFile.ui_passworddialog import Ui_passwordDialog
from PyQt5 import QtWidgets

class PasswordDialog(QDialog):
    passwordSignal = pyqtSignal(str)
    def __init__(self, parent = None):
        print('debug1')
        super().__init__(parent)
        self.ui = Ui_passwordDialog()
        self.ui.setupUi(self)
        self.ui.confirmButton.clicked.connect(self.sendPassword)

    def sendPassword(self):
        print('信号发送成功')
        password = self.ui.password.text()
        self.passwordSignal.emit(password)
        self.destroy()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = PasswordDialog()
    form.show()
    sys.exit(app.exec_())

