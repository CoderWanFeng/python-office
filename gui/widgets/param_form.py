# -*- coding: utf-8 -*-
"""通用控件：单参数表单。"""

from __future__ import annotations

import os
from typing import Any, Callable, Optional

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QDoubleSpinBox, QFileDialog, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QToolButton, QWidget,
)

from gui.registry import Param


class _BaseField(QWidget):
    """抽象字段：暴露 value() / setValue() / clear()。"""

    valueChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # 关键：高度由内容决定、宽度可缩，
        # 但绝不被父布局在垂直方向上挤压成 0。
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setMinimumHeight(32)

    def value(self) -> Any: ...
    def setValue(self, v: Any) -> None: ...
    def clear(self) -> None: ...


class TextField(_BaseField):
    def __init__(self, kind: str = "str", parent=None):
        super().__init__(parent)
        self._kind = kind
        # password 走 QLineEdit（echo mode），text 走 QPlainTextEdit（多行），其余 QLineEdit
        if kind == "password":
            self._edit = QLineEdit()
            self._edit.setEchoMode(QLineEdit.Password)
            self._edit.setPlaceholderText("请输入...")
        elif kind == "text":
            self._edit = QPlainTextEdit()
            self._edit.setPlaceholderText("请输入...")
            self._edit.setFixedHeight(72)
        else:
            self._edit = QLineEdit()
            self._edit.setPlaceholderText("请输入...")
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self._edit)

    def value(self):
        if isinstance(self._edit, QPlainTextEdit):
            return self._edit.toPlainText()
        return self._edit.text()

    def setValue(self, v):
        if v is None:
            return
        if isinstance(self._edit, QPlainTextEdit):
            self._edit.setPlainText(str(v))
        else:
            self._edit.setText(str(v))

    def clear(self):
        if isinstance(self._edit, QPlainTextEdit):
            self._edit.clear()
        else:
            self._edit.clear()


class IntField(_BaseField):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._spin = QSpinBox()
        self._spin.setRange(-1_000_000, 1_000_000)
        self._spin.setValue(0)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self._spin)

    def value(self):
        return self._spin.value()

    def setValue(self, v):
        if v is not None:
            self._spin.setValue(int(v))

    def clear(self):
        self._spin.setValue(0)


class FloatField(_BaseField):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._spin = QDoubleSpinBox()
        self._spin.setRange(-1e9, 1e9)
        self._spin.setDecimals(4)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self._spin)

    def value(self):
        return self._spin.value()

    def setValue(self, v):
        if v is not None:
            self._spin.setValue(float(v))

    def clear(self):
        self._spin.setValue(0.0)


class BoolField(_BaseField):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._cb = QCheckBox("启用")
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self._cb)

    def value(self):
        return self._cb.isChecked()

    def setValue(self, v):
        if v is not None:
            self._cb.setChecked(bool(v))

    def clear(self):
        self._cb.setChecked(False)


class ChoiceField(_BaseField):
    def __init__(self, choices: list, parent=None):
        super().__init__(parent)
        self._combo = QComboBox()
        self._combo.addItems([str(c) for c in choices])
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self._combo)

    def value(self):
        return self._combo.currentText()

    def setValue(self, v):
        if v is None:
            return
        idx = self._combo.findText(str(v))
        if idx >= 0:
            self._combo.setCurrentIndex(idx)

    def clear(self):
        if self._combo.count():
            self._combo.setCurrentIndex(0)


class FileField(_BaseField):
    """单文件 / 多文件 / 目录 / 另存为 通用选择器。

    mode 取值:
        - ``file``  : 选已存在的单个文件（QFileDialog.getOpenFileName）
        - ``files`` : 选已存在的多个文件，多个用分号拼接
        - ``dir``   : 选目录（QFileDialog.getExistingDirectory）
        - ``save``  : 选保存位置（QFileDialog.getSaveFileName），用于 output_* 等参数
    """

    def __init__(self, mode: str = "file", file_filter: str = "",
                 parent=None):
        super().__init__(parent)
        if mode not in ("file", "files", "dir", "save"):
            mode = "file"
        self._mode = mode
        self._filter = file_filter or "All files (*.*)"

        self._edit = QLineEdit()
        self._edit.setPlaceholderText({
            "file":  "选择文件...",
            "files": "选择多个文件（可分号 ; 拼接）...",
            "dir":   "选择目录...",
            "save":  "另存为...",
        }[mode])

        self._browse = QToolButton()
        self._browse.setText("..." if mode == "save" else "Browse")
        self._browse.setCursor(Qt.PointingHandCursor)
        self._browse.setToolTip({
            "file":  "选择文件",
            "files": "选择多个文件",
            "dir":   "选择目录",
            "save":  "另存为",
        }[mode])
        self._browse.clicked.connect(self._browse_clicked)

        # 把 QLineEdit 的 textChanged 透传为 valueChanged，
        # 供 ParamForm 监听以做"派生字段跟随"逻辑。
        # textChanged 带 1 个 str 参数，valueChanged 不带参，这里用 lambda 显式丢弃。
        self._edit.textChanged.connect(lambda *_a: self.valueChanged.emit())

        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self._edit, 1)
        lay.addWidget(self._browse)

    def _browse_clicked(self):
        if self._mode == "dir":
            path = QFileDialog.getExistingDirectory(self, "选择目录")
            if path:
                self._edit.setText(path)
        elif self._mode == "save":
            # 另存为：把当前文本作为默认路径/文件名
            current = self._edit.text() or ""
            path, _ = QFileDialog.getSaveFileName(
                self, "另存为", current, self._filter
            )
            if path:
                self._edit.setText(path)
        else:
            paths, _ = QFileDialog.getOpenFileNames(self, "选择文件", "", self._filter)
            if paths:
                self._edit.setText(";".join(paths) if self._mode == "files" else paths[0])

    def value(self):
        return self._edit.text() or None

    def setValue(self, v):
        if v is not None:
            self._edit.setText(str(v))

    def clear(self):
        self._edit.clear()


def make_field(param: Param) -> _BaseField:
    """根据 Param.kind 创建对应控件。"""
    if param.kind in ("file", "files", "dir", "save"):
        return FileField(mode=param.kind, file_filter=param.file_filter)
    if param.kind == "int":
        return IntField()
    if param.kind == "float":
        return FloatField()
    if param.kind == "bool":
        return BoolField()
    if param.kind in ("text",):
        return TextField(kind="text")
    if param.kind == "password":
        return TextField(kind="password")
    if param.kind == "choice" and param.choices:
        return ChoiceField(param.choices)
    return TextField(kind="str")


class ParamForm(QWidget):
    """根据 Param 列表自动生成表单。

    派生字段自动跟随：当 ``output_file`` 这类 save 字段的对应 ``input_file``
    变化时，output 字段会被重置为基于新 input 派生的默认路径，
    避免"input 已换但 output 还指向上一个文件"的问题。
    """

    valueChanged = Signal()

    def __init__(self, params: list[Param], parent=None):
        super().__init__(parent)
        from PySide6.QtWidgets import QFormLayout

        self._params: list[Param] = list(params)
        self._fields: dict[str, _BaseField] = {}
        # save_name -> input_name 的配对关系
        self._save_pairs: dict[str, str] = {}
        # dir_name -> input_name 的配对关系，用于 PDF 转图片这类输出目录。
        self._dir_pairs: dict[str, str] = {}

        layout = QFormLayout(self)
        layout.setLabelAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.setHorizontalSpacing(18)
        layout.setVerticalSpacing(12)
        layout.setContentsMargins(0, 0, 0, 0)

        for p in self._params:
            field = make_field(p)
            if p.default is not None:
                field.setValue(p.default)
            label_text = p.label + (" *" if p.required else "")
            label = QLabel(label_text)
            if p.placeholder and p.kind not in ("bool",):
                if hasattr(field, "_edit"):
                    field._edit.setPlaceholderText(p.placeholder)
            # 参数说明：同时挂到 label 和 field 上，鼠标悬停任意位置都能看到
            if p.description:
                tip = p.description
                label.setToolTip(tip)
                field.setToolTip(tip)
            layout.addRow(label, field)
            self._fields[p.name] = field
            field.valueChanged.connect(
                lambda n=p.name: self._on_field_changed(n)
            )

        # 构建 save-input 配对，并触发一次初始派生
        for p in self._params:
            if p.kind == "save":
                input_name = self._pair_to_input(p.name)
                if input_name in self._fields:
                    # input 字段为 dir 时不参与配对：dir 没有"文件名"概念，
                    # 不应触发 output_file 的自动派生（避免 with_suffix 出错）。
                    input_param = next(
                        (pp for pp in self._params if pp.name == input_name), None
                    )
                    if input_param and input_param.kind == "dir":
                        continue
                    self._save_pairs[p.name] = input_name
                    self._refresh_save_field(p.name)
            elif p.kind == "dir" and p.name == "output_file":
                input_name = self._pair_to_input(p.name)
                if input_name in self._fields:
                    input_param = next(
                        (pp for pp in self._params if pp.name == input_name), None
                    )
                    if input_param and input_param.kind == "file":
                        self._dir_pairs[p.name] = input_name
                        self._refresh_dir_field(p.name)

    # ----- 派生字段联动 -----
    @staticmethod
    def _pair_to_input(save_name: str) -> str:
        """``output_xxx`` ↔ ``input_xxx``，``xxx_output`` ↔ ``xxx_input``。"""
        if save_name.startswith("output_"):
            return "input_" + save_name[len("output_"):]
        if save_name.endswith("_output"):
            return save_name[: -len("_output")] + "_input"
        return ""

    @staticmethod
    def _suffix_from_filter(flt: str) -> str:
        """从 ``"Word documents (*.docx)"`` 中抽出 ``.docx``；``*.*`` 返回空。"""
        import re
        if not flt:
            return ""
        m = re.search(r"\*\.([a-zA-Z0-9]+)", flt)
        if not m:
            return ""
        ext = m.group(1)
        # 过滤 ``*.*`` 这种"任意文件"伪后缀
        if "*" in ext or "?" in ext:
            return ""
        return "." + ext

    def _on_field_changed(self, name: str) -> None:
        """任一字段变化时检查是否有 save 配对需要重置。"""
        for save_name, in_name in self._save_pairs.items():
            if in_name == name:
                self._refresh_save_field(save_name)
        for dir_name, in_name in self._dir_pairs.items():
            if in_name == name:
                self._refresh_dir_field(dir_name)

    def _refresh_save_field(self, save_name: str) -> None:
        """基于配对 input 字段重新计算 save 字段的派生值。"""
        in_name = self._save_pairs.get(save_name)
        if not in_name:
            return
        in_text = self._fields[in_name].value()
        if not in_text:
            return
        from pathlib import Path
        in_path = Path(in_text)

        save_param = next((p for p in self._params if p.name == save_name), None)
        if save_param is None:
            return

        # 后缀：优先用 save field 当前后缀（用户可能改过），其次 file_filter
        ext = ""
        current = self._fields[save_name].value()
        if current:
            cur_ext = Path(current).suffix
            if cur_ext:
                ext = cur_ext
        if not ext:
            ext = self._suffix_from_filter(save_param.file_filter)
        if not ext:
            ext = ".docx"

        new_path = str(in_path.with_suffix(ext))
        self._fields[save_name].setValue(new_path)

    def _refresh_dir_field(self, dir_name: str) -> None:
        """基于配对 input 文件重新计算输出目录字段的派生值。"""
        in_name = self._dir_pairs.get(dir_name)
        if not in_name:
            return
        in_text = self._fields[in_name].value()
        if not in_text:
            return
        from pathlib import Path
        in_path = Path(in_text)
        new_path = str(in_path.parent / f"{in_path.stem}_images")
        self._fields[dir_name].setValue(new_path)

    # ----- 公共 API -----
    def collect(self) -> dict:
        """收集当前表单值，按 Param 规则做类型转换，None 字段自动剔除。"""
        result = {}
        for p in self._params:
            if p.name not in self._fields:
                continue
            raw = self._fields[p.name].value()
            value = p.to_widget_value(raw)
            if value is not None and value != "":
                result[p.name] = value
        return result

    def set_value(self, name: str, value: Any) -> None:
        if name in self._fields:
            self._fields[name].setValue(value)
