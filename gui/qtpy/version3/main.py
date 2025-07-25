# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/8x7c9qiAneTsDJq9JnWLgA
@个人网站 ：www.python-office.com
@Date    ：2023/5/7 11:13 
@Description     ：
'''

# coding:utf-8
import os
import sys

from PyQt5.QtCore import Qt, QLocale, QTranslator
from PyQt5.QtWidgets import QApplication

from app.common.config import cfg, Language
from app.view.main_window import MainWindow


# enable dpi scale
if cfg.get(cfg.dpiScale) == "Auto":
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
else:
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

# create application
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

# internationalization
translator = QTranslator()
galleryTranslator = QTranslator()
language = cfg.get(cfg.language)

if language == Language.AUTO:
    translator.load(QLocale.system(), ":/gallery/i18n/qfluentwidgets_")
    galleryTranslator.load(QLocale.system(), ":/gallery/i18n/gallery_")
elif language != Language.ENGLISH:
    translator.load(f":/gallery/i18n/qfluentwidgets_{language.value}.qm")
    galleryTranslator.load(f":/gallery/i18n/gallery_{language.value}.qm")

app.installTranslator(translator)
app.installTranslator(galleryTranslator)

# create main window
w = MainWindow()
w.show()

app.exec_()
