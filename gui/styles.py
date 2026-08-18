# -*- coding: utf-8 -*-
"""Global QSS theme for a lighter desktop productivity interface."""

from __future__ import annotations

import base64

# UI/UX Pro Max direction: bright productivity teal with restrained orange CTA.
CANVAS = "#F0FDFA"
SIDEBAR = "#F8FFFC"
SURFACE = "#FFFFFF"
SURFACE_ALT = "#ECFDF5"
SURFACE_SOLID = SURFACE
LINE = "rgba(13, 148, 136, 0.16)"
LINE_STRONG = "rgba(13, 148, 136, 0.34)"
TEXT = "#134E4A"
TEXT_ON_DARK = "#0F2F2C"
TEXT_MUTED = "#5F7F7A"
TEXT_DIM = "#7A9A95"
BLUE = "#0D9488"
BLUE_HOVER = "#14B8A6"
BLUE_SOFT = "rgba(20, 184, 166, 0.12)"
BLUE_PRESS = "#0F766E"
RED = "#F97316"
RED_HOVER = "#FB923C"
RED_SOFT = "rgba(249, 115, 22, 0.14)"
GREEN = "#10B981"

# Backward-compatible names used by custom-painted widgets.
BASE = CANVAS
MANTLE = SIDEBAR
CRUST = LINE
SURFACE0 = LINE
SURFACE1 = LINE_STRONG
SURFACE2 = TEXT_DIM
LAKE = BLUE
LAKE_DEEP = BLUE_PRESS
LAKE_DARK = TEXT
LAKE_LIGHT = BLUE_HOVER
LAKE_SOFT = BLUE_SOFT
LAKE_TINT = "rgba(36, 201, 244, 0.10)"
AMBER = RED
AMBER_DARK = "#C2410C"
SUCCESS = GREEN
DANGER = RED
DANGER_LIGHT = RED_SOFT

TERMINAL_BG = "#F8FAFC"
TERMINAL_FG = "#134E4A"
TERMINAL_ACC = BLUE

RADIUS_SM = 8
RADIUS_MD = 10
RADIUS_LG = 14
SIDEBAR_WIDTH = 292

_CHECKMARK_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" '
    'width="16" height="16">'
    '<path d="M3.5 7.5L6.5 10.5L12.5 4.5" stroke="white" stroke-width="2.2" '
    'fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    '</svg>'
)
_CHECKMARK_URL = "data:image/svg+xml;base64," + base64.b64encode(
    _CHECKMARK_SVG.encode("utf-8")
).decode("ascii")

QSS = f"""
* {{
    font-family: "Segoe UI", "Microsoft YaHei UI", "Microsoft YaHei", "PingFang SC", "SF Pro Text", sans-serif;
    font-size: 13px;
    color: {TEXT};
    outline: 0;
}}

QMainWindow, QWidget#centralWidget {{
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:1,
        stop:0 #F0FDFA,
        stop:0.44 #ECFEFF,
        stop:0.74 #F8FAFC,
        stop:1 #FFF7ED
    );
}}

QMenuBar {{
    background: rgba(255, 255, 255, 0.86);
    color: {TEXT_MUTED};
    padding: 5px 10px;
    border: none;
    font-weight: 600;
}}

QMenuBar::item {{
    background: transparent;
    padding: 6px 12px;
    border-radius: {RADIUS_SM}px;
}}

QMenuBar::item:selected {{
    background: {BLUE_SOFT};
    color: {TEXT};
}}

QMenu {{
    background: rgba(255, 255, 255, 0.98);
    border: 1px solid {LINE_STRONG};
    border-radius: {RADIUS_MD}px;
    padding: 6px;
}}

QMenu::item {{
    color: {TEXT};
    padding: 8px 28px 8px 16px;
    border-radius: {RADIUS_SM}px;
}}

QMenu::item:selected {{
    background: {BLUE_SOFT};
}}

QMenu::separator {{
    height: 1px;
    background: {LINE};
    margin: 5px 8px;
}}

QWidget#sidebar {{
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #FFFFFF,
        stop:0.58 #F8FFFC,
        stop:1 #ECFDF5
    );
    border: none;
    border-right: 1px solid rgba(13, 148, 136, 0.18);
}}

QScrollArea#categoryList,
QScrollArea {{
    background: transparent;
    border: none;
}}

QScrollArea::viewport,
QWidget#pageContent {{
    background: transparent;
}}

QWidget#sidebarInner {{
    background: transparent;
}}

QLabel#sidebarAuthor {{
    color: #5F7F7A;
    background: rgba(240, 253, 250, 0.82);
    border-top: 1px solid rgba(13, 148, 136, 0.14);
    padding: 7px 22px;
    font-size: 11px;
    font-weight: 650;
    letter-spacing: 0.2px;
}}

QLabel#sidebarCategoryHeader {{
    background: transparent;
    border: none;
    padding: 0;
}}

QToolButton#sidebarFeatureBtn {{
    background: transparent;
    border: none;
    padding: 0;
    margin: 0;
    text-align: left;
}}

QStackedWidget#pages,
QWidget#pageRoot {{
    background: transparent;
    border: none;
}}

QLabel#pageTitle {{
    font-size: 28px;
    font-weight: 750;
    color: {TEXT};
    padding: 2px 0 0 0;
    background: transparent;
}}

QLabel#pageDesc {{
    color: {TEXT_MUTED};
    font-size: 13px;
    padding: 0 0 12px 0;
    background: transparent;
    line-height: 1.35;
}}

QFrame#card, QWidget#card {{
    background: {SURFACE};
    border: 1px solid rgba(13, 148, 136, 0.14);
    border-radius: {RADIUS_MD}px;
}}

QFrame#card QLabel, QWidget#card QLabel {{
    color: {TEXT};
    background: transparent;
}}

QLabel#cardTitle {{
    font-size: 12px;
    font-weight: 800;
    color: #0F766E;
    letter-spacing: 0.4px;
    padding: 0;
    margin: 0;
    text-transform: uppercase;
    background: transparent;
}}

QPushButton {{
    background: #FFFFFF;
    color: {TEXT};
    border: 1px solid rgba(13, 148, 136, 0.22);
    border-radius: {RADIUS_MD}px;
    padding: 8px 16px;
    min-height: 20px;
    font-weight: 700;
}}

QPushButton:hover {{
    background: #F0FDFA;
    border-color: rgba(13, 148, 136, 0.50);
}}

QPushButton:pressed {{
    background: #CCFBF1;
}}

QPushButton:disabled {{
    color: #83A0B5;
    background: rgba(215, 228, 239, 0.68);
    border-color: rgba(215, 228, 239, 0.68);
}}

QPushButton:focus {{
    border: 2px solid {BLUE};
    padding: 7px 15px;
}}

QPushButton#primaryButton {{
    background: {RED};
    color: #FFFFFF;
    border: 1px solid rgba(194, 65, 12, 0.22);
    font-weight: 800;
    padding: 9px 18px;
}}

QPushButton#primaryButton:hover {{
    background: {RED_HOVER};
}}

QPushButton#primaryButton:pressed {{
    background: #EA580C;
    color: white;
}}

QPushButton#dangerButton {{
    background: #FFFFFF;
    color: #DC2626;
    border: 1px solid rgba(220, 38, 38, 0.24);
}}

QPushButton#dangerButton:hover {{
    background: rgba(254, 242, 242, 0.92);
    border-color: rgba(220, 38, 38, 0.50);
}}

QLineEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QComboBox {{
    background: #FFFFFF;
    color: {TEXT};
    border: 1px solid rgba(13, 148, 136, 0.22);
    border-radius: {RADIUS_MD}px;
    padding: 8px 11px;
    selection-background-color: {BLUE};
    selection-color: #FFFFFF;
}}

QLineEdit:hover, QPlainTextEdit:hover, QSpinBox:hover,
QDoubleSpinBox:hover, QComboBox:hover {{
    border-color: rgba(13, 148, 136, 0.44);
}}

QLineEdit:focus, QPlainTextEdit:focus, QSpinBox:focus,
QDoubleSpinBox:focus, QComboBox:focus {{
    background: #FFFFFF;
    border: 2px solid {BLUE};
    padding: 7px 10px;
}}

QLineEdit:disabled, QPlainTextEdit:disabled, QSpinBox:disabled,
QDoubleSpinBox:disabled, QComboBox:disabled {{
    color: #83A0B5;
    background: rgba(215, 228, 239, 0.68);
    border-color: rgba(215, 228, 239, 0.68);
}}

QComboBox {{
    padding-right: 26px;
}}

QComboBox::drop-down {{
    border: none;
    width: 24px;
    subcontrol-origin: padding;
    subcontrol-position: top right;
}}

QComboBox::down-arrow {{
    image: none;
    width: 0;
    height: 0;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid #527D77;
    margin-right: 8px;
}}

QComboBox QAbstractItemView {{
    background: #FFFFFF;
    border: 1px solid rgba(13, 148, 136, 0.28);
    border-radius: {RADIUS_MD}px;
    selection-background-color: {BLUE_SOFT};
    selection-color: {TEXT};
    outline: 0;
    padding: 4px;
}}

QCheckBox, QRadioButton {{
    spacing: 8px;
    color: {TEXT};
    padding: 2px 0;
}}

QCheckBox::indicator, QRadioButton::indicator {{
    width: 18px;
    height: 18px;
    border-radius: 5px;
    border: 1px solid rgba(13, 148, 136, 0.34);
    background: #FFFFFF;
}}

QRadioButton::indicator {{
    border-radius: 9px;
}}

QCheckBox::indicator:checked {{
    background: {BLUE};
    border-color: {BLUE};
    image: url({_CHECKMARK_URL});
}}

QRadioButton::indicator:checked {{
    background: {BLUE};
    border-color: {BLUE};
}}

QPlainTextEdit#logView {{
    background: {TERMINAL_BG};
    color: {TERMINAL_FG};
    border: 1px solid rgba(13, 148, 136, 0.16);
    border-radius: {RADIUS_MD}px;
    padding: 12px 14px;
    font-family: "SF Mono", "Cascadia Code", "Consolas", monospace;
    font-size: 12px;
    selection-background-color: {BLUE};
    selection-color: #FFFFFF;
}}

QToolButton {{
    background: #FFFFFF;
    color: {TEXT};
    border: 1px solid rgba(13, 148, 136, 0.22);
    border-radius: {RADIUS_MD}px;
    padding: 7px 10px;
}}

QToolButton:hover {{
    background: #F0FDFA;
    border-color: rgba(13, 148, 136, 0.44);
}}

QScrollBar:vertical {{
    background: transparent;
    width: 10px;
    margin: 4px 2px;
    border: none;
}}

QScrollBar::handle:vertical {{
    background: rgba(13, 148, 136, 0.22);
    border-radius: 5px;
    min-height: 36px;
}}

QScrollBar::handle:vertical:hover {{
    background: rgba(13, 148, 136, 0.42);
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
    background: none;
}}

QScrollBar:horizontal {{
    background: transparent;
    height: 10px;
    margin: 2px 4px;
    border: none;
}}

QScrollBar::handle:horizontal {{
    background: rgba(13, 148, 136, 0.22);
    border-radius: 5px;
    min-width: 36px;
}}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0;
    background: none;
}}

QStatusBar {{
    background: rgba(255, 255, 255, 0.88);
    color: {TEXT_MUTED};
    border-top: 1px solid rgba(13, 148, 136, 0.14);
    padding: 5px 14px;
    font-size: 12px;
}}

QSplitter::handle {{
    background: rgba(13, 148, 136, 0.14);
}}

QSplitter::handle:horizontal {{
    width: 1px;
}}

QSplitter::handle:vertical {{
    height: 1px;
}}

QToolTip {{
    background: rgba(15, 47, 44, 0.96);
    color: white;
    border: 1px solid rgba(20, 184, 166, 0.34);
    border-radius: {RADIUS_SM}px;
    padding: 6px 10px;
    font-size: 12px;
}}
"""


def apply_theme(app) -> None:
    app.setStyleSheet(QSS)
