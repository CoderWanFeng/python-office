# -*- coding: utf-8 -*-
"""功能注册表（schema-driven + 自动反射）。

设计思路：
    1. 每个 ``Category`` 持一组 ``Feature``；
    2. ``Feature`` 的可执行体 ``callable`` 直接指向 ``office.api.<cat>.<func>``，
       参数表单由 ``inspect.signature`` 自动生成；
    3. 参数名 / 默认值启发式映射为合适的 GUI 控件：
       - 名字含 path / file / input / output / pdf / image → 文件选择
       - 名字含 dir / folder → 目录选择
       - bool 默认值 → 复选框
       - int / float 默认值 → SpinBox
       - 其余 → 单行/多行文本
    4. office.api 暂未提供实现的模块（如 email / ai / time / han）保留为
       "占位卡片"，引导用户安装对应子包后再启用，避免空架子。

新增 office.api 函数后，``build_registry()`` 反射即可让 GUI 多出一个
功能入口，无需手动改本文件。
"""

from __future__ import annotations

import importlib
import inspect
from dataclasses import dataclass, field
from typing import Any, Callable, Optional


# -------- 数据结构 --------

@dataclass
class Param:
    """单个参数的 UI 表单描述。"""
    name: str
    label: str
    kind: str  # 'file' | 'files' | 'dir' | 'str' | 'text' | 'int' | 'float' | 'bool' | 'password'
    default: Any = None
    placeholder: str = ""
    required: bool = False
    choices: list = field(default_factory=list)
    file_filter: str = ""  # e.g. "PDF files (*.pdf)"
    description: str = ""  # 鼠标悬停时显示的参数说明

    def to_widget_value(self, raw: Any) -> Any:
        """把表单控件的 raw value 转成函数调用期望的类型。"""
        if raw is None or raw == "":
            return None
        if self.kind in ("int",):
            try:
                return int(raw)
            except (TypeError, ValueError):
                return None
        if self.kind in ("float",):
            try:
                return float(raw)
            except (TypeError, ValueError):
                return None
        if self.kind == "bool":
            return bool(raw)
        if self.kind in ("files",) and isinstance(raw, str):
            return [p.strip() for p in raw.split(";") if p.strip()]
        if self.kind in ("text",) and isinstance(raw, str):
            return raw
        return raw


@dataclass
class Feature:
    """一个可执行的功能单元。"""
    id: str
    title: str
    desc: str
    callable: Callable
    params: list[Param] = field(default_factory=list)
    docs_url: str = ""
    is_async: bool = False
    is_placeholder: bool = False  # 占位卡：office.api 中暂无对应函数
    platform_note: str = ""       # 平台限制说明
    cli_only: bool = False        # CLI 交互式：GUI 不直接执行，提示用户在终端调用
    cli_command: str = ""         # 给用户的 CLI 调用示例（python -m ...）
    info_html: str = ""           # 纯展示内容（HTML 格式）；非空时右侧只显示该卡片，无按钮/无日志
    module_path: str = ""
    func_name: str = ""
    param_descriptions: dict[str, str] = field(default_factory=dict)
    param_overrides: dict[str, dict] = field(default_factory=dict)
    resolved: bool = False


@dataclass
class Category:
    """左侧栏一级分类。"""
    id: str
    title: str
    icon: str
    order: int
    features: list[Feature] = field(default_factory=list)


# -------- 启发式参数映射 --------

# file 词根：仅当名字真正像"文件名"时才算
_FILE_HINTS = ("file", "image", "img", "pic", "photo", "document", "word",
               "pdf", "doc", "docx", "excel", "xlsx", "audio", "video",
               "mp3", "mp4", "mark", "qrcode", "src", "dest", "filename")
# 目录词根：含 path / dir / folder / directory 单独出现就算
_DIR_HINTS = ("path", "dir", "folder", "directory")
_LANG_HINTS = ("lang", "language")
_PASSWORD_HINTS = ("password", "pwd", "passwd")


def _looks_like_dir(n: str) -> bool:
    """判定参数名更像"目录"而不是"文件"。

    规则：
        - 名字本身等于 dir/folder/directory → dir
        - 名字以 _dir / _folder / _directory 结尾 → dir
        - 名字以 _path 结尾但不含 file 词根或显式后缀关键词（pdf/docx/...） → dir
        - 单字 path 视为 file（避免和 fake2excel.path 这类输出文件冲突）
    """
    if n in ("dir", "folder", "directory"):
        return True
    if n.endswith(("_dir", "_folder", "_directory")):
        return True
    if n.endswith("_path"):
        # 含 file 词根或显式后缀关键词 → 视为文件（pdf_path / excel_path / image_path）
        if "file" in n:
            return False
        for hint in _FILE_HINTS:
            if hint in n:
                return False
        return True
    return False


def _looks_like_file(n: str) -> bool:
    """判定参数名更像"单个文件"（file/save 控件）。"""
    if "file" in n or n == "path":
        return True
    for hint in _FILE_HINTS:
        if hint in n:
            return True
    return False


def _is_output(n: str) -> bool:
    return (n.startswith("output") or n.startswith("save_") or
            n.endswith("_output") or n == "output")


def _param_label(name: str) -> str:
    """参数名 → 中文标签。优先查 _LABEL_TRANSLATIONS，缺失则回退英文。"""
    n = name.strip()
    if n in _LABEL_TRANSLATIONS:
        return _LABEL_TRANSLATIONS[n]
    pretty = n.replace("_", " ").strip()
    return " ".join(w.capitalize() for w in pretty.split()) or n


# 全局参数名 → 中文 label 映射（新手友好优先用中文）
_LABEL_TRANSLATIONS: dict[str, str] = {
    # 通用文件 / 路径
    "input_file":       "输入文件",
    "output_file":      "输出文件",
    "input_path":       "输入目录",
    "output_path":      "输出目录",
    "dir_path":         "目录",
    "file_path":        "文件路径",
    "filepath":         "文件路径",
    "path":             "文件路径",
    "input_dir":        "输入目录",
    "target_dir":       "搜索目录",
    "file_type":        "文件类型",
    "suffix":           "后缀名",
    "output_name":      "输出文件名",
    "new_word_name":    "新文件名",

    # 邮件
    "key":              "授权码",
    "msg_from":         "发件人",
    "msg_to":           "收件人",
    "msg_cc":           "抄送",
    "msg_subject":      "主题",
    "attach_files":     "附件",
    "host":             "服务器",
    "port":             "端口",
    "status":           "状态",

    # 输出格式相关
    "output_image":     "输出图片",
    "output_pdf":       "输出 PDF",
    "output_excel":     "输出 Excel",
    "output_excel_name": "输出文件名",
    "output_sheet_name": "合并表名",
    "output":           "输出文件",
    "result_file":      "词云图",
    "mp3_name":         "MP3 名称",
    "mp3":              "MP3 文件",

    # PDF / Word / PPT
    "pdf_path":         "输出 PDF",
    "excel_path":       "输入 Excel",
    "word_path":        "Word 文件",
    "img_path":         "图片输出目录",
    "sheet_id":         "工作表序号",
    "worksheet_name":   "工作表名",
    "from_page":        "起始页",
    "to_page":          "结束页",
    "page_nums":        "要删除的页码",

    # 加密 / 解密
    "password":         "密码",

    # 水印
    "mark_file":        "水印图片",
    "mark_str":         "水印内容",
    "mark":             "水印文字",
    "text":             "水印文字",
    "fontname":         "字体",
    "fontsize":         "字号",
    "font_size":        "字号",
    "font_type":        "字体",
    "font_color":       "字体颜色",
    "color":            "颜色",
    "opacity":          "不透明度",
    "space":            "水印间距",
    "size":             "水印大小",
    "angle":            "旋转角度",
    "point":            "位置坐标",

    # Excel
    "columns":          "列名",
    "rows":             "行数",
    "language":         "语言",
    "column":           "列号",
    "sheet_name":       "工作表名",

    # 图片处理
    "file":             "文件",
    "input_img":        "输入图片",
    "input_image":      "输入图片",
    "output_image":     "输出图片",
    "output_path":      "输出目录",
    "output_name":      "输出文件名",
    "quality":          "压缩质量",
    "qrcode_path":      "二维码图片",
    "filename":         "文本文件",
    "url":              "网址",
    "type":             "文件类型",
    "client_api":       "百度 API Key",
    "client_secret":    "百度 Secret Key",

    # 视频
    "video_path":       "视频文件",
    "audio_path":       "音频文件",
    "content":          "文本内容",
    "file":             "文件",
    "speak":            "是否朗读",
    "merge":            "合并为长图",
    "appid":            "AppID（应用 ID）",
    "secret_id":        "SecretId（密钥 ID）",
    "secret_key":       "SecretKey（密钥）",

    # OCR
    "img_url":          "图片 URL",
    "id":               "腾讯云 ID",
    "key":              "腾讯云 Key",
    "file_name":        "按文件名命名",
    "trans":            "是否翻译",

    # 文件管理
    "search_key":       "搜索关键词",
    "del_content":      "要删除的内容",
    "replace_content":  "替换为",
    "dir_rename":       "同时重命名文件夹",
    "file_rename":      "同时重命名文件",
    "prefix_content":   "前缀内容",
    "postfix_content":  "后缀内容",
    "insert_content":   "插入内容",
    "insert_position":  "插入位置",
    "add_line_dict":    "行内容",
    "name":             "文件名关键字",
    "sub":              "包含子目录",
    "level":            "搜索深度",
    "del_old_file":     "删除旧文件",

    # 工具
    "to_lang":          "目标语言",
    "from_lang":        "源语言",
    "theme":            "文章主题",
    "line_num":         "字数",
    "len":              "密码长度",
    "len_pwd":          "密码长度",
    "pwd_list":         "密码字符集",

    # 微信
    "who":              "好友 / 群名",
    "message":          "消息内容",
    "time":             "发送时间",
    "keywords":         "关键词",
    "txt":              "消息文件名",

    # 网络
    "tile":             "标题",

    # 弃用参数（保留兼容）
    "out_dir":          "输出目录（旧）",
    "input_file_list":  "PDF 列表",
    "one_by_one":       "PDF 列表（旧）",
    "output_file_name": "输出文件名（旧）",
    "pdf_file":         "PDF 文件（旧）",
    "file":             "文件",

    # 金融
    "buy_price":        "买入价",
    "sale_price":       "卖出价",
    "shares":           "股数",
    "w_rate":           "手续费率",
    "min_rate":         "最低收费",
    "stamp_tax":        "印花税率",
}


def _looks_like_str_only(n: str) -> bool:
    """参数名更像"纯文本输入"（用户输入字符串，不是文件路径）。

    典型场景：合并后的新文件名、主题、关键词、密码等。
    """
    if n in ("name", "text", "theme", "lang", "language", "title", "tile"):
        return True
    if n.endswith(("_name", "_text", "_theme", "_title", "_lang")):
        return True
    return False


def _resolve_annotation_kind(annotation: Any) -> str | None:
    """从函数参数注解推断简单控件 kind。

    注意：``annotation`` 可能是类型本身（``float``）也可能是字符串
    （``"float"``），两种情况都要处理。
    """
    if annotation is inspect.Parameter.empty:
        return None
    # 直接类型
    if annotation is bool:
        return "bool"
    if annotation is int:
        return "int"
    if annotation is float:
        return "float"
    if annotation is str:
        return "str"
    # 字符串形式（含 "typing.List[str]" 等）
    name = getattr(annotation, "__name__", None)
    if name is None:
        # typing 形式（List[str] 等）
        s = str(annotation).lower()
        if "list[" in s or s.startswith("list"):
            return "list"
        if s in ("int", "builtins.int"):
            return "int"
        if s in ("float", "builtins.float"):
            return "float"
        if s in ("bool", "builtins.bool"):
            return "bool"
        if s in ("str", "builtins.str"):
            return "str"
        return None
    name_lower = name.lower()
    return {
        "bool": "bool",
        "int": "int",
        "float": "float",
        "str": "str",
        "list": "list",
    }.get(name_lower)


def _infer_param_kind(name: str, default: Any, annotation: Any) -> tuple[str, str]:
    """根据参数名/默认值/类型注解推断 UI 控件种类及文件过滤器。

    优先级：
        1. 密码字段 → password
        2. list[...] 类型注解 → files / text
        3. 看起来像"纯文本输入"（name / theme / text / ...）→ str
        4. 看起来像目录（path/dir/folder/directory） → dir
        5. 看起来像文件（file/image/pdf/docx/...） → file 或 save（按 output 前缀）
        6. 其它：按 annotation / default 推断 bool/int/float
    """
    n = name.lower()
    annotation_str = str(annotation).lower() if annotation is not inspect.Parameter.empty else ""

    if any(h in n for h in _PASSWORD_HINTS):
        return "password", ""

    if "list[" in annotation_str or annotation_str.startswith("list"):
        if _looks_like_file(n) or _looks_like_dir(n):
            return "files", ""
        return "text", ""

    # 纯文本类判定优先于文件/目录类：避免 new_word_name / theme / lang 等
    # 含 word/document 等后缀关键词时被误判为 file/save
    if _looks_like_str_only(n):
        return "str", ""

    # 目录类判定优先于文件类：避免 input_path 被 "path" 误识别为 file
    if _looks_like_dir(n):
        return "dir", ""

    if _looks_like_file(n):
        suffix = _suffix_for_filename(n)
        kind = "save" if _is_output(n) else "file"
        return kind, suffix

    # 类型注解优先（直接用 ``is`` 比较类型本身）
    anno_kind = _resolve_annotation_kind(annotation)
    if anno_kind == "list":
        return "text", ""
    if anno_kind in ("bool", "int", "float"):
        return anno_kind, ""

    # 默认值类型
    if isinstance(default, bool):
        return "bool", ""
    if isinstance(default, int):
        return "int", ""
    if isinstance(default, float):
        return "float", ""

    return "str", ""


def _suffix_for_filename(n: str) -> str:
    """根据参数名推断合适的文件扩展名过滤器。"""
    if n.endswith("pdf") or "_pdf" in n or "pdf_" in n:
        return "PDF files (*.pdf)"
    if "image" in n or "img" in n or "pic" in n:
        return "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
    if "excel" in n or n.endswith("xlsx") or "xlsx" in n:
        return "Excel files (*.xlsx *.xls *.csv)"
    if "doc" in n:
        return "Word files (*.doc *.docx)"
    if "ppt" in n:
        return "PowerPoint files (*.ppt *.pptx)"
    if "audio" in n or "mp3" in n:
        return "Audio files (*.mp3 *.wav *.m4a *.flac)"
    if "video" in n or "mp4" in n:
        return "Video files (*.mp4 *.avi *.mov *.mkv)"
    if "txt" in n:
        return "Text files (*.txt *.md)"
    return "All files (*.*)"


def _params_from_signature(func: Callable) -> list[Param]:
    """从函数签名生成参数列表（自动跳过 **kwargs）。"""
    try:
        sig = inspect.signature(func)
    except (TypeError, ValueError):
        return []

    params: list[Param] = []
    for p in sig.parameters.values():
        if p.kind in (inspect.Parameter.VAR_POSITIONAL,
                      inspect.Parameter.VAR_KEYWORD):
            continue
        kind, file_filter = _infer_param_kind(p.name, p.default, p.annotation)
        default = None if p.default is inspect.Parameter.empty else p.default
        params.append(Param(
            name=p.name,
            label=_param_label(p.name),
            kind=kind,
            default=default,
            placeholder=str(default) if default not in (None, "") else "",
            required=(p.default is inspect.Parameter.empty),
            file_filter=file_filter,
        ))
    return params


# 手动给个别函数附加 placeholder / 默认值 / file_filter，弥补反射的不足
_PARAM_OVERRIDES: dict[tuple[str, str], dict[str, dict]] = {
    ("office.api.pdf", "pdf2docx"): {
        "output_file": {
            "placeholder": "留空则输出到 <输入文件同目录>/<同名>.docx",
            "file_filter": "Word documents (*.docx)",
        },
    },
}


def _apply_param_overrides(module_path: str, func_name: str,
                           params: list[Param]) -> list[Param]:
    """应用手动 placeholder / 默认值补丁。"""
    overrides = _PARAM_OVERRIDES.get((module_path, func_name))
    if not overrides:
        return params
    for p in params:
        ov = overrides.get(p.name)
        if ov:
            for k, v in ov.items():
                setattr(p, k, v)
    return params


def _try_import(module_path: str):
    """安全 import 子模块，失败返回 None。"""
    try:
        return importlib.import_module(module_path)
    except Exception:
        return None


def _lazy_callable(*args, **kwargs):
    raise RuntimeError("功能尚未加载，请重新打开该功能页后再试。")


def _resolve_params(func: Callable,
                    module_path: str,
                    func_name: str,
                    param_descriptions: dict[str, str] | None = None,
                    param_overrides: dict[str, dict] | None = None) -> list[Param]:
    params = _params_from_signature(func)
    params = _apply_param_overrides(module_path, func_name, params)
    if param_overrides:
        for p in params:
            ov = param_overrides.get(p.name)
            if ov:
                for k, v in ov.items():
                    setattr(p, k, v)
    if param_descriptions:
        for p in params:
            if p.name in param_descriptions:
                p.description = param_descriptions[p.name]
    return params


def resolve_feature(feature: Feature) -> Feature:
    """Import and inspect a feature only when its page is first opened."""
    if feature.resolved:
        return feature
    if feature.cli_only or feature.info_html or feature.is_placeholder:
        feature.resolved = True
        return feature

    mod = _try_import(feature.module_path)
    func = getattr(mod, feature.func_name, None) if mod else None
    if callable(func):
        feature.callable = func
        feature.params = _resolve_params(
            func,
            feature.module_path,
            feature.func_name,
            feature.param_descriptions,
            feature.param_overrides,
        )
        feature.is_placeholder = False
    else:
        feature.callable = lambda: None
        feature.params = []
        feature.is_placeholder = True
        if not feature.platform_note:
            feature.platform_note = "office.api 中暂时无法加载对应实现。请检查依赖是否完整。"
    feature.resolved = True
    return feature


def _build_feature(feature_id: str, title: str, desc: str,
                   module_path: str, func_name: str,
                   docs_url: str = "", platform_note: str = "",
                   param_descriptions: dict[str, str] = None,
                   param_overrides: dict[str, dict] = None,
                   is_placeholder: bool = False,
                   cli_only: bool = False,
                   cli_command: str = "",
                   info_html: str = "") -> Feature:
    """从一个 office.api.<m>.<func> 函数构造 Feature；找不到则降级为占位。

    Args:
        param_descriptions: ``{参数名: 说明文本}``，会作为 tooltip 提示用户
            这个参数是干嘛的。优先级：函数签名 docstring > _PARAM_OVERRIDES >
            此处传入的 param_descriptions。
        param_overrides: ``{参数名: {字段: 值}}``，可覆盖 ``kind`` / ``file_filter`` /
            ``placeholder`` / ``default`` / ``description``。用于修正反射推断错误的
            控件类型（例如 ``pdf_path`` 应为 save 而不是 dir）。
        is_placeholder: True=强制标为占位卡（即使底层函数存在），用于
            CLI 交互式入口（GUI 中无意义）等场景。
        cli_only: True=标记为 CLI 交互式（GUI 不直接执行）。区别于 is_placeholder：
            cli_only 不会弹"未实现"警告，而是显示"在命令行怎么调"的说明。
        cli_command: 给用户的 CLI 调用示例（多行字符串）。仅 cli_only=True 时有效。
        info_html: 纯展示内容（HTML 格式）。非空时右侧只显示该卡片，无按钮 / 无日志，
            适用于"项目信息"这种无副作用的纯展示功能。
    """
    if cli_only:
        return Feature(
            id=feature_id, title=title, desc=desc,
            callable=lambda: None,
            params=[], docs_url=docs_url,
            platform_note=platform_note,
            cli_only=True,
            cli_command=cli_command,
            info_html=info_html,
            module_path=module_path,
            func_name=func_name,
            resolved=True,
        )

    if not is_placeholder:
        return Feature(
            id=feature_id, title=title, desc=desc,
            callable=_lazy_callable, params=[], docs_url=docs_url,
            platform_note=platform_note,
            cli_only=cli_only,
            cli_command=cli_command,
            info_html=info_html,
            module_path=module_path,
            func_name=func_name,
            param_descriptions=param_descriptions or {},
            param_overrides=param_overrides or {},
            resolved=False,
        )

    return Feature(
        id=feature_id, title=title, desc=desc,
        callable=lambda: None,
        params=[], docs_url=docs_url,
        is_placeholder=True,
        platform_note=platform_note or "office.api 中暂无对应实现。请先安装对应 PyPI 子包（如 pip install python-office[all]）。",
        info_html=info_html,
        module_path=module_path,
        func_name=func_name,
        param_descriptions=param_descriptions or {},
        param_overrides=param_overrides or {},
        resolved=True,
    )


# -------- 类别定义 --------

def _cat(id_: str, title: str, icon: str, order: int) -> Category:
    return Category(id=id_, title=title, icon=icon, order=order)


def build_registry() -> list[Category]:
    """构造全量功能注册表。每次启动 GUI 都重新构造，开销可忽略。"""
    cats: list[Category] = []

    # --- PDF（按官方文档 https://www.python-office.com/modules/pdf/api 的 13 个函数）---
    c = _cat("pdf", "PDF 处理", "📕", 10)
    c.features = [
        _build_feature(
            "pdf2docx", "PDF 转 Word", "把 PDF 文件转为 .docx 文档。",
            "office.api.pdf", "pdf2docx",
            "https://www.python4office.cn/python-office/popdf/1-pdf2docx/",
            param_descriptions={
                "input_file":  "要转换的 PDF 文件完整路径（含 .pdf 后缀）。",
                "output_file": "输出 .docx 文件路径；留空时自动派生为 <输入同目录>/<同名>.docx。",
                "input_path":  "输入 PDF 所在目录（兼容风格：与 output_path 配对使用）。",
                "output_path": "输出 .docx 保存目录（兼容风格：与 input_path 配对使用）。",
            },
        ),
        _build_feature("pdf2imgs", "PDF 转图片", "把 PDF 每页导出为一张图片。",
                       "office.api.pdf", "pdf2imgs",
                       "https://www.python4office.cn/python-office/popdf/2-pdf2imgs/",
                       param_descriptions={
                           "input_file":  "源 PDF 文件。",
                           "output_file": "输出图片路径；merge=True 时是单张长图文件路径（如 ./long.png），merge=False 时是输出目录。",
                           "merge":       "True=所有页拼成一张长图；False=每页一张图。",
                           "pdf_path":    "[已弃用] 请改用 input_file。",
                           "out_dir":     "[已弃用] 请改用 output_file。",
                       }),
        _build_feature("txt2pdf", "文本转 PDF", "把 .txt 文本导出为 PDF。",
                       "office.api.pdf", "txt2pdf",
                       param_descriptions={
                           "input_file":  "要转换的 .txt 文本文件。",
                           "output_file": "生成的 PDF 文件路径。",
                       }),
        _build_feature("split4pdf", "PDF 拆分", "按页码范围拆分 PDF。",
                       "office.api.pdf", "split4pdf",
                       param_descriptions={
                           "input_file": "要拆分的 PDF 文件。",
                           "output_file": "拆分后的输出 PDF 文件路径。",
                           "from_page": "起始页码（1 起，-1 表示首页）。",
                           "to_page": "结束页码（-1 表示末页）。",
                       }),
        _build_feature("merge2pdf", "PDF 合并", "把多个 PDF 合并成一个。",
                       "office.api.pdf", "merge2pdf",
                       param_descriptions={
                           "input_file_list": "要合并的 PDF 文件路径列表，顺序即合并顺序。",
                           "output_file":     "合并后的 PDF 文件路径。",
                           "one_by_one":       "[已弃用] 请改用 input_file_list。",
                           "output":           "[已弃用] 请改用 output_file。",
                       }),
        _build_feature("encrypt4pdf", "PDF 加密", "为 PDF 设置打开密码。",
                       "office.api.pdf", "encrypt4pdf",
                       param_descriptions={
                           "password":   "PDF 打开密码，建议 12 位以上。",
                           "input_file": "要加密的 PDF 文件。",
                           "output_file": "加密后的输出 PDF 路径。",
                           "input_path": "[已弃用] 请改用 input_file。",
                           "output_path": "[已弃用] 请改用 output_file。",
                       }),
        _build_feature("decrypt4pdf", "PDF 解密", "用已知密码移除 PDF 保护。",
                       "office.api.pdf", "decrypt4pdf",
                       param_descriptions={
                           "password":   "已知的 PDF 密码。",
                           "input_file": "要解密的加密 PDF 文件。",
                           "output_file": "解密后的输出 PDF 路径。",
                           "input_path": "[已弃用] 请改用 input_file。",
                           "output_path": "[已弃用] 请改用 output_file。",
                       }),
        _build_feature("add_text_watermark", "PDF 加文字水印", "在 PDF 上叠加文字水印。",
                       "office.api.pdf", "add_text_watermark",
                       param_descriptions={
                           "input_file":  "源 PDF 文件。",
                           "text":        "水印文字内容。",
                           "output_file": "加水印后的输出 PDF 路径。",
                           "point":       "水印位置坐标 (x, y)；空则使用默认位置。",
                           "fontname":    "字体名称，默认 Helvetica。",
                           "fontsize":    "字号，默认 20。",
                           "color":       "RGB 颜色三元组，每个分量 0~1。默认 (0, 0, 1) 蓝色。",
                       }),
        _build_feature("add_img_water", "PDF 加图片水印", "用图片给 PDF 加水印。",
                       "office.api.pdf", "add_img_water",
                       "https://www.python-office.com/modules/pdf/api#add_img_water",
                       param_descriptions={
                           "input_file":  "源 PDF 文件。",
                           "mark_file":   "作为水印的图片文件（建议 PNG / JPG）。",
                           "output_file": "加水印后的输出 PDF 路径。",
                       }),
        _build_feature("add_mark", "PDF 加水印（旧版）", "旧版兼容入口，推荐 add_watermark_by_parameters。",
                       "office.api.pdf", "add_mark",
                       param_overrides={
                           "mark_str":  {"kind": "str"},
                       },
                       param_descriptions={
                           "input_file":      "源 PDF 文件。",
                           "mark_str":        "水印文字内容。",
                           "output_path":     "输出目录，文件名前缀。",
                           "output_file":     "输出文件名。",
                           "pdf_file":        "[已弃用] 请改用 input_file。",
                           "output_file_name": "[已弃用] 请改用 output_file。",
                       }),
        _build_feature("add_watermark_by_parameters", "PDF 加水印（参数化）", "参数化水印接口（推荐）。",
                       "office.api.pdf", "add_watermark_by_parameters",
                       "https://www.python-office.com/modules/pdf/api#add_watermark_by_parameters",
                       param_overrides={
                           "mark_str":  {"kind": "str"},
                       },
                       param_descriptions={
                           "input_file":      "源 PDF 文件。",
                           "mark_str":        "水印文字内容。",
                           "output_path":     "输出目录。",
                           "output_file":     "输出文件名。",
                           "pdf_file":        "[已弃用] 请改用 input_file。",
                           "output_file_name": "[已弃用] 请改用 output_file。",
                       }),
        _build_feature("del4pdf", "删除 PDF 页", "按页码列表删除 PDF 页面。",
                       "office.api.pdf", "del4pdf",
                       param_descriptions={
                           "input_file":  "源 PDF 文件。",
                           "output_file": "删除页后的输出 PDF 路径。",
                           "page_nums":   "要删除的页码列表（1 起），多个用逗号或分号分隔，如 1,3,5。",
                       }),
        _build_feature("pdf_add_watermark_interactive", "交互式水印", "命令行交互式水印（GUI 中可忽略此入口）。",
                       "office.api.pdf", "add_watermark",
                       "https://www.python-office.com/modules/pdf/api#add_watermark"),
    ]
    cats.append(c)

    # --- Excel（按官方文档 https://www.python-office.com/modules/excel/api 的 7 个函数）---
    c = _cat("excel", "Excel 处理", "📗", 20)
    c.features = [
        _build_feature("fake2excel", "生成模拟 Excel", "用 Faker 库生成测试数据。",
                       "office.api.excel", "fake2excel",
                       param_overrides={
                           "path": {
                               "kind": "save",
                               "file_filter": "Excel files (*.xlsx)",
                           },
                       },
                       param_descriptions={
                           "columns":  "列名列表。可用字段：name, phone, email, address, company, job, country, city, postcode, ssn, credit_card_number, user_agent, text, sentence。多个用逗号分隔。",
                           "rows":     "要生成的数据行数。",
                           "path":     "输出 Excel 文件路径（另存为对话框，默认 .xlsx）。",
                           "language": "数据语言：'zh_CN' 中文 / 'english' 英文。",
                       }),
        _build_feature("merge2excel", "合并多个 Excel", "把目录下多个 Excel 合并成一个文件的不同 sheet。",
                       "office.api.excel", "merge2excel",
                       param_descriptions={
                           "dir_path":   "包含多个 Excel 文件的目录路径。",
                           "output_file": "合并后的 Excel 文件路径。",
                       }),
        _build_feature("sheet2excel", "按 sheet 拆分", "把一个 Excel 的多个 sheet 拆成多个文件。",
                       "office.api.excel", "sheet2excel",
                       param_descriptions={
                           "file_path":   "要拆分的 Excel 文件路径。",
                           "output_path": "拆分后文件的输出目录。",
                       }),
        _build_feature("merge2sheet", "多 Excel 多 sheet 合并", "跨文件、跨 sheet 自动合并。",
                       "office.api.excel", "merge2sheet",
                       param_descriptions={
                           "dir_path":          "包含多个 Excel 文件的目录路径。",
                           "output_sheet_name": "合并后的 sheet 名称。",
                           "output_excel_name": "合并后的 Excel 文件名（不含 .xlsx 后缀）。",
                       }),
        _build_feature("find_excel_data", "搜索 Excel 内容", "在指定目录下搜索单元格内容。",
                       "office.api.excel", "find_excel_data",
                       param_descriptions={
                           "search_key": "要搜索的关键词。",
                           "target_dir": "搜索的目录路径。",
                       }),
        _build_feature("split_excel_by_column", "按列拆分 Excel", "按指定列的不同值拆分工作表。",
                       "office.api.excel", "split_excel_by_column",
                       param_descriptions={
                           "filepath":       "要拆分的 Excel 文件路径。",
                           "column":         "按哪一列的内容进行拆分（1 起）。",
                           "worksheet_name": "要处理的工作表名称，留空则用第一个工作表。",
                       }),
        _build_feature("excel2pdf", "Excel 转 PDF", "把指定 sheet 导出为 PDF。",
                       "office.api.excel", "excel2pdf",
                       param_overrides={
                           # pdf_path 实际是输出文件，但名字以 _path 结尾会被推断为 dir
                           # 这里显式覆盖为 save 模式（另存为对话框）
                           "pdf_path": {
                               "kind": "save",
                               "file_filter": "PDF files (*.pdf)",
                           },
                       },
                       param_descriptions={
                           "excel_path": "源 Excel 文件路径。",
                           "pdf_path":   "输出 PDF 文件路径（另存为对话框）。",
                           "sheet_id":   "工作表索引（0 起，0 表示第一个 sheet）。",
                       }),
        _build_feature("excel2markdown", "Excel 转 Markdown", "把 Excel 表格转 Markdown 文档（HTML 表格，支持 colspan/rowspan，保留合并单元格原貌）。",
                       "office.api.markdown", "excel2markdown",
                       param_overrides={
                           "input_file": {
                               "kind": "file",
                               "file_filter": "Excel files (*.xlsx *.xls)",
                           },
                           "output_file": {
                               "kind": "save",
                               "file_filter": "Markdown files (*.md)",
                           },
                       },
                       param_descriptions={
                           "input_file":  "要转换的 Excel 文件（.xlsx / .xls）。",
                           "output_file": "输出的 Markdown 文件（另存为对话框，默认 ./excel2markdown.md）。",
                           "sheet_name":  "要转换的工作表名，留空则转换所有工作表。",
                       }),
    ]
    cats.append(c)

    # --- Word (官方文档 https://www.python-office.com/modules/word/api 的 5 个函数)---
    c = _cat("word", "Word 处理", "📘", 30)
    c.features = [
        _build_feature("docx2pdf", "Word 转 PDF", "Word 转 PDF，支持单个文件或整个文件夹批量。",
                       "office.api.word", "docx2pdf",
                       platform_note="依赖 Microsoft Word / WPS / LibreOffice，桌面环境可用",
                       param_overrides={
                           # path 既能传文件也能传目录，kind 留 file 让用户选文件；如选目录会报错但更直观
                           "path": {"file_filter": "Word files (*.docx *.doc)"},
                       },
                       param_descriptions={
                           "path":        "Word 文件路径，或包含多个 Word 文件的目录路径。传目录时批量转换。",
                           "output_path": "PDF 输出目录；不存在会自动创建。留空则输出到 path 所在目录。",
                       }),
        _build_feature("merge4docx", "合并 Word", "把多个 .docx 合并成一个文件。",
                       "office.api.word", "merge4docx",
                       platform_note="依赖 Microsoft Word / WPS / LibreOffice",
                       param_descriptions={
                           "input_path":    "包含多个 .docx 的目录路径。",
                           "output_path":   "合并后文件保存目录。",
                           "new_word_name": "合并后新文件的名字（不含 .docx 后缀）。",
                       }),
        _build_feature("doc2docx", "doc 转 docx", "把旧版 .doc 转为 .docx。",
                       "office.api.word", "doc2docx",
                       platform_note="依赖 Microsoft Word / WPS / LibreOffice",
                       param_overrides={
                           "input_path": {
                               "kind": "file",
                               "file_filter": "Word 97-2003 (*.doc)",
                           },
                       },
                       param_descriptions={
                           "input_path":  "要转换的 .doc 文件路径。",
                           "output_path": "生成的 .docx 保存目录（默认 ./）。",
                           "output_name": "输出文件名（不含后缀），留空则与原文件同名。",
                       }),
        _build_feature("docx2doc", "docx 转 doc", "把 .docx 转回旧版 .doc。",
                       "office.api.word", "docx2doc",
                       platform_note="依赖 Microsoft Word / WPS / LibreOffice",
                       param_overrides={
                           "input_path": {
                               "kind": "file",
                               "file_filter": "Word 文档 (*.docx)",
                           },
                       },
                       param_descriptions={
                           "input_path":  "要转换的 .docx 文件路径。",
                           "output_path": "生成的 .doc 保存目录（默认 ./）。",
                           "output_name": "输出文件名（不含后缀），留空则与原文件同名。",
                       }),
        _build_feature("docx4imgs", "Word 提取图片", "从 Word 文档中提取所有图片。",
                       "office.api.word", "docx4imgs",
                       platform_note="依赖 python-docx，不依赖 Microsoft Word",
                       param_overrides={
                           "word_path": {
                               "kind": "file",
                               "file_filter": "Word 文档 (*.docx)",
                           },
                           "img_path": {
                               "kind": "dir",
                           },
                       },
                       param_descriptions={
                           "word_path": "要提取图片的 .docx 文件路径。",
                           "img_path":  "图片输出根目录；会自动按 Word 文件名生成子目录。",
                       }),
    ]
    cats.append(c)

    # --- PPT（按官方文档 https://www.python-office.com/modules/ppt/api 的 3 个函数）---
    c = _cat("ppt", "PPT 处理", "📙", 40)
    c.features = [
        _build_feature("ppt2pdf", "PPT 转 PDF", "把 .pptx 转成 PDF。",
                       "office.api.ppt", "ppt2pdf",
                       platform_note="依赖 Microsoft PowerPoint / WPS / LibreOffice",
                       param_overrides={
                           "path": {
                               "kind": "file",
                               "file_filter": "PowerPoint files (*.pptx *.ppt)",
                           },
                       },
                       param_descriptions={
                           "path":        "输入的 .pptx / .ppt 文件路径。",
                           "output_path": "PDF 保存目录。",
                       }),
        _build_feature("ppt2img", "PPT 转图片", "把幻灯片导出为图片，可合并为长图。",
                       "office.api.ppt", "ppt2img",
                       platform_note="依赖 Microsoft PowerPoint / WPS / LibreOffice",
                       param_overrides={
                           "input_path": {
                               "kind": "file",
                               "label": "输入文件",
                               "file_filter": "PowerPoint files (*.pptx *.ppt)",
                           },
                       },
                       param_descriptions={
                           "input_path":  "输入的 .pptx 文件路径；也可传目录，批量转换目录下所有 PPT。",
                           "output_path": "图片输出目录（merge=False）或单张长图文件路径（merge=True）。",
                           "merge":       "True=把所有幻灯片拼成一张长图，False=每页一张图。",
                       }),
        _build_feature("merge4ppt", "合并 PPT", "把多个 .pptx 合并成一个文件。",
                       "office.api.ppt", "merge4ppt",
                       platform_note="依赖 Microsoft PowerPoint / WPS / LibreOffice",
                       param_descriptions={
                           "input_path":  "包含多个 .pptx / .ppt 的目录。",
                           "output_path": "合并后文件保存目录。",
                           "output_name": "合并后文件名（含 .pptx 后缀，默认 merge4ppt.pptx）。",
                       }),
    ]
    cats.append(c)

    # --- 图片（按官方文档 https://www.python-office.com/modules/image/api 的 9 个函数）---
    c = _cat("image", "图片处理", "🖼️", 50)
    c.features = [
        _build_feature("compress_image", "压缩图片", "按质量参数压缩图片，减小体积。",
                       "office.api.image", "compress_image",
                       param_overrides={
                           "input_file":  {"file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)"},
                           "output_file": {"kind": "save", "file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)"},
                       },
                       param_descriptions={
                           "input_file":  "要压缩的输入图片文件。",
                           "output_file": "压缩后的图片保存路径（另存为对话框）。",
                           "quality":     "压缩质量 0~95，越大越清晰、文件越大；推荐 70~85。",
                       }),
        _build_feature("image2gif", "图片转 GIF", "将图片转为 GIF（交互式入口，GUI 中可忽略）。",
                       "office.api.image", "image2gif",
                       is_placeholder=True,
                       platform_note="CLI 交互式入口"),
        _build_feature("add_watermark", "图片加水印", "为图片添加文字水印。",
                       "office.api.image", "add_watermark",
                       param_overrides={
                           "mark": {"kind": "str"},
                           "file": {"file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)"},
                       },
                       param_descriptions={
                           "file":        "要加水印的图片文件。",
                           "mark":        "水印文字内容（如 @python-office）。",
                           "output_path": "输出目录。",
                           "color":       "水印颜色，十六进制如 #eaeaea。",
                           "size":        "水印字号大小。",
                           "opacity":     "不透明度，0.01~1 之间。",
                           "space":       "水印之间的间距（像素）。",
                           "angle":       "旋转角度（如 30 表示倾斜 30 度）。",
                       }),
        _build_feature("del_watermark", "图片去水印", "尝试移除图片中的水印。",
                       "office.api.image", "del_watermark",
                       param_overrides={
                           "input_image":  {"file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)"},
                           "output_image": {"kind": "save", "file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)"},
                       },
                       param_descriptions={
                           "input_image":  "含水印的图片文件。",
                           "output_image": "去水印后保存的文件（另存为对话框）。",
                       }),
        _build_feature("img2Cartoon", "图片转漫画", "调用百度 AI 把图片转为卡通风格。",
                       "office.api.image", "img2Cartoon",
                       param_overrides={
                           "path": {"file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)"},
                       },
                       param_descriptions={
                           "path":          "输入图片文件。",
                           "client_api":    "百度 AI 应用的 API Key（留空使用内置 Key）。",
                           "client_secret": "百度 AI 应用的 Secret Key（留空使用内置 Key）。",
                       }),
        _build_feature("down4img", "下载网络图片", "通过 URL 下载图片到本地。",
                       "office.api.image", "down4img",
                       param_descriptions={
                           "url":         "图片的网络地址（http/https）。",
                           "output_path": "保存目录（默认当前目录）。",
                           "output_name": "保存的文件名前缀（不含后缀）。",
                           "type":        "图片格式，如 jpg / png。",
                       }),
        _build_feature("txt2wordcloud", "生成词云", "从文本生成词云图片。",
                       "office.api.image", "txt2wordcloud",
                       param_overrides={
                           "result_file": {
                               "kind": "save",
                               "file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)",
                           },
                           "filename": {"file_filter": "Text files (*.txt *.md)"},
                       },
                       param_descriptions={
                           "filename":    "输入的 .txt 文本文件路径。",
                           "color":       "词云背景色，如 white / black / 十六进制。",
                           "result_file": "输出的词云图片（另存为对话框）。",
                       }),
        _build_feature("pencil4img", "铅笔画效果", "把图片转成铅笔素描风格。",
                       "office.api.image", "pencil4img",
                       param_overrides={
                           "input_img": {"file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)"},
                       },
                       param_descriptions={
                           "input_img":   "输入图片文件。",
                           "output_path": "输出目录。",
                           "output_name": "输出文件名（含后缀，默认 pencil4img.jpg）。",
                       }),
        _build_feature("decode_qrcode", "解码二维码", "识别图片中的二维码内容。",
                       "office.api.image", "decode_qrcode",
                       param_overrides={
                           "qrcode_path": {
                               "kind": "file",
                               "file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)",
                           },
                       },
                       param_descriptions={
                           "qrcode_path": "二维码图片文件路径。",
                       }),
    ]
    cats.append(c)

    # --- 文件（按官方文档 https://www.python-office.com/modules/file/api 的 9 个函数）---
    c = _cat("file", "文件管理", "📁", 60)
    c.features = [
        _build_feature("replace4filename", "批量重命名", "按关键字批量替换文件名 / 文件夹名。",
                       "office.api.file", "replace4filename",
                       param_overrides={
                           "path":        {"kind": "dir"},
                           "file_rename": {"kind": "bool"},
                       },
                       param_descriptions={
                           "path":            "要批量重命名的根目录（该目录本身不会被改）。",
                           "del_content":     "文件名中要删除 / 替换的内容。",
                           "replace_content": "替换成的新内容，留空则等于删除。",
                           "dir_rename":      "是否同时修改子文件夹名。",
                           "file_rename":     "是否同时修改文件名。",
                           "suffix":          "只处理特定后缀的文件，如 .txt；留空处理所有。",
                       }),
        _build_feature("file_name_insert_content", "文件名中间插入", "在文件名中间插入字符串。",
                       "office.api.file", "file_name_insert_content",
                       param_overrides={
                           "insert_position": {"kind": "int"},
                       },
                       param_descriptions={
                           "file_path":       "文件路径。",
                           "insert_position": "插入位置（1 起），如 3 表示在第 3 个字符后插入。",
                           "insert_content":  "要插入的字符串。",
                       }),
        _build_feature("file_name_add_prefix", "文件加前缀", "批量给文件名前加前缀。",
                       "office.api.file", "file_name_add_prefix",
                       param_descriptions={
                           "file_path":      "文件路径。",
                           "prefix_content": "要添加的前缀字符串。",
                       }),
        _build_feature("file_name_add_postfix", "文件加后缀", "批量给文件名后加后缀。",
                       "office.api.file", "file_name_add_postfix",
                       param_descriptions={
                           "file_path":       "文件路径。",
                           "postfix_content": "要添加的后缀字符串。",
                       }),
        _build_feature("output_file_list_to_excel", "文件名导出 Excel", "把目录下的文件名清单写入 Excel。",
                       "office.api.file", "output_file_list_to_excel",
                       param_descriptions={
                           "dir_path": "要导出的目录。",
                       }),
        _build_feature("search_specify_type_file", "按类型搜索文件", "按扩展名搜索文件。",
                       "office.api.file", "search_specify_type_file",
                       param_overrides={
                           "file_path": {"kind": "dir"},
                           "file_type": {"kind": "str"},
                       },
                       param_descriptions={
                           "file_path": "搜索的目录。",
                           "file_type": "要搜索的扩展名，如 .pdf / .docx（必须带点）。",
                       }),
        _build_feature("get_files", "获取文件列表", "返回目录下符合条件的文件路径列表。",
                       "office.api.file", "get_files",
                       param_overrides={
                           "path": {"kind": "dir"},
                       },
                       param_descriptions={
                           "path":   "搜索的目录。",
                           "name":   "文件名关键字（留空匹配所有）。",
                           "suffix": "文件后缀，如 .pdf（留空匹配所有）。",
                           "sub":    "True=递归搜索子目录。",
                           "level":  "递归深度，0 表示无限。",
                       }),
        _build_feature("add_line_by_type", "按类型插入行", "向指定后缀的文件批量插入行。",
                       "office.api.file", "add_line_by_type",
                       param_overrides={
                           "add_line_dict": {"kind": "text"},
                           "file_type":     {"kind": "str"},
                       },
                       param_descriptions={
                           "add_line_dict": "要插入的内容，格式如 {'import os': ['a.py', 'b.py']}。多行文本框输入 JSON。",
                           "file_path":     "目标目录。",
                           "file_type":     "要处理的文件后缀（如 .py）。",
                           "output_path":   "新文件输出目录。",
                       }),
        _build_feature("group_by_name", "按名称分组", "把目录下的文件按名称分组整理到子目录。",
                       "office.api.file", "group_by_name",
                       param_overrides={
                           "path":         {"kind": "dir"},
                           "del_old_file": {"kind": "bool"},
                       },
                       param_descriptions={
                           "path":         "源目录。",
                           "output_path":  "分组后的输出目录，留空则在 path 同级创建 group_by_name 子目录。",
                           "del_old_file": "是否删除原文件。",
                       }),
    ]
    cats.append(c)

    # --- 视频（按官方文档 https://www.python-office.com/modules/video/api 的 4 个函数）---
    c = _cat("video", "视频处理", "🎬", 70)
    c.features = [
        _build_feature("video2mp3", "视频提取音频", "从视频中提取音频为 MP3。",
                       "office.api.video", "video2mp3",
                       param_overrides={
                           "path": {
                               "kind": "file",
                               "file_filter": "Video files (*.mp4 *.avi *.mov *.mkv *.flv)",
                           },
                       },
                       param_descriptions={
                           "path":        "输入视频文件（mp4 / avi / mov / mkv 等）。",
                           "mp3_name":    "MP3 文件名（不含后缀），留空则用原视频文件名。",
                           "output_path": "输出目录。",
                       }),
        _build_feature("audio2txt", "音频转文字", "调用腾讯云语音识别把音频转为文字。",
                       "office.api.video", "audio2txt",
                       platform_note="需要腾讯云 appid / SecretId / SecretKey；本地音频 ≤ 5MB",
                       param_overrides={
                           "audio_path": {"file_filter": "Audio files (*.mp3 *.wav *.m4a *.flac)"},
                       },
                       param_descriptions={
                           "audio_path": "输入的音频文件。",
                           "appid":      "腾讯云语音识别应用的 appid。",
                           "secret_id":  "腾讯云 API SecretId。",
                           "secret_key": "腾讯云 API SecretKey。",
                       }),
        _build_feature("mark2video", "视频加文字水印", "在视频上叠加滚动文字水印。",
                       "office.api.video", "mark2video",
                       param_overrides={
                           "mark_str": {"kind": "str"},
                       },
                       param_descriptions={
                           "video_path": "输入视频文件。",
                           "output_path": "输出目录。",
                           "output_name": "输出文件名（**记得带 .mp4 后缀**，默认 mark2video.mp4）。",
                           "mark_str":   "水印文字内容。",
                           "font_size":  "水印字号（默认 28）。",
                           "font_type":  "字体名称或字体文件路径（默认 Arial）。",
                           "font_color": "字体颜色（默认 white）。",
                       }),
        _build_feature("txt2mp3", "文本转语音", "调用本地 TTS 引擎把文本合成 MP3。",
                       "office.api.video", "txt2mp3",
                       param_overrides={
                           "mp3": {
                               "kind": "save",
                               "file_filter": "Audio files (*.mp3 *.wav *.m4a *.flac)",
                           },
                           "file": {
                               "file_filter": "Text files (*.txt *.md)",
                           },
                       },
                       param_descriptions={
                           "content": "要朗读的文本内容（默认 '程序员晚枫'）。",
                           "file":    "可选：从指定文本文件读取（优先级最高）。",
                           "mp3":     "输出的 MP3 文件（另存为对话框）。",
                           "speak":   "True=边合成边朗读，False=只生成文件。",
                       }),
    ]
    cats.append(c)

    # --- 邮件（按官方文档 https://www.python-office.com/modules/email/api 的 2 个函数）---
    c = _cat("email", "邮件收发", "📧", 80)
    c.features = [
        _build_feature("send_email", "发送邮件", "通过 SMTP 发送邮件，支持附件 / 抄送。",
                       "office.api.email", "send_email",
                       param_overrides={
                           "key":  {"label": "邮箱授权码"},
                           "host": {
                               "kind": "choice",
                               "choices": ["smtp.qq.com", "smtp.163.com", "smtp.gmail.com"],
                           },
                       },
                       param_descriptions={
                           "key":          "邮箱授权码（不是登录密码）。QQ 邮箱在 设置→账户→POP3/IMAP 服务 生成。",
                           "msg_from":     "发件人邮箱地址。",
                           "msg_to":       "收件人邮箱地址。",
                           "msg_cc":       "抄送地址（多个用英文逗号分隔），留空则不抄送。",
                           "attach_files": "附件文件路径列表（用分号 ; 分隔多个路径），留空则无附件。",
                           "msg_subject":  "邮件主题。",
                           "content":      "邮件正文。",
                           "host":         "SMTP 服务器地址：QQ 选 smtp.qq.com / 163 选 smtp.163.com / Gmail 选 smtp.gmail.com。",
                           "port":         "SMTP 端口：QQ/163 用 465，Gmail 用 587。",
                       }),
        _build_feature("receive_email", "接收邮件", "按状态 / 主题过滤接收邮件并保存。",
                       "office.api.email", "receive_email",
                       param_overrides={
                           "key":  {"label": "邮箱授权码"},
                           "host": {
                               "kind": "choice",
                               "choices": ["smtp.qq.com", "smtp.163.com", "smtp.gmail.com"],
                           },
                           "status": {
                               "kind": "choice",
                               "choices": ["UNSEEN", "SEEN", "ALL"],
                           },
                       },
                       param_descriptions={
                           "key":          "邮箱授权码（不是登录密码）。",
                           "msg_from":     "发件人邮箱地址。",
                           "output_path":  "邮件保存目录。",
                           "status":      "邮件状态过滤：UNSEEN=未读 / SEEN=已读 / ALL=全部。",
                           "msg_subject": "邮件主题过滤（留空匹配所有）。",
                           "host":        "邮件服务器地址。",
                           "port":        "邮件服务器端口。",
                       }),
    ]
    cats.append(c)

    # --- Markdown 模块（excel2markdown 已移到 Excel 处理分类下）---

    # --- 工具（按官方文档 https://www.python-office.com/modules/tools/api 的 10 个函数）---
    c = _cat("tools", "实用工具", "🛠️", 110)
    c.features = [
        _build_feature("qrcodetools", "生成二维码", "把 URL 转为二维码图片。",
                       "office.api.tools", "qrcodetools",
                       param_overrides={
                           "output": {
                               "kind": "save",
                               "file_filter": "Images (*.png *.jpg *.jpeg *.bmp *.gif)",
                           },
                       },
                       param_descriptions={
                           "url":    "要编码成二维码的网址或文本。",
                           "output": "二维码图片保存路径（另存为对话框，默认 ./qrcode_img.png）。",
                       }),
        _build_feature("passwordtools", "随机密码", "生成指定长度的随机密码。",
                       "office.api.tools", "passwordtools",
                       param_descriptions={
                           "len": "密码长度（默认 8）。",
                       }),
        _build_feature("weather", "天气查询", "查询指定城市的天气。CLI 交互式（会按提示选择城市/日期），建议在终端使用。",
                       "office.api.tools", "weather",
                       cli_only=True,
                       cli_command=(
                           "python\n"
                           ">>> from office.api.tools import weather\n"
                           ">>> weather()\n"
                           "\n"
                           "# 或者直接命令行一行调用（按提示交互）：\n"
                           "python -c \"from office.api.tools import weather; weather()\"\n"
                       ),
                        param_descriptions={}),
        _build_feature("lottery8ticket", "彩票号码", "随机生成 8 位彩票号码。CLI 交互式（可重复生成直至满意），建议在终端使用。",
                       "office.api.tools", "lottery8ticket",
                       cli_only=True,
                       cli_command=(
                           "python\n"
                           ">>> from office.api.tools import lottery8ticket\n"
                           ">>> lottery8ticket()\n"
                           "\n"
                           "# 直接命令行调用：\n"
                           "python -c \"from office.api.tools import lottery8ticket; lottery8ticket()\"\n"
                       ),
                        param_descriptions={}),
        _build_feature("pwd4wifi", "WiFi 密码字典（生成器）",
                       "按指定字符集 × 长度枚举所有可能密码，保存为字典文件。",
                       "office.api.tools", "pwd4wifi",
                       cli_only=True,
                       cli_command=(
                           "# ⚠️ 当前 office.api.tools.pwd4wifi 是空函数（wftools 库未实现），\n"
                           "#    所以 GUI 点'运行'什么也不会发生。请直接用下面的代码生成字典：\n"
                           "\n"
                           "python\n"
                           ">>> import itertools\n"
                           ">>> # 字符集：手机号段\n"
                           ">>> charset = '0123456789'\n"
                           ">>> length = 8\n"
                           ">>> # 生成所有 8 位纯数字组合（10^8 = 1 亿条，建议限制长度）\n"
                           ">>> with open('wifi_dict.txt', 'w') as f:\n"
                           ">>>     for combo in itertools.product(charset, repeat=length):\n"
                           ">>>         f.write(''.join(combo) + '\\n')\n"
                           "\n"
                           "# 一行命令（生成 6 位纯数字字典，1MB 左右）：\n"
                           "python -c \"import itertools; open('wifi_dict.txt','w').writelines(\n"
                           "    ''.join(p)+'\\n' for p in itertools.product('0123456789', repeat=6))\"\n"
                           "\n"
                           "# ⚠️ 真正的 WiFi 破解需要：\n"
                           "#   1. pywifi 扫描附近 WiFi 的 SSID + 信号强度\n"
                           "#   2. 字典逐条尝试连接（一次握手需 1-5 秒）\n"
                           "#   3. 通常需要管理员权限 + 真实网卡\n"
                           "# python-office 暂未集成这一套；可参考 pywifi + 字典爆破脚本\n"
                       ),
                       param_overrides={
                           "len_pwd":  {"kind": "int"},
                           "pwd_list": {"kind": "str"},
                       },
                       param_descriptions={
                           "len_pwd":  "密码长度（默认 8）。",
                           "pwd_list": "可选：自定义字符集（用文本框输入），如 '0123456789' 或 'abc123'。",
                       }),
        _build_feature("net_speed_test", "网速测试", "测试当前网络的上传/下载速度（speedtest.net）。CLI 交互式（会持续输出进度），建议在终端使用。",
                       "office.api.tools", "net_speed_test",
                       cli_only=True,
                       cli_command=(
                           "python\n"
                           ">>> from office.api.tools import net_speed_test\n"
                           ">>> net_speed_test()\n"
                           "\n"
                            "# 直接命令行调用：\n"
                            "python -c \"from office.api.tools import net_speed_test; net_speed_test()\"\n"
                        ),
                        param_descriptions={}),
        _build_feature("VatInvoiceOCR2Excel", "增值税发票识别 → Excel",
                       "调用百度智能云 OCR 识别发票图片 / PDF 中的关键字段，导出为 Excel 文件。支持单张/批量。",
                       "office.api.ocr", "VatInvoiceOCR2Excel",
                       cli_only=True,
                       cli_command=(
                           "# =================== 增值税发票识别 使用说明 ===================\n"
                           "#\n"
                           "# 📌 原理：调用百度智能云的「增值税发票识别」API（OCR 引擎），\n"
                           "#    把图片/PDF 中的发票号、金额、税额、销售方等字段识别后写入 Excel。\n"
                           "#\n"
                           "# ─────────── 1. 申请百度智能云 OCR 凭据（必须）───────────\n"
                           "#   a) 注册账号：https://ai.baidu.com/\n"
                           "#   b) 顶部菜单「文字识别 OCR」→「增值税发票识别」→ 点击「立即使用」\n"
                           "#   c) 创建应用：\n"
                           "#      - 应用名称：python-office（随便起）\n"
                           "#      - 应用类型：选择「纯应用」或「服务端」\n"
                           "#      - 勾选「增值税发票识别」服务\n"
                           "#   d) 创建完成后，在「应用列表」里点开，看「API Key」和「Secret Key」\n"
                           "#      复制下来 → 填入下方命令的 id / key 参数\n"
                           "#\n"
                           "# ─────────── 2. 安装依赖（首次）───────────\n"
                           "pip install python-office[ocr] openpyxl\n"
                           "\n"
                           "# ─────────── 3. 准备发票图片/PDF ───────────\n"
                           "#   - 单张：d:/invoices/01.jpg\n"
                           "#   - 批量：把所有发票放到 d:/invoices/ 目录（支持 jpg/png/pdf）\n"
                           "\n"
                           "# ─────────── 4. 命令行调用 ───────────\n"
                           "# 单张：\n"
                           "python -c \"\n"
                           "from office.api.ocr import VatInvoiceOCR2Excel\n"
                           "VatInvoiceOCR2Excel(\n"
                           "    input_path='d:/invoices/01.jpg',\n"
                           "    output_path='d:/result',\n"
                           "    output_excel='invoices.xlsx',\n"
                           "    id='你的 API Key',\n"
                           "    key='你的 Secret Key',\n"
                           "    file_name=True,   # 用文件名当 Sheet 名（多发票时建议开启）\n"
                           "    trans=False,      # 是否同时翻译为英文（按需）\n"
                           ")\"\n"
                           "\n"
                           "# 批量（传入目录）：\n"
                           "python -c \"\n"
                           "from office.api.ocr import VatInvoiceOCR2Excel\n"
                           "VatInvoiceOCR2Excel(\n"
                           "    input_path='d:/invoices/',\n"
                           "    output_path='d:/result',\n"
                           "    id='你的 API Key',\n"
                           "    key='你的 Secret Key',\n"
                           "    file_name=True,\n"
                           ")\"\n"
                           "\n"
                           "# ─────────── 5. 输出 ───────────\n"
                           "#   生成 d:/result/invoices.xlsx，Sheet 名 = 文件名\n"
                           "#   每行一张发票的关键字段（发票号、购买方、销售方、金额、税额等）\n"
                           "\n"
                           "# ─────────── 6. 常见问题 ───────────\n"
                           "#   Q: 报错「access_token invalid」？\n"
                           "#   A: id / key 填错了，或应用未勾选「增值税发票识别」服务。\n"
                           "#\n"
                           "#   Q: 报错「image format error」？\n"
                           "#   A: 图片损坏 / 格式不支持 → 重新导出 jpg/png；PDF 用 pdf 转图工具预处理。\n"
                           "\n"
                           "#   Q: 每天免费额度？\n"
                           "#   A: 百度 OCR 增值税发票识别有赠送免费额度（几百~几千次/月），够个人用。\n"
                       ),
                       param_overrides={
                           "img_url":    {"kind": "str"},
                           "id":         {"label": "百度 API Key ID"},
                           "key":        {"label": "百度 Secret Key"},
                           "file_name":  {"kind": "bool"},
                           "trans":      {"kind": "bool"},
                       },
                       param_descriptions={
                           "input_path":  "发票图片 / PDF 的路径，或包含多张发票的目录。",
                           "output_path": "输出 Excel 的保存目录。",
                           "output_excel": "输出 Excel 文件名（默认 VatInvoiceOCR2Excel.xlsx）。",
                           "img_url":     "可选：在线发票图片 URL（与 input_path 二选一）。",
                           "id":          "百度智能云 OCR 应用的 Access Key ID（在百度智能云控制台创建「文字识别 OCR」应用后获取）。",
                           "key":         "百度智能云 OCR 应用的 Secret Key。",
                           "file_name":   "True=用图片文件名作为 Sheet 名（多张发票时建议开启）。",
                           "trans":       "True=同时把识别结果翻译为英文。",
                       }),
        _build_feature("t0", "T+0 交易成本计算", "计算股票 T+0 交易费率与净收益。",
                       "office.api.finance", "t0",
                       param_descriptions={
                           "buy_price":  "买入价格（元 / 股）。",
                           "sale_price": "卖出价格（元 / 股）。",
                           "shares":     "交易股数。",
                           "w_rate":     "佣金费率（默认 2.5/10000 = 万 2.5 = 0.025%）。",
                           "min_rate":   "单笔最低手续费（元，默认 5；交易额 ≤ 20000 时按此收）。",
                           "stamp_tax":  "印花税率（默认 1/1000 = 千 1 = 0.1%，卖出时扣）。",
                       }),
        _build_feature("course", "项目信息", "显示 python-office 项目信息和资源链接。",
                       "office.api.tools", "course",
                       info_html=(
                           "<h2 style='margin-top:0;color:#06162D;'>📦 python-office</h2>"
                           "<p style='color:#294661;'>One-line Python automation for office & daily work.</p>"
                           "<hr>"
                           "<h3 style='color:#06162D;'>📚 学习资源</h3>"
                           "<ul>"
                           "<li><a href='https://www.python-office.com/course/50-python-office.html'>"
                           "给小白的【50 讲 Python 自动化办公】</a></li>"
                           "<li><a href='https://www.python-office.com'>"
                           "官方文档：python-office.com</a></li>"
                           "</ul>"
                           "<h3 style='color:#06162D;'>💬 社区交流</h3>"
                           "<ul>"
                           "<li><a href='https://www.python4office.cn/wechat-group/'>"
                           "项目交流群（微信群）</a></li>"
                           "<li><a href='https://github.com/CoderWanFeng/python-office'>"
                           "GitHub 源码仓库</a></li>"
                           "<li><a href='https://github.com/CoderWanFeng/python-office/issues'>"
                           "Bug 反馈 / 功能建议</a></li>"
                           "</ul>"
                           "<h3 style='color:#06162D;'>🎯 子模块速查</h3>"
                           "<table style='border-collapse:collapse;width:100%;'>"
                           "<tr style='background:#EAF7FF;'>"
                           "<th style='padding:6px 12px;text-align:left;'>分类</th>"
                           "<th style='padding:6px 12px;text-align:left;'>子包</th>"
                           "<th style='padding:6px 12px;text-align:left;'>功能</th>"
                           "</tr>"
                           "<tr><td style='padding:4px 12px;'>📕 PDF</td>"
                           "<td style='padding:4px 12px;'>popdf</td>"
                           "<td style='padding:4px 12px;'>PDF 转 Word / Excel / 图片、合并、拆分、加密</td></tr>"
                           "<tr style='background:#F3FBFF;'><td style='padding:4px 12px;'>📊 Excel</td>"
                           "<td style='padding:4px 12px;'>poexcel</td>"
                           "<td style='padding:4px 12px;'>批量拆分 Excel、按列拆分、合并</td></tr>"
                           "<tr><td style='padding:4px 12px;'>📝 Word</td>"
                           "<td style='padding:4px 12px;'>poword</td>"
                           "<td style='padding:4px 12px;'>Word 转 PDF、批量加水印</td></tr>"
                           "<tr style='background:#F3FBFF;'><td style='padding:4px 12px;'>🎨 PPT</td>"
                           "<td style='padding:4px 12px;'>poppt</td>"
                           "<td style='padding:4px 12px;'>批量生成 PPT</td></tr>"
                           "<tr><td style='padding:4px 12px;'>🖼️ 图片</td>"
                           "<td style='padding:4px 12px;'>poimage</td>"
                           "<td style='padding:4px 12px;'>加水印、压缩、转字符画、GIF 拼接</td></tr>"
                           "<tr style='background:#F3FBFF;'><td style='padding:4px 12px;'>📂 文件</td>"
                           "<td style='padding:4px 12px;'>pofile</td>"
                           "<td style='padding:4px 12px;'>批量重命名、整理文件、按类型分类</td></tr>"
                           "<tr><td style='padding:4px 12px;'>📧 邮件</td>"
                           "<td style='padding:4px 12px;'>poemail</td>"
                           "<td style='padding:4px 12px;'>群发邮件、读取收件箱</td></tr>"
                           "<tr style='background:#F3FBFF;'><td style='padding:4px 12px;'>🔍 OCR</td>"
                           "<td style='padding:4px 12px;'>poocr</td>"
                           "<td style='padding:4px 12px;'>增值税发票识别 → Excel</td></tr>"
                           "<tr><td style='padding:4px 12px;'>🎬 视频</td>"
                           "<td style='padding:4px 12px;'>povideo</td>"
                           "<td style='padding:4px 12px;'>视频合成、压缩、提取音频</td></tr>"
                           "<tr style='background:#F3FBFF;'><td style='padding:4px 12px;'>💬 微信</td>"
                           "<td style='padding:4px 12px;'>PyOfficeRobot</td>"
                           "<td style='padding:4px 12px;'>自动发消息、关键词回复、智能机器人</td></tr>"
                           "<tr><td style='padding:4px 12px;'>🛠️ 工具</td>"
                           "<td style='padding:4px 12px;'>wftools</td>"
                           "<td style='padding:4px 12px;'>翻译、二维码、随机密码、天气、网速</td></tr>"
                           "<tr style='background:#F3FBFF;'><td style='padding:4px 12px;'>📈 金融</td>"
                           "<td style='padding:4px 12px;'>pofinance</td>"
                           "<td style='padding:4px 12px;'>股票 T+0 交易成本计算</td></tr>"
                           "</table>"
                           "<hr>"
                           "<p style='color:#294661;font-size:12px;'>"
                           "💡 安装指定子模块：<code>pip install python-office[pdf,excel,...]</code><br>"
                           "💡 安装所有子模块：<code>pip install python-office[all]</code><br>"
                           "💡 Windows 全功能：<code>pip install python-office[all-windows]</code>"
                           "</p>"
                       ),
                       param_descriptions={}),
    ]
    cats.append(c)

    # --- 微信机器人（按官方文档 https://www.python-office.com/modules/wechat/api 的 7 个函数）---
    c = _cat("wechat", "微信机器人", "💬", 120)
    c.features = [
        _build_feature("send_message", "发送消息", "向好友 / 群发送文本消息。",
                       "office.api.wechat", "send_message",
                       cli_only=True,
                       cli_command=(
                           "# 前置：PC 微信客户端已登录\n"
                           "python -c \"from office.api.wechat import send_message; send_message('好友备注', '消息内容')\"\n"
                       ),
                       param_descriptions={
                           "who":     "好友昵称 / 群名（如 '文件传输助手' / '家人'）。",
                           "message": "要发送的文本内容。",
                       }),
        _build_feature("send_message_by_time", "定时发送", "在指定时间自动发送消息。",
                       "office.api.wechat", "send_message_by_time",
                       cli_only=True,
                       cli_command=(
                           "# 前置：PC 微信客户端已登录；到点前请保持程序运行\n"
                           "python -c \"from office.api.wechat import send_message_by_time; "
                           "send_message_by_time('好友备注', '消息内容', '2026-06-15 09:00:00')\"\n"
                           "# 程序会一直等到指定时间才发，期间保持窗口不关闭\n"
                       ),
                       param_descriptions={
                           "who":     "好友昵称 / 群名。",
                           "message": "要发送的文本内容。",
                           "time":    "定时发送时间，格式 'YYYY-MM-DD HH:MM:SS'，如 '2026-06-15 09:00:00'。",
                       }),
        _build_feature("chat_by_keywords", "关键词自动回复", "根据关键词字典自动回复好友 / 群。",
                       "office.api.wechat", "chat_by_keywords",
                       cli_only=True,
                       cli_command=(
                           "# 前置：PC 微信客户端已登录\n"
                           "# keywords 传 dict，例如 {\"你好\": \"你好！\", \"在吗\": \"在的\"}\n"
                           "python -c \"from office.api.wechat import chat_by_keywords; "
                           "chat_by_keywords('好友备注', {'你好': '你好！'})\"\n"
                           "# 进入无限循环监听，按 Ctrl+C 退出\n"
                       ),
                       param_overrides={
                           "keywords": {"kind": "text"},
                       },
                       param_descriptions={
                           "who":      "要监听的好友 / 群名。",
                           "keywords": "关键词 → 回复内容的字典，多行文本框输入 JSON，例如 {\"你好\": \"你好！\"}。",
                       }),
        _build_feature("send_file", "发送文件", "通过微信发送本地文件给好友 / 群。",
                       "office.api.wechat", "send_file",
                       cli_only=True,
                       cli_command=(
                           "# 前置：PC 微信客户端已登录\n"
                           "python -c \"from office.api.wechat import send_file; send_file('好友备注', 'C:/path/file.pdf')\"\n"
                       ),
                       param_descriptions={
                           "who":  "好友昵称 / 群名。",
                           "file": "要发送的文件路径。",
                       }),
        _build_feature("group_send", "群发消息", "按预设群组列表批量发送消息。",
                       "office.api.wechat", "group_send",
                       cli_only=True,
                       cli_command=(
                           "# 前置：PC 微信客户端已登录；首次运行会弹窗让你配置群组名单\n"
                           "python -c \"from office.api.wechat import group_send; group_send()\"\n"
                           "# 会弹出 PyQt5 配置窗口，配置好后保存为本地名单文件\n"
                       ),
                       param_descriptions={}),
        _build_feature("receive_message", "接收消息", "监听并保存收到的微信消息。",
                       "office.api.wechat", "receive_message",
                       cli_only=True,
                       cli_command=(
                           "# 前置：PC 微信客户端已登录\n"
                           "python -c \"from office.api.wechat import receive_message; "
                           "receive_message('好友备注', 'userMessage.txt', 'C:/path/save')\"\n"
                           "# 进入无限循环监听，按 Ctrl+C 退出\n"
                       ),
                       param_overrides={
                           "output_path": {"kind": "dir"},
                       },
                       param_descriptions={
                           "who":         "要监听的好友 / 群名（默认 '文件传输助手'）。",
                           "txt":         "消息保存的文本文件名（默认 'userMessage.txt'）。",
                           "output_path": "消息文件保存目录。",
                       }),
        _build_feature("chat_robot", "智能聊天（微信自动回复机器人）",
                       "在 PC 微信上监听指定好友的消息，自动调用大模型（GPT/DeepSeek/智谱等）生成回复并发回给对方。",
                       "office.api.wechat", "chat_robot",
                       cli_only=True,
                       cli_command=(
                           "# 前置条件：\n"
                           "#   1. PC 微信客户端已登录\n"
                           "#   2. 配置了大模型 API Key（OpenAI / DeepSeek / 智谱 等）\n"
                           "#\n"
                           "# 启动方式 —— 在 PowerShell / CMD 中执行：\n"
                           "python -c \"from office.api.wechat import chat_robot; chat_robot('好友备注名')\"\n"
                           "\n"
                           "# 或交互式 Python：\n"
                           "python\n"
                           ">>> from office.api.wechat import chat_robot\n"
                           ">>> chat_robot('好友备注名')    # 进入无限循环监听\n"
                           "# 按 Ctrl+C 退出\n"
                       ),
                       platform_note="依赖 PC 微信客户端 + 大模型 API Key；运行后会无限循环，需 Ctrl+C 退出。",
                        param_descriptions={
                            "who": "聊天对象（微信里的备注名称，不支持特殊字符，默认 '程序员晚枫'）。",
                        }),
    ]
    cats.append(c)

    gui_cats: list[Category] = []
    for cat in cats:
        features = [feat for feat in cat.features if not feat.cli_only]
        if features:
            gui_cats.append(Category(
                id=cat.id,
                title=cat.title,
                icon=cat.icon,
                order=cat.order,
                features=features,
            ))

    gui_cats.sort(key=lambda x: x.order)
    return gui_cats


def find_feature(categories: list[Category], feature_id: str) -> Optional[Feature]:
    """按 id 查找 Feature。"""
    for cat in categories:
        for feat in cat.features:
            if feat.id == feature_id:
                return feat
    return None
