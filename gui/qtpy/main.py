import sys

from PyQt5.QtWidgets import QApplication
from customizeWindowPyfile.FinalWidget import FinalWidget
from qt_material import apply_stylesheet  # 设置PyQt的皮肤，原开源链接 https://github.com/UN-GCPDS/qt-material

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = FinalWidget()
    mainWidget.show()
    apply_stylesheet(app, theme='dark_teal.xml')  # 设置皮肤

    sys.exit(app.exec_())
