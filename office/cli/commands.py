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
            "lottery8ticket": {
                "help": "随机双色球号码 / Random lottery numbers",
                "params": [],
            },
            "create_article": {
                "help": "自动生成文章 / Generate an article",
                "params": [
                    {"name": "theme", "positional": True, "metavar": "THEME",
                     "help": "文章主题 / article theme"},
                    {"name": "line_num", "type": int, "default": 200,
                     "help": "行数 / number of lines"},
                ],
            },
        },
    },
    "image": {
        "module": "office.api.image",
        "help": "图片处理：压缩 / 水印 / 下载 / 词云 / 二维码 / 铅笔画",
        "platforms": None,
        "commands": {
            "compress_image": {
                "help": "压缩图片 / Compress an image",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "IMG",
                     "help": "输入图片 / input image"},
                    {"name": "output_file", "help": "输出图片 / output image"},
                    {"name": "quality", "type": int,
                     "help": "压缩质量 / compression quality"},
                ],
            },
            "add_watermark": {
                "help": "添加文字水印 / Add text watermark",
                "params": [
                    {"name": "file", "positional": True, "metavar": "IMG",
                     "help": "输入图片 / input image"},
                    {"name": "mark", "positional": True, "metavar": "TEXT",
                     "help": "水印文字 / watermark text"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                    {"name": "color", "default": "#eaeaea",
                     "help": "水印颜色 / watermark color"},
                    {"name": "size", "type": int, "default": 30,
                     "help": "字号 / font size"},
                    {"name": "opacity", "type": float, "default": 0.35,
                     "help": "透明度 / opacity"},
                    {"name": "space", "type": int, "default": 200,
                     "help": "水印间距 / watermark spacing"},
                    {"name": "angle", "type": int, "default": 30,
                     "help": "旋转角度 / rotation angle"},
                ],
            },
            "img2Cartoon": {
                "help": "头像转动漫风 / Image to cartoon style (Baidu API)",
                "params": [
                    {"name": "path", "positional": True, "metavar": "IMG",
                     "help": "输入图片 / input image"},
                    {"name": "client_api", "required": True,
                     "help": "百度 API Key / Baidu API key"},
                    {"name": "client_secret", "required": True,
                     "help": "百度 Secret Key / Baidu secret key"},
                ],
            },
            "down4img": {
                "help": "下载图片 / Download an image",
                "params": [
                    {"name": "url", "positional": True, "metavar": "URL",
                     "help": "图片 URL / image URL"},
                    {"name": "output_path", "default": ".",
                     "help": "输出目录 / output directory"},
                    {"name": "output_name", "default": "down4img",
                     "help": "输出文件名 / output file name"},
                    {"name": "type", "default": "jpg",
                     "help": "图片格式 / image format"},
                ],
            },
            "txt2wordcloud": {
                "help": "文本生成词云 / Text to word cloud",
                "params": [
                    {"name": "filename", "positional": True, "metavar": "TXT",
                     "help": "输入文本文件 / input text file"},
                    {"name": "color", "default": "white",
                     "help": "背景色 / background color"},
                    {"name": "result_file", "default": "your_wordcloud.png",
                     "help": "输出图片 / output image"},
                ],
            },
            "pencil4img": {
                "help": "图片转铅笔画 / Image to pencil sketch",
                "params": [
                    {"name": "input_img", "positional": True, "metavar": "IMG",
                     "help": "输入图片 / input image"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                    {"name": "output_name", "default": "pencil4img.jpg",
                     "help": "输出文件名 / output file name"},
                ],
            },
            "decode_qrcode": {
                "help": "解析二维码 / Decode a QR code",
                "params": [
                    {"name": "qrcode_path", "positional": True, "metavar": "IMG",
                     "help": "二维码图片 / QR code image"},
                ],
            },
            "del_watermark": {
                "help": "去除图片水印 / Remove image watermark",
                "params": [
                    {"name": "input_image", "positional": True, "metavar": "IMG",
                     "help": "输入图片 / input image"},
                    {"name": "output_image", "default": "./del_water_mark.jpg",
                     "help": "输出图片 / output image"},
                ],
            },
        },
    },
    "file": {
        "module": "office.api.file",
        "help": "文件管理：批量改名 / 搜索 / 分组 / 清单导出",
        "platforms": None,
        "commands": {
            "replace4filename": {
                "help": "批量替换文件名 / Batch replace in file names",
                "params": [
                    {"name": "path", "positional": True, "metavar": "PATH",
                     "help": "处理的目录或文件 / directory or file"},
                    {"name": "del_content", "positional": True, "metavar": "TEXT",
                     "help": "要删除的内容 / content to remove"},
                    {"name": "replace_content", "default": "",
                     "help": "替换为的内容 / replacement content"},
                    {"name": "dir_rename", "type": "bool", "default": True,
                     "help": "是否改目录名 / rename directories"},
                    {"name": "file_rename", "type": "bool", "default": True,
                     "help": "是否改文件名 / rename files"},
                    {"name": "suffix", "help": "限定后缀，如 .pdf / file suffix filter"},
                ],
            },
            "file_name_insert_content": {
                "help": "文件名插入内容 / Insert content into file name",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "PATH",
                     "help": "文件路径 / file path"},
                    {"name": "insert_position", "positional": True, "type": int,
                     "metavar": "POS",
                     "help": "插入位置 / insert position"},
                    {"name": "insert_content", "positional": True, "metavar": "TEXT",
                     "help": "插入内容 / content to insert"},
                ],
            },
            "file_name_add_prefix": {
                "help": "文件名加前缀 / Add prefix to file name",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "PATH",
                     "help": "文件路径 / file path"},
                    {"name": "prefix_content", "required": True,
                     "help": "前缀内容 / prefix content"},
                ],
            },
            "file_name_add_postfix": {
                "help": "文件名加后缀 / Add postfix to file name",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "PATH",
                     "help": "文件路径 / file path"},
                    {"name": "postfix_content", "required": True,
                     "help": "后缀内容 / postfix content"},
                ],
            },
            "output_file_list_to_excel": {
                "help": "文件清单导出 Excel / Export file list to Excel",
                "params": [
                    {"name": "dir_path", "positional": True, "metavar": "DIR",
                     "help": "目录 / directory"},
                ],
            },
            "search_specify_type_file": {
                "help": "搜索指定类型文件 / Search files by type",
                "params": [
                    {"name": "file_path", "positional": True, "metavar": "DIR",
                     "help": "搜索目录 / directory to search"},
                    {"name": "file_type", "required": True,
                     "help": "文件类型，如 .pdf / file type"},
                ],
            },
            "group_by_name": {
                "help": "按名称分组文件 / Group files by name",
                "params": [
                    {"name": "path", "positional": True, "metavar": "DIR",
                     "help": "目录 / directory"},
                    {"name": "output_path", "help": "输出目录 / output directory"},
                    {"name": "del_old_file", "type": "bool",
                     "help": "删除原文件 / delete old files"},
                ],
            },
            "get_files": {
                "help": "按名称/后缀找文件 / Find files by name/suffix",
                "params": [
                    {"name": "path", "positional": True, "metavar": "DIR",
                     "help": "搜索目录 / directory to search"},
                    {"name": "name", "default": "",
                     "help": "名称包含 / name contains"},
                    {"name": "suffix", "help": "后缀，如 .pdf / suffix filter"},
                    {"name": "sub", "flag": True,
                     "help": "含子目录 / include subdirectories"},
                    {"name": "level", "type": int, "default": 0,
                     "help": "子目录层级 / subdirectory level"},
                ],
            },
        },
    },
    "markdown": {
        "module": "office.api.markdown",
        "help": "Markdown 处理",
        "platforms": None,
        "commands": {
            "excel2markdown": {
                "help": "Excel 转 Markdown 表格 / Excel to Markdown table",
                "params": [
                    {"name": "input_file", "positional": True, "metavar": "XLSX",
                     "help": "输入 Excel / input Excel file"},
                    {"name": "output_file", "default": "./excel2markdown.md",
                     "help": "输出 Markdown / output file"},
                    {"name": "sheet_name", "help": "sheet 名 / sheet name"},
                ],
            },
        },
    },
    "finance": {
        "module": "office.api.finance",
        "help": "金融计算：T+0 交易成本 / T+0 trading cost",
        "platforms": None,
        "commands": {
            "t0": {
                "help": "T+0 买卖收益计算 / T+0 profit calculation",
                "params": [
                    {"name": "buy_price", "positional": True, "type": float,
                     "metavar": "BUY",
                     "help": "买入价 / buy price"},
                    {"name": "sale_price", "positional": True, "type": float,
                     "metavar": "SALE",
                     "help": "卖出价 / sale price"},
                    {"name": "shares", "positional": True, "type": int,
                     "metavar": "N",
                     "help": "股数 / number of shares"},
                    {"name": "w_rate", "type": float, "default": 0.00025,
                     "help": "佣金率 / commission rate"},
                    {"name": "min_rate", "type": float, "default": 5,
                     "help": "最低佣金 / minimum commission"},
                    {"name": "stamp_tax", "type": float, "default": 0.001,
                     "help": "印花税 / stamp tax"},
                ],
            },
        },
    },
    "video": {
        "module": "office.api.video",
        "help": "音视频处理：转 MP3 / 提取文字 / 加水印 / 文字转语音",
        "platforms": None,
        "commands": {
            "video2mp3": {
                "help": "视频提取音频 / Extract audio from video",
                "params": [
                    {"name": "path", "positional": True, "metavar": "VIDEO",
                     "help": "输入视频 / input video"},
                    {"name": "mp3_name", "help": "MP3 文件名 / MP3 file name"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                ],
            },
            "audio2txt": {
                "help": "音频转文字（腾讯云）/ Audio to text (Tencent Cloud)",
                "params": [
                    {"name": "audio_path", "positional": True, "metavar": "AUDIO",
                     "help": "输入音频 / input audio"},
                    {"name": "appid", "required": True, "help": "腾讯云 AppID"},
                    {"name": "secret_id", "required": True,
                     "help": "腾讯云 SecretId"},
                    {"name": "secret_key", "required": True,
                     "help": "腾讯云 SecretKey"},
                ],
            },
            "mark2video": {
                "help": "视频加水印 / Add watermark to video",
                "params": [
                    {"name": "video_path", "positional": True, "metavar": "VIDEO",
                     "help": "输入视频 / input video"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                    {"name": "output_name", "default": "mark2video.mp4",
                     "help": "输出文件名 / output file name"},
                    {"name": "mark_str", "default": "www.python-office.com",
                     "help": "水印文字 / watermark text"},
                    {"name": "font_size", "type": int, "default": 28,
                     "help": "字号 / font size"},
                    {"name": "font_type", "default": "Arial",
                     "help": "字体 / font"},
                    {"name": "font_color", "default": "white",
                     "help": "颜色 / color"},
                ],
            },
            "txt2mp3": {
                "help": "文字转语音 / Text to speech",
                "params": [
                    {"name": "content", "positional": True, "metavar": "TEXT",
                     "help": "文本内容 / text content"},
                    {"name": "file", "help": "文本文件（优先于 content）/ text file"},
                    {"name": "mp3", "default": "./程序员晚枫.mp3",
                     "help": "输出 MP3 / output MP3"},
                    {"name": "speak", "type": "bool", "default": True,
                     "help": "是否直接朗读 / speak aloud"},
                ],
            },
        },
    },
    "web": {
        "module": "office.api.web",
        "help": "网页处理：网页转电子书 / Web page to ebook",
        "platforms": None,
        "commands": {
            "url2ebook": {
                "help": "网页转电子书 / Convert web page to ebook",
                "params": [
                    {"name": "url", "positional": True, "metavar": "URL",
                     "help": "网页 URL / page URL"},
                    {"name": "tile", "positional": True, "metavar": "TITLE",
                     "help": "书名 / ebook title"},
                ],
            },
        },
    },
    "word": {
        "module": "office.api.word",
        "help": "Word 处理（仅 Windows）/ Word processing (Windows only)",
        "platforms": ["win32"],
        "commands": {
            "docx2pdf": {
                "help": "Word 转 PDF / Word to PDF",
                "params": [
                    {"name": "path", "positional": True, "metavar": "DOCX",
                     "help": "输入 Word / input Word file"},
                    {"name": "output_path", "help": "输出路径 / output path"},
                ],
            },
            "merge4docx": {
                "help": "合并多个 Word / Merge Word files",
                "params": [
                    {"name": "input_path", "positional": True, "metavar": "DIR",
                     "help": "输入目录 / input directory"},
                    {"name": "output_path", "positional": True, "metavar": "DIR",
                     "help": "输出目录 / output directory"},
                    {"name": "new_word_name", "default": "merge4docx",
                     "help": "合并后文件名 / merged file name"},
                ],
            },
            "doc2docx": {
                "help": "doc 转 docx / Convert doc to docx",
                "params": [
                    {"name": "input_path", "positional": True, "metavar": "DIR",
                     "help": "输入目录 / input directory"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                    {"name": "output_name", "help": "输出文件名 / output file name"},
                ],
            },
            "docx2doc": {
                "help": "docx 转 doc / Convert docx to doc",
                "params": [
                    {"name": "input_path", "positional": True, "metavar": "DIR",
                     "help": "输入目录 / input directory"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                    {"name": "output_name", "help": "输出文件名 / output file name"},
                ],
            },
            "docx4imgs": {
                "help": "Word 转图片 / Word to images",
                "params": [
                    {"name": "word_path", "positional": True, "metavar": "DOCX",
                     "help": "输入 Word / input Word file"},
                    {"name": "img_path", "positional": True, "metavar": "DIR",
                     "help": "输出目录 / output directory"},
                ],
            },
        },
    },
    "ppt": {
        "module": "office.api.ppt",
        "help": "PPT 处理（仅 Windows）/ PPT processing (Windows only)",
        "platforms": ["win32"],
        "commands": {
            "ppt2pdf": {
                "help": "PPT 转 PDF / PPT to PDF",
                "params": [
                    {"name": "path", "positional": True, "metavar": "PPT",
                     "help": "输入 PPT / input PPT file"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                ],
            },
            "ppt2img": {
                "help": "PPT 转图片 / PPT to images",
                "params": [
                    {"name": "input_path", "positional": True, "metavar": "DIR",
                     "help": "输入目录 / input directory"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                    {"name": "merge", "flag": True,
                     "help": "合并为长图 / merge into one image"},
                ],
            },
            "merge4ppt": {
                "help": "合并多个 PPT / Merge PPT files",
                "params": [
                    {"name": "input_path", "positional": True, "metavar": "DIR",
                     "help": "输入目录 / input directory"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                    {"name": "output_name", "default": "merge4ppt.pptx",
                     "help": "输出文件名 / output file name"},
                ],
            },
        },
    },
    "wechat": {
        "module": "office.api.wechat",
        "help": "微信机器人（仅 Windows，需桌面微信）/ WeChat robot (Windows only)",
        "platforms": ["win32"],
        "commands": {
            "send_message": {
                "help": "发送消息 / Send a message",
                "params": [
                    {"name": "who", "positional": True, "metavar": "WHO",
                     "help": "接收人 / recipient"},
                    {"name": "message", "positional": True, "metavar": "TEXT",
                     "help": "消息内容 / message"},
                ],
            },
            "send_message_by_time": {
                "help": "定时发送消息 / Send a message at a given time",
                "params": [
                    {"name": "who", "positional": True, "metavar": "WHO",
                     "help": "接收人 / recipient"},
                    {"name": "message", "positional": True, "metavar": "TEXT",
                     "help": "消息内容 / message"},
                    {"name": "time", "required": True,
                     "help": "发送时间 / send time"},
                ],
            },
            "send_file": {
                "help": "发送文件 / Send a file",
                "params": [
                    {"name": "who", "positional": True, "metavar": "WHO",
                     "help": "接收人 / recipient"},
                    {"name": "file", "positional": True, "metavar": "FILE",
                     "help": "文件路径 / file path"},
                ],
            },
            "chat_by_keywords": {
                "help": "关键词自动回复 / Auto-reply by keywords",
                "params": [
                    {"name": "who", "positional": True, "metavar": "WHO",
                     "help": "聊天对象 / chat target"},
                    {"name": "keywords", "positional": True, "metavar": "TEXT",
                     "help": "关键词 / keywords"},
                ],
            },
            "group_send": {
                "help": "群发消息 / Broadcast a message",
                "params": [],
            },
            "receive_message": {
                "help": "接收消息 / Receive messages",
                "params": [
                    {"name": "who", "default": "文件传输助手",
                     "help": "聊天对象 / chat target"},
                    {"name": "txt", "default": "userMessage.txt",
                     "help": "消息记录文件 / message log file"},
                    {"name": "output_path", "default": "./",
                     "help": "输出目录 / output directory"},
                ],
            },
            "chat_robot": {
                "help": "自动聊天机器人 / Chat robot",
                "params": [
                    {"name": "who", "default": "程序员晚枫",
                     "help": "聊天对象 / chat target"},
                ],
            },
        },
    },
}
