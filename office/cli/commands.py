# -*- coding: UTF-8 -*-
"""`po` 命令的声明式注册表。

Declarative registry of the `po` command.

注册表自包含全部参数信息：构建 argparse 解析器时无需 import 任何 ``office.api``
模块（只有真正分发调用时才延迟导入），因此 ``po --help`` 的构建过程零依赖。

每个模块条目的字段：

- ``module``：延迟导入的 ``office.api`` 模块路径
- ``help``：模块级帮助文本
- ``platforms``：``None`` 表示全平台；否则为允许的 ``sys.platform`` 列表
- ``commands``：子命令名 -> {help, params}

参数字段：

- ``name``：对应 api 函数的形参名（分发时按此名传 kwargs）
- ``positional``：True 为位置参数，否则为 ``--kebab-case`` 选项
- ``flag``：store_true 布尔开关（仅选项）
- ``type`` / ``nargs`` / ``default`` / ``choices`` / ``required``：直传 argparse

刻意不收录的函数：交互式或长任务（weather、net_speed_test 等）、已废弃
（open_soft 等）、参数为遗留兼容别名的（add_mark / add_watermark）。
"""

MODULES = {
    "pdf": {
        "module": "office.api.pdf",
        "help": "PDF 处理：合并 / 拆分 / 格式转换 / 水印 / 加密",
        "platforms": None,
        "commands": {
            "pdf2docx": {
                "help": "PDF 转 Word / Convert PDF to docx",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "output_file", "help": "输出 docx 文件 / output docx file"},
                ],
            },
            "pdf2imgs": {
                "help": "PDF 转图片 / Convert PDF to images",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "output_file", "help": "输出图片（或目录）/ output image or dir"},
                    {"name": "merge", "flag": True,
                     "help": "合并为长图 / merge into one long image"},
                ],
            },
            "txt2pdf": {
                "help": "文本文件转 PDF / Convert txt to PDF",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "TXT",
                     "help": "输入 txt 文件 / input txt file"},
                    {"name": "output_file", "help": "输出 PDF 文件 / output PDF file"},
                ],
            },
            "split4pdf": {
                "help": "按页码拆分 PDF / Split PDF by page range",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "output_file", "help": "输出 PDF 文件 / output PDF file"},
                    {"name": "from_page", "type": int, "default": -1,
                     "help": "起始页（0 起）/ first page (0-based)"},
                    {"name": "to_page", "type": int, "default": -1,
                     "help": "结束页 / last page"},
                ],
            },
            "merge2pdf": {
                "help": "合并多个 PDF / Merge multiple PDF files",
                "params": [
                    {"name": "input_file_list", "positional": True, "nargs": "+",
                     "metavar": "PDF",
                     "help": "输入 PDF 文件列表 / input PDF files"},
                    {"name": "output_file", "default": "merged.pdf",
                     "help": "输出 PDF 文件，默认 merged.pdf / output file"},
                ],
            },
            "del4pdf": {
                "help": "删除指定页面 / Delete pages from PDF",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "page_nums", "required": True, "nargs": "+", "type": int,
                     "metavar": "PAGE",
                     "help": "要删除的页码（0 起）/ page numbers to delete"},
                    {"name": "output_file", "help": "输出 PDF 文件 / output PDF file"},
                ],
            },
            "encrypt4pdf": {
                "help": "加密 PDF / Encrypt PDF with password",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "password", "required": True,
                     "help": "密码 / password"},
                    {"name": "output_file", "help": "输出 PDF 文件 / output PDF file"},
                ],
            },
            "decrypt4pdf": {
                "help": "解密 PDF / Decrypt PDF",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "password", "required": True,
                     "help": "密码 / password"},
                    {"name": "output_file", "help": "输出 PDF 文件 / output PDF file"},
                ],
            },
            "add_text_watermark": {
                "help": "添加文字水印 / Add text watermark",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "text", "default": "python-office",
                     "help": "水印文字 / watermark text"},
                    {"name": "output_file", "help": "输出 PDF 文件 / output PDF file"},
                    {"name": "fontname", "default": "Helvetica",
                     "help": "字体名 / font name"},
                    {"name": "fontsize", "type": int, "default": 12,
                     "help": "字号 / font size"},
                ],
            },
            "add_img_water": {
                "help": "添加图片水印 / Add image watermark",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "mark_file", "required": True,
                     "help": "水印图片 / watermark image"},
                    {"name": "output_file", "help": "输出 PDF 文件 / output PDF file"},
                ],
            },
            "add_watermark_by_parameters": {
                "help": "参数化文字水印 / Add watermark by parameters",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "输入 PDF 文件 / input PDF file"},
                    {"name": "mark_str", "required": True,
                     "help": "水印文字 / watermark text"},
                    {"name": "output_file", "help": "输出 PDF 文件 / output PDF file"},
                ],
            },
        },
    },
    "excel": {
        "module": "office.api.excel",
        "help": "Excel 处理：模拟数据 / 合并拆分 / 格式转换 / 内容检索",
        "platforms": None,
        "commands": {
            "fake2excel": {
                "help": "生成模拟数据 Excel / Create Excel with fake data",
                "params": [
                    {"name": "columns", "nargs": "+", "default": ["name"],
                     "metavar": "COL",
                     "help": "列名列表，见文档 / column names"},
                    {"name": "rows", "type": int, "default": 1,
                     "help": "行数 / number of rows"},
                    {"name": "path", "default": "./fake2excel.xlsx",
                     "help": "输出文件 / output file"},
                    {"name": "language", "default": "zh_CN",
                     "choices": ["zh_CN", "english"],
                     "help": "数据语言 / data language"},
                ],
            },
            "merge2excel": {
                "help": "多个 Excel 合并为多 sheet / Merge Excel files (one sheet each)",
                "params": [
                    {"name": "dir_path", "positional": True, "metavar": "DIR",
                     "help": "输入目录 / input directory"},
                    {"name": "output_file", "default": "merge2excel.xlsx",
                     "help": "输出文件 / output file"},
                ],
            },
            "sheet2excel": {
                "help": "按 sheet 拆分为多文件 / Split sheets into files",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "XLSX",
                     "help": "输入 Excel 文件 / input Excel file"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                ],
            },
            "merge2sheet": {
                "help": "多个 Excel 合并到一个 sheet / Merge files into one sheet",
                "params": [
                    {"name": "dir_path", "positional": True, "metavar": "DIR",
                     "help": "输入目录 / input directory"},
                    {"name": "output_sheet_name", "default": "Sheet1",
                     "help": "输出 sheet 名 / output sheet name"},
                    {"name": "output_excel_name", "default": "merge2sheet",
                     "help": "输出文件名 / output file name"},
                ],
            },
            "find_excel_data": {
                "help": "搜索 Excel 内容 / Search content in Excel files",
                "params": [
                    {"name": "search_key", "positional": True, "metavar": "KEY",
                     "help": "搜索关键词 / search key"},
                    {"name": "target_dir", "positional": True, "metavar": "DIR",
                     "help": "搜索目录 / directory to search"},
                ],
            },
            "split_excel_by_column": {
                "help": "按列值拆分 Excel / Split Excel by column values",
                "params": [
                    {"name": "filepath", "positional": True, "metavar": "XLSX",
                     "help": "输入 Excel 文件 / input Excel file"},
                    {"name": "column", "positional": True, "type": int, "metavar": "COL",
                     "help": "列号（0 起）/ column index (0-based)"},
                    {"name": "worksheet_name",
                     "help": "sheet 名，默认第一个 / worksheet name"},
                ],
            },
            "excel2pdf": {
                "help": "Excel 转 PDF / Convert Excel to PDF",
                "params": [
                    {"name": "excel_path", "positional": True, "metavar": "XLSX",
                     "help": "输入 Excel 文件 / input Excel file"},
                    {"name": "pdf_path", "positional": True, "metavar": "PDF",
                     "help": "输出 PDF 文件 / output PDF file"},
                    {"name": "sheet_id", "type": int, "default": 0,
                     "help": "sheet 序号（0 起）/ sheet index (0-based)"},
                ],
            },
        },
    },
    "tools": {
        "module": "office.api.tools",
        "help": "实用工具：翻译 / IP 解析 / 二维码 / 密码生成",
        "platforms": None,
        "commands": {
            "url2ip": {
                "help": "域名解析 IP / Resolve URL to IP address",
                "params": [
                    {"name": "url", "positional": True, "metavar": "URL",
                     "help": "URL 或域名 / URL or domain"},
                ],
            },
            "transtools": {
                "help": "文本翻译 / Translate text",
                "params": [
                    {"name": "to_lang", "positional": True, "metavar": "LANG",
                     "help": "目标语言 / target language"},
                    {"name": "content", "positional": True, "metavar": "TEXT",
                     "help": "待翻译内容 / content to translate"},
                    {"name": "from_lang", "default": "zh",
                     "help": "源语言 / source language"},
                ],
            },
            "qrcodetools": {
                "help": "URL 转二维码 / Generate QR code for URL",
                "params": [
                    {"name": "url", "positional": True, "metavar": "URL",
                     "help": "URL / URL to encode"},
                    {"name": "output", "default": "./qrcode_img.png",
                     "help": "输出图片 / output image"},
                ],
            },
            "passwordtools": {
                "help": "生成随机密码 / Generate random password",
                "params": [
                    {"name": "len", "type": int, "default": 8,
                     "help": "密码长度 / password length"},
                ],
            },
        },
    },
}
