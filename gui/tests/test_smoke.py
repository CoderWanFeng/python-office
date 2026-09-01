# -*- coding: utf-8 -*-
"""Lightweight tests for the optional PySide6 GUI layer."""

from __future__ import annotations

import warnings


def test_deprecated_params_warns_and_remaps():
    from office.lib.decorator_utils import deprecated_params

    @deprecated_params({"old_name": "new_name"})
    def fn(new_name=None, old_name=None):
        return new_name

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = fn(old_name="x")

    assert result == "x"
    assert any(issubclass(item.category, DeprecationWarning) for item in caught)


def test_registry_builds_expected_categories():
    from gui.registry import build_registry

    cats = build_registry()
    ids = {cat.id for cat in cats}

    assert ids >= {
        "pdf",
        "excel",
        "word",
        "ppt",
        "image",
        "file",
        "video",
        "email",
        "tools",
    }
    assert all(cat.features for cat in cats)


def test_feature_params_are_resolved_lazily():
    from gui.registry import build_registry, resolve_feature

    cats = build_registry()
    feature = next(
        item
        for cat in cats
        if cat.id == "pdf"
        for item in cat.features
        if item.id == "pdf2docx"
    )

    assert feature.resolved is False
    assert feature.params == []

    resolve_feature(feature)

    assert feature.resolved is True
    assert {param.name for param in feature.params} >= {
        "input_file",
        "output_file",
        "input_path",
        "output_path",
    }


def test_pdf2imgs_passes_output_file(monkeypatch):
    import office.api.pdf as api_pdf

    captured = {}

    def fake_pdf2imgs(**kwargs):
        captured.update(kwargs)

    monkeypatch.setattr(api_pdf.popdf, "pdf2imgs", fake_pdf2imgs)

    api_pdf.pdf2imgs(input_file="input.pdf", output_file="images", merge=False)

    assert captured == {
        "input_file": "input.pdf",
        "output_file": "images",
        "merge": False,
    }


def test_add_text_watermark_calls_current_popdf_api(monkeypatch):
    import office.api.pdf as api_pdf

    captured = {}

    def fake_add_text_watermark(**kwargs):
        captured.update(kwargs)

    monkeypatch.setattr(api_pdf.popdf, "add_text_watermark", fake_add_text_watermark)

    api_pdf.add_text_watermark(
        input_file="input.pdf",
        output_file="output.pdf",
        point="(10, 20)",
        color="(0, 0, 1)",
    )

    assert captured == {
        "input_file": "input.pdf",
        "point": (10.0, 20.0),
        "text": "python-office",
        "output_file": "output.pdf",
        "fontname": "Helvetica",
        "fontsize": 20,
        "color": (0.0, 0.0, 1.0),
    }


def test_add_text_watermark_output_file_filter_is_pdf():
    from gui.registry import build_registry, resolve_feature

    cats = build_registry()
    feature = next(
        item
        for cat in cats
        if cat.id == "pdf"
        for item in cat.features
        if item.id == "add_text_watermark"
    )
    resolve_feature(feature)

    output = next(param for param in feature.params if param.name == "output_file")
    assert output.kind == "save"
    assert "pdf" in output.file_filter.lower()
    assert "docx" not in output.file_filter.lower()


def test_pdf2imgs_output_file_is_output_dir():
    """pdf2imgs 常用模式下 output_file 实际是输出目录，不能显示为 docx 另存为。"""
    from gui.registry import build_registry, resolve_feature

    cats = build_registry()
    feature = next(
        item
        for cat in cats
        if cat.id == "pdf"
        for item in cat.features
        if item.id == "pdf2imgs"
    )
    resolve_feature(feature)

    output = next(param for param in feature.params if param.name == "output_file")
    assert output.kind == "dir"
    assert output.label == "输出目录"
    assert ".docx" not in output.placeholder.lower()


def test_output_dir_resets_when_input_file_changes():
    """输出目录字段跟随输入文件派生为 <stem>_images。"""
    import os

    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    warnings.simplefilter("ignore")

    from PySide6.QtWidgets import QApplication

    app = QApplication.instance() or QApplication([])

    from gui.registry import Param
    from gui.widgets import ParamForm

    def norm(path):
        return os.path.normpath(path)

    params = [
        Param(name="input_file", label="Input File", kind="file",
              file_filter="PDF files (*.pdf)"),
        Param(name="output_file", label="Output Dir", kind="dir"),
    ]
    form = ParamForm(params)

    form._fields["input_file"].setValue("D:/docs/report.pdf")
    assert norm(form._fields["output_file"].value()) == norm("D:/docs/report_images")

    form._fields["input_file"].setValue("D:/docs/manual.pdf")
    assert norm(form._fields["output_file"].value()) == norm("D:/docs/manual_images")


def test_feature_cards_are_actionable_or_explained():
    from gui.registry import build_registry

    cats = build_registry()

    features = [feature for cat in cats for feature in cat.features]

    assert features
    assert all(
        not feature.cli_only or feature.cli_command
        for feature in features
    )


def test_param_to_widget_value_conversions():
    from gui.registry import Param

    assert Param(name="x", label="X", kind="int").to_widget_value("42") == 42
    assert Param(name="x", label="X", kind="int").to_widget_value("bad") is None
    assert Param(name="x", label="X", kind="float").to_widget_value("3.14") == 3.14
    assert Param(name="x", label="X", kind="files").to_widget_value("a.pdf;b.pdf") == [
        "a.pdf",
        "b.pdf",
    ]
