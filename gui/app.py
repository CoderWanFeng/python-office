# -*- coding: utf-8 -*-
"""QApplication 工厂 + main window 装配。"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow
from gui.styles import apply_theme


def _app_icon_path() -> Path:
    return Path(__file__).resolve().parent / "assets" / "python-office.ico"


def create_app(argv: Optional[list[str]] = None) -> QApplication:
    app = QApplication.instance() or QApplication(argv or sys.argv)
    app.setApplicationName("python-office")
    app.setOrganizationName("python-office")
    app.setFont(QFont("Segoe UI", 10))
    icon_path = _app_icon_path()
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))
    apply_theme(app)
    return app


def main() -> int:
    app = create_app()
    window = MainWindow()
    window.show()
    return app.exec()
