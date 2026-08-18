# -*- coding: utf-8 -*-
"""功能面板：根据 Feature 动态生成的参数表单 + 运行按钮 + 日志视图。

布局策略（关键）：
    上半部分用 QScrollArea 包裹「标题 / 描述 / 备注 / 文档链接 / 参数 / 操作按钮」，
    窗口高度缩小时出滚动条而不是把输入框挤压；下半部分是日志视图，固定
    最小高度并随窗口下沿一起伸缩，永远看得见。
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QLabel, QMessageBox, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSplitter, QTextBrowser,
    QVBoxLayout, QWidget,
)

from gui.registry import Feature
from gui.styles import BLUE, BLUE_SOFT, LINE, SURFACE_ALT, TEXT, TEXT_MUTED
from gui.widgets import ParamForm
from gui.workers import JobRunner, make_runner


class FeaturePage(QWidget):
    """单个功能的展示页。"""

    def __init__(self, feature: Feature, parent=None):
        super().__init__(parent)
        self.setObjectName("pageRoot")
        self._feature = feature
        self._runner: JobRunner | None = None
        self._build_ui()

    # ----- UI 构建 -----
    def _build_ui(self):
        # 顶层用 QSplitter 上下分割：上半滚动 + 下半日志
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        splitter = QSplitter(Qt.Vertical)
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(1)
        outer.addWidget(splitter)

        # ----- 上半：可滚动的内容 -----
        top = QWidget()
        top.setObjectName("pageContent")
        top_lay = QVBoxLayout(top)
        top_lay.setContentsMargins(36, 28, 36, 18)
        top_lay.setSpacing(14)

        title = QLabel(self._feature.title)
        title.setObjectName("pageTitle")
        top_lay.addWidget(title)

        if self._feature.desc:
            desc = QLabel(self._feature.desc)
            desc.setObjectName("pageDesc")
            desc.setWordWrap(True)
            top_lay.addWidget(desc)

        if self._feature.platform_note:
            note = QLabel(f"[i] {self._feature.platform_note}")
            note.setStyleSheet("color: #C2410C; font-size: 12px;")
            note.setWordWrap(True)
            top_lay.addWidget(note)

        # 纯展示功能（info_html 非空）：直接渲染信息卡片，无按钮/无日志/无 CLI
        if self._feature.info_html:
            info_card = self._make_info_card()
            top_lay.addWidget(info_card, 1)
            scroll = self._wrap_scroll(top)
            splitter.addWidget(scroll)
            self._log = None
            splitter.setStretchFactor(0, 1)
            return

        # CLI 交互式功能：显示命令行使用说明（不弹警告）
        if self._feature.cli_only:
            cli_card = self._make_cli_card()
            top_lay.addWidget(cli_card)
            top_lay.addStretch(1)
            scroll = self._wrap_scroll(top)
            splitter.addWidget(scroll)
            # CLI 卡片页不需要运行按钮/日志区
            self._log = None
            return

        if self._feature.is_placeholder:
            placeholder_card = self._make_placeholder_card()
            top_lay.addWidget(placeholder_card)
            top_lay.addStretch(1)
            scroll = self._wrap_scroll(top)
            splitter.addWidget(scroll)
            # 占位卡页只需要上半就够了，禁用下半
            self._log = None
            return

        if self._feature.params:
            form_card = self._make_card("参数")
            self._form = ParamForm(self._feature.params)
            self._form.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            form_card.layout().addWidget(self._form)
            top_lay.addWidget(form_card)
        else:
            self._form = None

        action_row = QHBoxLayout()
        self._run_btn = QPushButton("运行")
        self._run_btn.setObjectName("primaryButton")
        self._run_btn.setCursor(Qt.PointingHandCursor)
        self._run_btn.clicked.connect(self._on_run)
        action_row.addWidget(self._run_btn)

        self._cancel_btn = QPushButton("停止")
        self._cancel_btn.setObjectName("dangerButton")
        self._cancel_btn.setEnabled(False)
        self._cancel_btn.clicked.connect(self._on_cancel)
        action_row.addWidget(self._cancel_btn)

        self._clear_btn = QPushButton("清空日志")
        self._clear_btn.clicked.connect(self._on_clear_log)
        action_row.addWidget(self._clear_btn)
        action_row.addStretch(1)
        top_lay.addLayout(action_row)

        scroll = self._wrap_scroll(top)
        splitter.addWidget(scroll)

        # ----- 下半：日志卡片 -----
        log_card = self._make_card("运行日志")
        self._log = QPlainTextEdit()
        self._log.setObjectName("logView")
        self._log.setReadOnly(True)
        self._log.setMinimumHeight(180)
        log_card.layout().addWidget(self._log)
        log_wrap = QWidget()
        log_wrap.setObjectName("pageContent")
        log_lay = QVBoxLayout(log_wrap)
        log_lay.setContentsMargins(36, 0, 36, 18)
        log_lay.setSpacing(0)
        log_lay.addWidget(log_card)
        splitter.addWidget(log_wrap)

        # 默认高度分配：上半多、日志至少 240（一倍高度 = 360）
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)
        splitter.setSizes([420, 300])
        splitter.setCollapsible(0, False)
        splitter.setCollapsible(1, False)

    def _wrap_scroll(self, inner: QWidget) -> QScrollArea:
        """把 inner 包进 QScrollArea，仅垂直滚动，水平永远不出滚动条。"""
        area = QScrollArea()
        area.setWidgetResizable(True)
        area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        area.setFrameShape(QFrame.NoFrame)
        area.setWidget(inner)
        return area

    def _make_card(self, title: str) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout(card)
        v.setContentsMargins(24, 18, 24, 22)
        v.setSpacing(14)
        lbl = QLabel(title)
        lbl.setObjectName("cardTitle")
        v.addWidget(lbl)
        return card

    def _make_placeholder_card(self) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout(card)
        v.setContentsMargins(20, 18, 20, 18)
        v.setSpacing(8)
        lbl = QLabel("该功能尚未在本项目中提供 GUI 入口。")
        lbl.setObjectName("cardTitle")
        v.addWidget(lbl)
        hint = QLabel(
            "可能原因：\n"
            "  • 对应子包未安装：请使用 pip install python-office[all] 或单独安装\n"
            "  • office.api.<模块> 中暂无对应函数实现\n\n"
            "解决方案：按提示安装依赖后重启 GUI。"
        )
        hint.setStyleSheet(f"color: {TEXT_MUTED};")
        hint.setWordWrap(True)
        v.addWidget(hint)
        return card

    def _make_info_card(self) -> QFrame:
        """纯展示卡片：用 QTextBrowser 渲染 Feature.info_html，支持超链接。"""
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout(card)
        v.setContentsMargins(24, 20, 24, 20)
        v.setSpacing(8)

        browser = QTextBrowser()
        browser.setObjectName("infoBrowser")
        browser.setOpenExternalLinks(True)  # 让 <a href> 点击后用系统浏览器打开
        browser.setHtml(self._feature.info_html)
        browser.setMinimumHeight(560)
        browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        browser.setStyleSheet(
            "QTextBrowser#infoBrowser {"
            " background: transparent; border: none;"
            f" color: {TEXT};"
            "}"
            f"QTextBrowser#infoBrowser a {{ color: {BLUE}; text-decoration: none; }}"
            "QTextBrowser#infoBrowser a:hover { text-decoration: underline; }"
            f"QTextBrowser#infoBrowser h2, h3 {{ color: {TEXT}; }}"
            f"QTextBrowser#infoBrowser hr {{ color: {LINE}; }}"
            "QTextBrowser#infoBrowser code {"
            f"  background: {SURFACE_ALT}; padding: 2px 6px; border-radius: 4px;"
            f"  color: {TEXT}; font-family: 'SF Mono', 'Cascadia Mono', Consolas, monospace;"
            "}"
        )
        v.addWidget(browser)
        return card

    def _make_cli_card(self) -> QFrame:
        """CLI 交互式卡片：提示用户在终端使用，并给出可复制的命令行示例。"""
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout(card)
        v.setContentsMargins(20, 18, 20, 18)
        v.setSpacing(10)

        lbl = QLabel("CLI 交互式功能 · 请在终端使用")
        lbl.setObjectName("cardTitle")
        v.addWidget(lbl)

        hint = QLabel(
            "此功能需要按命令行提示交互操作（如选择城市、确认号码等），\n"
            "GUI 不适合实时交互，请在 PowerShell / CMD / 终端中运行。"
        )
        hint.setStyleSheet(f"color: {TEXT_MUTED};")
        hint.setWordWrap(True)
        v.addWidget(hint)

        # 命令行示例（只读、可全选复制）
        example = QPlainTextEdit()
        example.setObjectName("cliExample")
        example.setReadOnly(True)
        example.setPlainText(
            self._feature.cli_command
            or f"python -c \"from {self._feature.callable.__module__} "
               f"import {self._feature.callable.__name__}; "
               f"{self._feature.callable.__name__}()\""
        )
        # 自适应高度（8 行左右），避免撑得太高
        example.setMinimumHeight(140)
        example.setMaximumHeight(180)
        example.setStyleSheet(
            "QPlainTextEdit#cliExample {"
            " background: #F8FAFC; color: #134E4A;"
            " border: 1px solid rgba(13, 148, 136, 0.18); border-radius: 10px;"
            " padding: 12px; font-family: 'SF Mono', 'Cascadia Mono', Consolas, monospace;"
            " font-size: 12px;"
            "}"
        )
        v.addWidget(example)

        # 复制按钮
        copy_btn = QPushButton("复制命令到剪贴板")
        copy_btn.setCursor(Qt.PointingHandCursor)
        copy_btn.clicked.connect(
            lambda: QApplication.clipboard().setText(example.toPlainText())
        )
        v.addWidget(copy_btn, 0, Qt.AlignRight)

        return card

    # ----- 槽 -----
    def _on_run(self):
        if self._runner is not None and self._runner.isRunning():
            return

        if self._feature.is_placeholder:
            QMessageBox.information(
                self, "提示",
                "该功能尚未实现，请先安装对应依赖。",
            )
            return

        if self._feature.cli_only:
            # CLI 交互式不在 GUI 里运行 —— 引导用户去终端
            cmd = self._feature.cli_command or (
                f"python -c \"from {self._feature.callable.__module__} "
                f"import {self._feature.callable.__name__}; "
                f"{self._feature.callable.__name__}()\""
            )
            QMessageBox.information(
                self, "CLI 交互式功能",
                f"此功能需要在终端命令行里按提示交互操作。\n\n"
                f"请打开 PowerShell / CMD，激活 python-office 环境后执行：\n\n"
                f"{cmd}",
            )
            return

        kwargs = self._form.collect() if self._form else {}

        if self._log is not None:
            self._log.appendPlainText(
                f"▶ 开始执行：{self._feature.title}\n  参数：{kwargs}\n"
            )
        self._run_btn.setEnabled(False)
        self._cancel_btn.setEnabled(True)

        self._runner = make_runner(self._feature.callable, kwargs)
        self._runner.log.connect(self._append_log)
        self._runner.job_finished.connect(self._on_finished)
        self._runner.start()

    def _on_cancel(self):
        if self._runner and self._runner.isRunning():
            self._runner.terminate()
            self._runner.wait(500)
            self._append_log("[用户取消]")
            self._on_finished(False, "✗ 已取消")

    def _on_clear_log(self):
        if self._log is not None:
            self._log.clear()

    def _append_log(self, text: str):
        if self._log is None:
            return
        self._log.appendPlainText(text.rstrip())
        sb = self._log.verticalScrollBar()
        sb.setValue(sb.maximum())

    def _on_finished(self, success: bool, msg: str):
        if self._log is not None:
            self._log.appendPlainText(msg + "\n")
        self._run_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)
        self._runner = None
