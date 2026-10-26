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
        "help": "PDF: merge, split, convert, watermark, encrypt",
        "platforms": None,
        "commands": {
            "pdf2docx": {
                "help": "Convert PDF to docx",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "output_file", "help": "output docx file"},
                ],
            },
            "pdf2imgs": {
                "help": "Convert PDF to images",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "output_file", "help": "output image (or dir)"},
                    {"name": "merge", "flag": True,
                     "help": "merge into one long image"},
                ],
            },
            "txt2pdf": {
                "help": "Convert txt to PDF",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "TXT",
                     "help": "input txt file"},
                    {"name": "output_file", "help": "output PDF file"},
                ],
            },
            "split4pdf": {
                "help": "Split PDF by page range",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "output_file", "help": "output PDF file"},
                    {"name": "from_page", "type": int, "default": -1,
                     "help": "first page (0-based)"},
                    {"name": "to_page", "type": int, "default": -1,
                     "help": "last page"},
                ],
            },
            "merge2pdf": {
                "help": "Merge multiple PDF files",
                "params": [
                    {"name": "input_file_list", "positional": True, "nargs": "+",
                     "metavar": "PDF",
                     "help": "input PDF files"},
                    {"name": "output_file", "default": "merged.pdf",
                     "help": "output file"},
                ],
            },
            "del4pdf": {
                "help": "Delete pages from PDF",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "page_nums", "required": True, "nargs": "+", "type": int,
                     "metavar": "PAGE",
                     "help": "page numbers to delete (0-based)"},
                    {"name": "output_file", "help": "output PDF file"},
                ],
            },
            "encrypt4pdf": {
                "help": "Encrypt PDF with password",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "password", "required": True,
                     "help": "password"},
                    {"name": "output_file", "help": "output PDF file"},
                ],
            },
            "decrypt4pdf": {
                "help": "Decrypt PDF",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "password", "required": True,
                     "help": "password"},
                    {"name": "output_file", "help": "output PDF file"},
                ],
            },
            "add_text_watermark": {
                "help": "Add text watermark",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "text", "default": "python-office",
                     "help": "watermark text"},
                    {"name": "output_file", "help": "output PDF file"},
                    {"name": "fontname", "default": "Helvetica",
                     "help": "font name"},
                    {"name": "fontsize", "type": int, "default": 12,
                     "help": "font size"},
                ],
            },
            "add_img_water": {
                "help": "Add image watermark",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "mark_file", "required": True,
                     "help": "watermark image"},
                    {"name": "output_file", "help": "output PDF file"},
                ],
            },
            "add_watermark_by_parameters": {
                "help": "Add watermark by parameters",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "PDF",
                     "help": "input PDF file"},
                    {"name": "mark_str", "required": True,
                     "help": "watermark text"},
                    {"name": "output_file", "help": "output PDF file"},
                ],
            },
        },
    },
    "excel": {
        "module": "office.api.excel",
        "help": "Excel: fake data, merge/split, convert, search",
        "platforms": None,
        "commands": {
            "fake2excel": {
                "help": "Create Excel with fake data",
                "params": [
                    {"name": "columns", "nargs": "+", "default": ["name"],
                     "metavar": "COL",
                     "help": "column names"},
                    {"name": "rows", "type": int, "default": 1,
                     "help": "number of rows"},
                    {"name": "path", "default": "./fake2excel.xlsx",
                     "help": "output file"},
                    {"name": "language", "default": "zh_CN",
                     "choices": ["zh_CN", "english"],
                     "help": "data language"},
                ],
            },
            "merge2excel": {
                "help": "Merge Excel files (one sheet each)",
                "params": [
                    {"name": "dir_path", "positional": True, "metavar": "DIR",
                     "help": "input directory"},
                    {"name": "output_file", "default": "merge2excel.xlsx",
                     "help": "output file"},
                ],
            },
            "sheet2excel": {
                "help": "Split sheets into files",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "XLSX",
                     "help": "input Excel file"},
                    {"name": "output_path", "default": "./",
                     "help": "output directory"},
                ],
            },
            "merge2sheet": {
                "help": "Merge files into one sheet",
                "params": [
                    {"name": "dir_path", "positional": True, "metavar": "DIR",
                     "help": "input directory"},
                    {"name": "output_sheet_name", "default": "Sheet1",
                     "help": "output sheet name"},
                    {"name": "output_excel_name", "default": "merge2sheet",
                     "help": "output file name"},
                ],
            },
            "find_excel_data": {
                "help": "Search content in Excel files",
                "params": [
                    {"name": "search_key", "positional": True, "metavar": "KEY",
                     "help": "search key"},
                    {"name": "target_dir", "positional": True, "metavar": "DIR",
                     "help": "directory to search"},
                ],
            },
            "split_excel_by_column": {
                "help": "Split Excel by column values",
                "params": [
                    {"name": "filepath", "positional": True, "metavar": "XLSX",
                     "help": "input Excel file"},
                    {"name": "column", "positional": True, "type": int, "metavar": "COL",
                     "help": "column index (0-based)"},
                    {"name": "worksheet_name",
                     "help": "worksheet name"},
                ],
            },
            "excel2pdf": {
                "help": "Convert Excel to PDF",
                "params": [
                    {"name": "excel_path", "positional": True, "metavar": "XLSX",
                     "help": "input Excel file"},
                    {"name": "pdf_path", "positional": True, "metavar": "PDF",
                     "help": "output PDF file"},
                    {"name": "sheet_id", "type": int, "default": 0,
                     "help": "sheet index (0-based)"},
                ],
            },
        },
    },
    "tools": {
        "module": "office.api.tools",
        "help": "Utilities: translate, URL-to-IP, QR code, password",
        "platforms": None,
        "commands": {
            "url2ip": {
                "help": "Resolve URL to IP address",
                "params": [
                    {"name": "url", "positional": True, "metavar": "URL",
                     "help": "URL or domain"},
                ],
            },
            "transtools": {
                "help": "Translate text",
                "params": [
                    {"name": "to_lang", "positional": True, "metavar": "LANG",
                     "help": "target language"},
                    {"name": "content", "positional": True, "metavar": "TEXT",
                     "help": "content to translate"},
                    {"name": "from_lang", "default": "zh",
                     "help": "source language"},
                ],
            },
            "qrcodetools": {
                "help": "Generate QR code for URL",
                "params": [
                    {"name": "url", "positional": True, "metavar": "URL",
                     "help": "URL to encode"},
                    {"name": "output", "default": "./qrcode_img.png",
                     "help": "output image"},
                ],
            },
            "passwordtools": {
                "help": "Generate random password",
                "params": [
                    {"name": "len", "type": int, "default": 8,
                     "help": "password length"},
                ],
            },
            "lottery8ticket": {
                "help": "Random lottery numbers",
                "params": [],
            },
            "create_article": {
                "help": "Generate an article",
                "params": [
                    {"name": "theme", "positional": True, "metavar": "THEME",
                     "help": "article theme"},
                    {"name": "line_num", "type": int, "default": 200,
                     "help": "number of lines"},
                ],
            },
        },
    },
    "image": {
        "module": "office.api.image",
        "help": "Image: compress, watermark, download, word cloud, QR, sketch",
        "platforms": None,
        "commands": {
            "compress_image": {
                "help": "Compress an image",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "IMG",
                     "help": "input image"},
                    {"name": "output_file", "default": "./compress_img.jpg",
                     "help": "output image"},
                    {"name": "quality", "type": int, "default": 95,
                     "help": "compression quality (0-95)"},
                ],
            },
            "add_watermark": {
                "help": "Add text watermark",
                "params": [
                    {"name": "file", "positional": True, "metavar": "IMG",
                     "help": "input image"},
                    {"name": "mark", "positional": True, "metavar": "TEXT",
                     "help": "watermark text"},
                    {"name": "output_path", "default": "./",
                     "help": "output directory"},
                    {"name": "color", "default": "#eaeaea",
                     "help": "watermark color"},
                    {"name": "size", "type": int, "default": 30,
                     "help": "font size"},
                    {"name": "opacity", "type": float, "default": 0.35,
                     "help": "opacity"},
                    {"name": "space", "type": int, "default": 200,
                     "help": "watermark spacing"},
                    {"name": "angle", "type": int, "default": 30,
                     "help": "rotation angle"},
                ],
            },
            "img2Cartoon": {
                "help": "Image to cartoon style (Baidu API)",
                "params": [
                    {"name": "path", "positional": True, "metavar": "IMG",
                     "help": "input image"},
                    {"name": "client_api", "required": True,
                     "help": "Baidu API key"},
                    {"name": "client_secret", "required": True,
                     "help": "Baidu secret key"},
                ],
            },
            "down4img": {
                "help": "Download an image",
                "params": [
                    {"name": "url", "positional": True, "metavar": "URL",
                     "help": "image URL"},
                    {"name": "output_path", "default": ".",
                     "help": "output directory"},
                    {"name": "output_name", "default": "down4img",
                     "help": "output file name"},
                    {"name": "type", "default": "jpg",
                     "help": "image format"},
                ],
            },
            "txt2wordcloud": {
                "help": "Text to word cloud",
                "params": [
                    {"name": "filename", "positional": True, "metavar": "TXT",
                     "help": "input text file"},
                    {"name": "color", "default": "white",
                     "help": "background color"},
                    {"name": "result_file", "default": "your_wordcloud.png",
                     "help": "output image"},
                ],
            },
            "pencil4img": {
                "help": "Image to pencil sketch",
                "params": [
                    {"name": "input_img", "positional": True, "metavar": "IMG",
                     "help": "input image"},
                    {"name": "output_path", "default": "./",
                     "help": "output directory"},
                    {"name": "output_name", "default": "pencil4img.jpg",
                     "help": "output file name"},
                ],
            },
            "decode_qrcode": {
                "help": "Decode a QR code",
                "params": [
                    {"name": "qrcode_path", "positional": True, "metavar": "IMG",
                     "help": "QR code image"},
                ],
            },
            "del_watermark": {
                "help": "Remove image watermark",
                "params": [
                    {"name": "input_image", "positional": True, "metavar": "IMG",
                     "help": "input image"},
                    {"name": "output_image", "default": "./del_water_mark.jpg",
                     "help": "output image"},
                ],
            },
        },
    },
    "file": {
        "module": "office.api.file",
        "help": "File management: batch rename, search, group, list export",
        "platforms": None,
        "commands": {
            "replace4filename": {
                "help": "Batch replace in file names",
                "params": [
                    {"name": "path", "positional": True, "metavar": "PATH",
                     "help": "directory or file"},
                    {"name": "del_content", "positional": True, "metavar": "TEXT",
                     "help": "content to remove"},
                    {"name": "replace_content", "default": "",
                     "help": "replacement content"},
                    {"name": "dir_rename", "type": "bool", "default": True,
                     "help": "rename directories"},
                    {"name": "file_rename", "type": "bool", "default": True,
                     "help": "rename files"},
                    {"name": "suffix", "help": "file suffix filter"},
                ],
            },
            "file_name_insert_content": {
                "help": "Insert content into file name",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "PATH",
                     "help": "file path"},
                    {"name": "insert_position", "positional": True, "type": int,
                     "metavar": "POS",
                     "help": "insert position"},
                    {"name": "insert_content", "positional": True, "metavar": "TEXT",
                     "help": "content to insert"},
                ],
            },
            "file_name_add_prefix": {
                "help": "Add prefix to file name",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "PATH",
                     "help": "file path"},
                    {"name": "prefix_content", "required": True,
                     "help": "prefix content"},
                ],
            },
            "file_name_add_postfix": {
                "help": "Add postfix to file name",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "PATH",
                     "help": "file path"},
                    {"name": "postfix_content", "required": True,
                     "help": "postfix content"},
                ],
            },
            "output_file_list_to_excel": {
                "help": "Export file list to Excel",
                "params": [
                    {"name": "dir_path", "positional": True, "metavar": "DIR",
                     "help": "directory"},
                ],
            },
            "search_specify_type_file": {
                "help": "Search files by type",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "DIR",
                     "help": "directory to search"},
                    {"name": "file_type", "required": True,
                     "help": "file type"},
                ],
            },
            "group_by_name": {
                "help": "Group files by name",
                "params": [
                    {"name": "path", "positional": True, "metavar": "DIR",
                     "help": "directory"},
                    {"name": "output_path", "help": "output directory"},
                    {"name": "del_old_file", "type": "bool",
                     "help": "delete old files"},
                ],
            },
            "get_files": {
                "help": "Find files by name/suffix",
                "params": [
                    {"name": "path", "positional": True, "metavar": "DIR",
                     "help": "directory to search"},
                    {"name": "name", "default": "",
                     "help": "name contains"},
                    {"name": "suffix", "help": "suffix filter"},
                    {"name": "sub", "flag": True,
                     "help": "include subdirectories"},
                    {"name": "level", "type": int, "default": 0,
                     "help": "subdirectory level"},
                ],
            },
        },
    },
    "markdown": {
        "module": "office.api.markdown",
        "help": "Markdown processing",
        "platforms": None,
        "commands": {
            "excel2markdown": {
                "help": "Excel to Markdown table",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "XLSX",
                     "help": "input Excel file"},
                    {"name": "output_file", "default": "./excel2markdown.md",
                     "help": "output file"},
                    {"name": "sheet_name", "help": "sheet name"},
                ],
            },
        },
    },
    "finance": {
        "module": "office.api.finance",
        "help": "T+0 trading cost",
        "platforms": None,
        "commands": {
            "t0": {
                "help": "T+0 profit calculation",
                "params": [
                    {"name": "buy_price", "positional": True, "type": float,
                     "metavar": "BUY",
                     "help": "buy price"},
                    {"name": "sale_price", "positional": True, "type": float,
                     "metavar": "SALE",
                     "help": "sale price"},
                    {"name": "shares", "positional": True, "type": int,
                     "metavar": "N",
                     "help": "number of shares"},
                    {"name": "w_rate", "type": float, "default": 0.00025,
                     "help": "commission rate"},
                    {"name": "min_rate", "type": float, "default": 5,
                     "help": "minimum commission"},
                    {"name": "stamp_tax", "type": float, "default": 0.001,
                     "help": "stamp tax"},
                ],
            },
        },
    },
}
