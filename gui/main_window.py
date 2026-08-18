# -*- coding: utf-8 -*-
"""主窗口：左侧分类列表 + 右侧功能面板。"""

from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QAction, QColor, QKeySequence, QLinearGradient, QPainter, QPixmap
from PySide6.QtWidgets import (
    QButtonGroup, QHBoxLayout, QLabel, QMainWindow, QMessageBox,
    QPushButton, QScrollArea, QSizePolicy, QSplitter, QStackedWidget,
    QStatusBar, QToolButton, QVBoxLayout, QWidget,
)

from gui import __version__
from gui.panels import FeaturePage
from gui.registry import Category, Feature, build_registry, find_feature, resolve_feature
from gui.styles import (
    BLUE, BLUE_HOVER, BLUE_PRESS, BLUE_SOFT, LINE, RED, SIDEBAR_WIDTH,
    SURFACE, TEXT, TEXT_MUTED,
)


APPLE_ICON_KINDS = {
    "📕": "doc",
    "📗": "grid",
    "📘": "doc",
    "📙": "deck",
    "🖼️": "image",
    "📁": "folder",
    "🎬": "video",
    "📧": "mail",
    "🔎": "search",
    "🛠️": "tool",
    "💬": "chat",
}

APPLE_ICON_ACCENTS = {
    "📕": ("#F97316", "#FFF7ED"),
    "📗": ("#0D9488", "#ECFDF5"),
    "📘": ("#0284C7", "#E0F2FE"),
    "📙": ("#F97316", "#FFF7ED"),
    "🖼️": ("#0D9488", "#ECFDF5"),
    "📁": ("#0F766E", "#F0FDFA"),
    "🎬": ("#0284C7", "#E0F2FE"),
    "📧": ("#0D9488", "#ECFDF5"),
    "🔎": ("#F97316", "#FFF7ED"),
    "🛠️": ("#0F766E", "#F0FDFA"),
    "💬": ("#10B981", "#ECFDF5"),
}


class HeaderLabel(QLabel):
    """侧栏分类 header：可点击切换折叠状态（▶/▼）。

    自绘文字（完全控制 layout → 箭头精准左对齐）+ override 完整的 mouse 事件：
        - press → 记录按下状态
        - release 在 label 内 → emit clicked
        - release 在 label 外 → 取消
        - move → 更新 hover/pressed 视觉效果
    QLabel 默认 mouseRelease 传给父，必须 override 才能响应点击。
    """

    clicked = Signal()

    def __init__(self, icon: str, title: str, expanded: bool = False, parent=None):
        super().__init__(parent)
        self._icon_text = icon
        self._icon_kind = APPLE_ICON_KINDS.get(icon, "app")
        self._accent_color, self._accent_soft = APPLE_ICON_ACCENTS.get(
            icon, (BLUE, BLUE_SOFT)
        )
        self._title_text = title
        self._expanded = expanded
        self._hover = False
        self._pressed = False
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(40)
        # 启用 mouse tracking（让 mouseMove / leave / enter 事件正常触发）
        self.setMouseTracking(True)
        # 透明背景（让 styles.py 控制 hover / checked）
        self.setStyleSheet("QLabel#sidebarCategoryHeader { background: transparent; border: none; }")

    def set_expanded(self, expanded: bool) -> None:
        """设置折叠/展开状态（重绘）。"""
        self._expanded = expanded
        self.update()

    def is_expanded(self) -> bool:
        return self._expanded

    @staticmethod
    def _draw_apple_icon(p, rect, kind: str, color: QColor) -> None:
        from PySide6.QtCore import QPointF, QRectF
        from PySide6.QtGui import QPainterPath, QPen, QPolygonF

        pen = QPen(color, 1.55)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        p.setPen(pen)
        p.setBrush(Qt.NoBrush)

        x, y, w, h = rect.x(), rect.y(), rect.width(), rect.height()

        if kind in ("doc", "app"):
            p.drawRoundedRect(QRectF(x + 6, y + 4, w - 12, h - 8), 3, 3)
            p.drawLine(QPointF(x + 10, y + 10), QPointF(x + w - 10, y + 10))
            p.drawLine(QPointF(x + 10, y + 14), QPointF(x + w - 13, y + 14))
            return

        if kind == "grid":
            p.drawRoundedRect(QRectF(x + 5, y + 5, w - 10, h - 10), 3, 3)
            p.drawLine(QPointF(x + w / 2, y + 5), QPointF(x + w / 2, y + h - 5))
            p.drawLine(QPointF(x + 5, y + h / 2), QPointF(x + w - 5, y + h / 2))
            return

        if kind == "deck":
            p.drawRoundedRect(QRectF(x + 5, y + 6, w - 10, h - 11), 3, 3)
            p.drawLine(QPointF(x + 11, y + h - 4), QPointF(x + w - 11, y + h - 4))
            p.drawLine(QPointF(x + w / 2, y + h - 5), QPointF(x + w / 2, y + h - 2))
            return

        if kind == "image":
            box = QRectF(x + 5, y + 5, w - 10, h - 10)
            p.drawRoundedRect(box, 3, 3)
            p.drawEllipse(QRectF(x + w - 13, y + 8, 3.5, 3.5))
            mountain = QPainterPath()
            mountain.moveTo(x + 8, y + h - 7)
            mountain.lineTo(x + 14, y + 13)
            mountain.lineTo(x + 18, y + h - 8)
            mountain.lineTo(x + 21, y + 15)
            mountain.lineTo(x + w - 7, y + h - 7)
            p.drawPath(mountain)
            return

        if kind == "folder":
            path = QPainterPath()
            path.moveTo(x + 5, y + 9)
            path.lineTo(x + 13, y + 9)
            path.lineTo(x + 16, y + 12)
            path.lineTo(x + w - 5, y + 12)
            path.lineTo(x + w - 5, y + h - 5)
            path.lineTo(x + 5, y + h - 5)
            path.closeSubpath()
            p.drawPath(path)
            return

        if kind == "video":
            p.drawRoundedRect(QRectF(x + 5, y + 5, w - 10, h - 10), 3, 3)
            tri = QPolygonF([
                QPointF(x + 14, y + 10),
                QPointF(x + 14, y + h - 10),
                QPointF(x + w - 12, y + h / 2),
            ])
            p.setBrush(color)
            p.drawPolygon(tri)
            p.setBrush(Qt.NoBrush)
            return

        if kind == "mail":
            box = QRectF(x + 5, y + 7, w - 10, h - 12)
            p.drawRoundedRect(box, 3, 3)
            p.drawLine(QPointF(x + 6, y + 9), QPointF(x + w / 2, y + 15))
            p.drawLine(QPointF(x + w - 6, y + 9), QPointF(x + w / 2, y + 15))
            return

        if kind == "search":
            p.drawEllipse(QRectF(x + 7, y + 6, 11, 11))
            p.drawLine(QPointF(x + 17, y + 17), QPointF(x + 23, y + 23))
            return

        if kind == "tool":
            for i, yy in enumerate((8, 14, 20)):
                p.drawLine(QPointF(x + 6, y + yy), QPointF(x + w - 6, y + yy))
                knob_x = x + (12 if i == 0 else 20 if i == 1 else 15)
                p.drawEllipse(QRectF(knob_x - 2, y + yy - 2, 4, 4))
            return

        if kind == "chat":
            bubble = QPainterPath()
            bubble.addRoundedRect(QRectF(x + 5, y + 5, w - 10, h - 12), 5, 5)
            bubble.moveTo(x + 12, y + h - 8)
            bubble.lineTo(x + 10, y + h - 4)
            bubble.lineTo(x + 16, y + h - 8)
            p.drawPath(bubble)

    def paintEvent(self, event):
        from PySide6.QtCore import QPointF, QRectF
        from PySide6.QtGui import QColor, QFont, QPainter, QPainterPath, QPen

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setRenderHint(QPainter.TextAntialiasing, True)

        rect = self.rect()

        bg_rect = rect.adjusted(0, 2, 0, -2)
        path = QPainterPath()
        path.addRoundedRect(QRectF(bg_rect), 10.0, 10.0)

        # 1) 背景（按 hover / pressed / expanded 状态）
        if self._pressed:
            bg = QColor("#CCFBF1")
        elif self._hover or self._expanded:
            bg = QColor(self._accent_soft if self._expanded else "#F0FDFA")
        else:
            bg = QColor("transparent")
        if bg.alpha() > 0:
            p.fillPath(path, bg)

        # 2) Apple-like chevron + monochrome badge + title.
        chevron_pen = QPen(QColor(self._accent_color if self._expanded else "#7A9A95"), 1.8)
        chevron_pen.setCapStyle(Qt.RoundCap)
        chevron_pen.setJoinStyle(Qt.RoundJoin)
        p.setPen(chevron_pen)
        cy = rect.center().y()
        if self._expanded:
            p.drawLine(QPointF(15, cy - 3), QPointF(19, cy + 1))
            p.drawLine(QPointF(19, cy + 1), QPointF(23, cy - 3))
        else:
            p.drawLine(QPointF(16, cy - 4), QPointF(21, cy))
            p.drawLine(QPointF(21, cy), QPointF(16, cy + 4))

        badge_w = 34
        badge_rect = QRectF(30, cy - 11, badge_w, 22)
        badge_path = QPainterPath()
        badge_path.addRoundedRect(badge_rect, 7.0, 7.0)
        p.fillPath(badge_path, QColor("#FFFFFF" if self._expanded else self._accent_soft))
        p.setPen(QPen(QColor(self._accent_color if self._expanded else "#B8D9D3"), 1.0))
        p.drawPath(badge_path)
        self._draw_apple_icon(
            p,
            badge_rect,
            self._icon_kind,
            QColor(self._accent_color if self._expanded else "#5F7F7A"),
        )

        font = QFont(self.font())
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        p.setFont(font)

        # 颜色
        if self._expanded:
            p.setPen(QColor(self._accent_color))
        else:
            p.setPen(QColor(TEXT_MUTED))

        text_rect = rect.adjusted(78, 0, -8, 0)
        p.drawText(text_rect, int(Qt.AlignLeft | Qt.AlignVCenter), self._title_text)

        p.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._pressed = True
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._pressed:
            self._pressed = False
            # 只在 release 时鼠标仍在 label 内才触发 click
            if self.rect().contains(event.pos()):
                self.clicked.emit()
            self.update()

    def mouseMoveEvent(self, event):
        # 鼠标在 label 内移动（hover 效果）
        was_hover = self._hover
        self._hover = self.rect().contains(event.pos())
        if was_hover != self._hover:
            self.update()

    def enterEvent(self, event):
        self._hover = True
        self.update()

    def leaveEvent(self, event):
        self._hover = False
        # 如果按下时鼠标离开，取消按下状态
        if self._pressed:
            self._pressed = False
        self.update()


class FeatureLabel(QToolButton):
    """侧栏二级功能按钮：自绘背景和文字，确保文本稳定左对齐。"""

    def __init__(self, title: str, feature_id: str, expanded_parents: bool = False, parent=None):
        super().__init__(parent)
        self._title_text = title
        self._feature_id = feature_id
        self._hover = False
        self.setText(title)
        self.setCheckable(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(38)
        self.setMouseTracking(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def paintEvent(self, event):
        from PySide6.QtCore import QRectF
        from PySide6.QtGui import QColor, QFont, QLinearGradient, QPainter, QPainterPath

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setRenderHint(QPainter.TextAntialiasing, True)

        rect = self.rect()
        bg_rect = rect.adjusted(0, 1, 0, -1)
        path = QPainterPath()
        path.addRoundedRect(QRectF(bg_rect), 12.0, 12.0)

        if self.isChecked():
            bg = QColor("#F97316" if not self._hover else "#FB923C")
            border = QColor("#FED7AA")
            text = QColor("#FFFFFF")
            weight = QFont.ExtraBold
        elif self.isDown():
            bg = QColor("#0F766E")
            border = QColor("#0F766E")
            text = QColor("#FFFFFF")
            weight = QFont.Bold
        elif self._hover:
            bg = QColor("#F0FDFA")
            border = QColor("#99F6E4")
            text = QColor(TEXT)
            weight = QFont.DemiBold
        else:
            bg = QColor("transparent")
            border = QColor("transparent")
            text = QColor(TEXT_MUTED)
            weight = QFont.Medium

        if bg.alpha() > 0:
            p.fillPath(path, bg)
        p.setPen(border)
        p.drawPath(path)

        font = QFont(self.font())
        font.setPointSize(12)
        font.setWeight(weight)
        p.setFont(font)
        p.setPen(text)
        text_rect = rect.adjusted(24, 0, -10, 0)
        p.drawText(text_rect, int(Qt.AlignLeft | Qt.AlignVCenter), self._title_text)
        p.end()

    def enterEvent(self, event):
        self._hover = True
        self.update()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._hover = False
        self.update()
        super().leaveEvent(event)


class TitleBlock(QWidget):
    """侧栏顶部标题块：简洁品牌卡。"""

    def __init__(self, version: str = "", parent=None):
        super().__init__(parent)
        self._version = version  # 保留参数以兼容旧调用，但不再渲染
        self._icon_pixmap = QPixmap(str(Path(__file__).resolve().parent / "assets" / "python-office-icon.png"))
        self.setObjectName("sidebarTitleBlock")
        self.setFixedHeight(92)
        from PySide6.QtWidgets import QSizePolicy
        sp = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setSizePolicy(sp)

    def paintEvent(self, event):
        from PySide6.QtCore import QRectF
        from PySide6.QtGui import QColor, QFont, QPainter, QPainterPath

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, True)

        rect = self.rect()
        radius = 16.0
        margin = 10
        inner_rect = rect.adjusted(margin, margin, -margin, -margin)
        path = QPainterPath()
        path.addRoundedRect(QRectF(inner_rect), radius, radius)
        grad = QLinearGradient(inner_rect.left(), inner_rect.top(), inner_rect.right(), inner_rect.bottom())
        grad.setColorAt(0.0, QColor("#FFFFFF"))
        grad.setColorAt(0.58, QColor("#F0FDFA"))
        grad.setColorAt(1.0, QColor("#FFF7ED"))
        p.fillPath(path, grad)
        p.setPen(QColor("#99F6E4"))
        p.drawPath(path)

        icon_rect = QRectF(inner_rect.left() + 14, inner_rect.top() + 16, 38, 38)
        if not self._icon_pixmap.isNull():
            p.drawPixmap(icon_rect.toRect(), self._icon_pixmap)
        else:
            dot_rect = QRectF(inner_rect.left() + 18, inner_rect.top() + 22, 12, 12)
            dot_path = QPainterPath()
            dot_path.addEllipse(dot_rect)
            p.fillPath(dot_path, QColor(RED))

        title_font = QFont(self.font())
        title_font.setPointSize(16)
        title_font.setWeight(QFont.Bold)
        p.setFont(title_font)
        p.setPen(QColor(TEXT))
        p.drawText(inner_rect.adjusted(62, 13, -16, -34), int(Qt.AlignLeft | Qt.AlignVCenter), "python-office")

        sub_font = QFont(self.font())
        sub_font.setPointSize(10)
        sub_font.setWeight(QFont.Medium)
        p.setFont(sub_font)
        p.setPen(QColor(TEXT_MUTED))
        p.drawText(inner_rect.adjusted(62, 42, -16, -10), int(Qt.AlignLeft | Qt.AlignVCenter), f"Automation Studio  v{self._version}")

        p.end()


class MainWindow(QMainWindow):
    """GUI 入口窗口。"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("python-office · 图形界面")
        self.resize(1920, 1080)
        self.setMinimumSize(1280, 720)

        self._categories: list[Category] = build_registry()
        self._pages: dict[str, FeaturePage] = {}

        self._build_ui()
        self._populate_sidebar()
        self._select_first_category()

    # ----- UI 构建 -----
    @staticmethod
    def _make_gradient_pixmap(width: int, height: int) -> QPixmap:
        """生成一个 湖蓝→浅蓝 上→下渐变 pixmap。"""
        pix = QPixmap(width, height)
        painter = QPainter(pix)
        grad = QLinearGradient(0, 0, 0, height)
        grad.setColorAt(0.0, QColor("#F0FDFA"))
        grad.setColorAt(0.62, QColor("#ECFEFF"))
        grad.setColorAt(1.0, QColor("#FFF7ED"))
        painter.fillRect(0, 0, width, height, grad)
        painter.end()
        return pix

    def _build_ui(self):
        central = QWidget()
        central.setObjectName("centralWidget")
        self.setCentralWidget(central)

        outer = QHBoxLayout(central)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(1)
        splitter.setChildrenCollapsible(False)

        # 侧边栏
        self._sidebar = QWidget()
        self._sidebar.setObjectName("sidebar")
        self._sidebar.setFixedWidth(SIDEBAR_WIDTH)
        sb_lay = QVBoxLayout(self._sidebar)
        sb_lay.setContentsMargins(0, 0, 0, 0)
        sb_lay.setSpacing(0)

        title_block = TitleBlock(__version__)
        title_block.setObjectName("sidebarTitleBlock")
        sb_lay.addWidget(title_block)

        self._category_list = QScrollArea()
        self._category_list.setObjectName("categoryList")
        self._category_list.setWidgetResizable(True)
        self._category_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._sidebar_inner = QWidget()
        self._sidebar_inner.setObjectName("sidebarInner")
        self._sidebar_layout = QVBoxLayout(self._sidebar_inner)
        self._sidebar_layout.setContentsMargins(12, 8, 12, 12)
        self._sidebar_layout.setSpacing(2)
        self._category_list.setWidget(self._sidebar_inner)
        self._feature_buttons: list[QToolButton] = []
        # 每个分类的折叠组：{分类id: (header按钮, [功能按钮列表])}
        self._category_groups: dict[str, tuple[HeaderLabel, list[QToolButton]]] = {}
        self._feature_button_group = QButtonGroup(self)
        self._feature_button_group.setExclusive(True)
        sb_lay.addWidget(self._category_list, 1)

        author_label = QLabel("主程序：程序员晚枫\n图形设计：倚栏听雨")
        author_label.setObjectName("sidebarAuthor")
        author_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        author_label.setFixedHeight(58)
        sb_lay.addWidget(author_label)

        splitter.addWidget(self._sidebar)

        # 主区
        self._stack = QStackedWidget()
        self._stack.setObjectName("pages")
        splitter.addWidget(self._stack)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([SIDEBAR_WIDTH, 1656])

        outer.addWidget(splitter)

        # 状态栏
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("就绪")

        # 菜单
        self._build_menu()

    def _build_menu(self):
        reload_action = QAction("刷新注册表", self)
        reload_action.setShortcut(QKeySequence("F5"))
        reload_action.triggered.connect(self._reload_registry)

        about_action = QAction("关于", self)
        about_action.triggered.connect(self._show_about)

        quit_action = QAction("退出", self)
        quit_action.setShortcut(QKeySequence.Quit)
        quit_action.triggered.connect(self.close)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("文件")
        file_menu.addAction(reload_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

        help_menu = menubar.addMenu("帮助")
        help_menu.addAction(about_action)

    # ----- 数据填充 -----
    def _populate_sidebar(self):
        # 清空旧 layout
        while self._sidebar_layout.count():
            item = self._sidebar_layout.takeAt(0)
            w = item.widget()
            if w is not None:
                w.deleteLater()
        self._feature_buttons.clear()
        if hasattr(self, "_category_groups"):
            self._category_groups.clear()

        # QStackedWidget 没有 clear()：手动逐个移除
        while self._stack.count():
            w = self._stack.widget(0)
            self._stack.removeWidget(w)
            w.deleteLater()
        self._pages.clear()

        for cat in self._categories:
            # 分类 header：可点击切换折叠
            # 用 QLabel + 配合自绘点击事件（避免 QPushButton 默认文字居中问题）
            header_btn = HeaderLabel(cat.icon, cat.title, expanded=False)
            header_btn.setObjectName("sidebarCategoryHeader")
            header_btn.setProperty("role", "categoryHeader")
            header_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            header_btn.setProperty("expanded", False)
            # 点击 → 折叠/展开
            header_btn.clicked.connect(lambda cid=cat.id: self._toggle_category(cid))
            self._sidebar_layout.addWidget(header_btn)

            # 收集此分类下所有功能按钮
            cat_buttons = []
            for feat in cat.features:
                btn = FeatureLabel(feat.title, feat.id, expanded_parents=False)
                btn.setObjectName("sidebarFeatureBtn")
                btn.setProperty("featureId", feat.id)
                # 默认折叠：所有功能按钮隐藏
                btn.setVisible(False)
                btn.clicked.connect(lambda _=False, fid=feat.id: self._on_feature_clicked(fid))
                self._feature_button_group.addButton(btn)
                self._feature_buttons.append(btn)
                self._sidebar_layout.addWidget(btn)
                cat_buttons.append(btn)

            # 把这个分类的按钮列表存起来，header 切换时用
            self._category_groups[cat.id] = (header_btn, cat_buttons)

        self._sidebar_layout.addStretch(1)

    def _ensure_page(self, feat: Feature) -> FeaturePage:
        page = self._pages.get(feat.id)
        if page is not None:
            return page
        resolved = resolve_feature(feat)
        page = FeaturePage(resolved, self)
        self._stack.addWidget(page)
        self._pages[feat.id] = page
        return page

    @staticmethod
    def _write_header_text(header_btn, expanded: bool):
        """更新 HeaderLabel 的 expanded 状态（触发重绘）。"""
        if hasattr(header_btn, "set_expanded"):
            header_btn.set_expanded(expanded)
        header_btn.setProperty("expanded", expanded)

    def _toggle_category(self, cat_id: str):
        """点击分类 header：切换该分类下所有功能按钮的可见性。"""
        if not hasattr(self, "_category_groups"):
            return
        group = self._category_groups.get(cat_id)
        if not group:
            return
        header_btn, buttons = group
        # 切换状态
        new_expanded = not header_btn.is_expanded() if hasattr(header_btn, "is_expanded") else True
        self._write_header_text(header_btn, expanded=new_expanded)
        for btn in buttons:
            btn.setVisible(new_expanded)

    def _on_feature_clicked(self, feature_id: str):
        feat = find_feature(self._categories, feature_id)
        if not feat:
            return
        self._show_feature(feat)
        cat = next(
            (c for c in self._categories if any(f.id == feature_id for f in c.features)),
            None,
        )
        if cat:
            self.statusBar().showMessage(
                f"分类：{cat.title}  ·  功能：{feat.title}"
            )

    def _select_first_category(self):
        if self._feature_buttons:
            if self._categories and self._categories[0].features:
                self._show_feature(self._categories[0].features[0])

    def _show_feature(self, feat: Feature):
        page = self._ensure_page(feat)
        idx = self._stack.indexOf(page)
        if idx >= 0:
            self._stack.setCurrentIndex(idx)

    def _reload_registry(self):
        self._categories = build_registry()
        self._populate_sidebar()
        self._select_first_category()
        self.statusBar().showMessage("注册表已刷新", 3000)

    def _show_about(self):
        QMessageBox.about(
            self,
            "关于 python-office GUI",
            f"<h3>python-office GUI</h3>"
            f"<p>版本：v{__version__}</p>"
            f"<p>主题：Deep Glass</p>"
            f"<p>主页：<a href='https://www.python-office.com'>python-office.com</a></p>"
            f"<p>所有功能均委托给 office.api.* 实现，"
            f"本 GUI 仅是更友好的入口。</p>",
        )

    # ----- 关闭事件：清理线程 -----
    def closeEvent(self, event):
        # 先取消所有正在跑的 JobRunner，等线程真正退出再关闭窗口
        for page in self._pages.values():
            if page._runner and page._runner.isRunning():
                page._runner.terminate()
                if not page._runner.wait(3000):
                    # 3s 后还在跑：再 quit() 一次，兜底
                    page._runner.quit()
                    page._runner.wait(2000)
        super().closeEvent(event)
