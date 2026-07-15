# python-office Skills 索引

> 将 `python-office` 库的所有方法封装为独立的 Skill（技能），
> 每个 Skill 都是一个独立的子目录，可以单独调用。

## 目录

- [Email 邮件](#email-邮件) - ⚠️ 暂无可用方法
- [Excel 处理](#excel-处理)
- [File 文件处理](#file-文件处理)
- [Finance 金融计算](#finance-金融计算)
- [Image 图像处理](#image-图像处理)
- [Markdown 处理](#markdown-处理)
- [OCR 识别](#ocr-识别)
- [PDF 处理](#pdf-处理)
- [PPT 处理](#ppt-处理)
- [Tools 工具](#tools-工具)
- [Video 视频处理](#video-视频处理)
- [WeChat 微信](#wechat-微信)
- [Word 文档处理](#word-文档处理)
- [Ruiming 测试 API](#ruiming-测试-api)

---

## 使用方式

每个 Skill 都可以单独导入和调用：

```python
# 方式 1：直接导入函数
from skills.excel import fake2excel
fake2excel(rows=10)

# 方式 2：导入子模块
from skills.excel import fake2excel as fe
fe(rows=10, columns=['name', 'phone'])
```

每个 Skill 目录下都有 `SKILL.md` 文件，详细说明该 Skill 的参数、返回值和使用示例。

---

## Email 邮件

> ⚠️ 暂无可用 Skill
>
> `office/api/email.py` 中所有方法（`send_email`、`receive_email` 等）目前都已被注释，
> 没有可对外暴露的函数，因此暂未封装 Skill。

---

## Excel 处理

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `fake2excel` | 自动创建 Excel 并模拟数据 | `office/skills/excel/fake2excel/` |
| `merge2excel` | 多个 Excel 合并到一个文件的不同 sheet 中 | `office/skills/excel/merge2excel/` |
| `sheet2excel` | 同一个 Excel 的不同 sheet 拆分为不同文件 | `office/skills/excel/sheet2excel/` |
| `merge2sheet` | 多个 Excel 的多个 sheet 自动合并 | `office/skills/excel/merge2sheet/` |
| `find_excel_data` | 搜索 Excel 中指定内容 | `office/skills/excel/find_excel_data/` |
| `split_excel_by_column` | 按指定列拆分 Excel | `office/skills/excel/split_excel_by_column/` |
| `excel2pdf` | Excel 转 PDF | `office/skills/excel/excel2pdf/` |

调用示例：
```python
from skills.excel import fake2excel
fake2excel(columns=['name', 'phone'], rows=100, path='./test.xlsx')
```

---

## File 文件处理

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `replace4filename` | 批量修改文件/文件夹名称 | `office/skills/file/replace4filename/` |
| `file_name_insert_content` | 在文件名中间插入字符 | `office/skills/file/file_name_insert_content/` |
| `file_name_add_prefix` | 给文件名增加前缀 | `office/skills/file/file_name_add_prefix/` |
| `file_name_add_postfix` | 给文件名增加后缀 | `office/skills/file/file_name_add_postfix/` |
| `output_file_list_to_excel` | 整理文件名到 Excel | `office/skills/file/output_file_list_to_excel/` |
| `add_line_by_type` | 根据类型添加行 | `office/skills/file/add_line_by_type/` |
| `search_specify_type_file` | 搜索指定类型文件 | `office/skills/file/search_specify_type_file/` |
| `group_by_name` | 按名称分组整理文件 | `office/skills/file/group_by_name/` |
| `get_files` | 搜索指定类型文件并返回列表 | `office/skills/file/get_files/` |

调用示例：
```python
from skills.file import replace4filename
replace4filename(path='./test_dir', del_content='old', replace_content='new')
```

---

## Finance 金融计算

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `t0` | 计算做 T 的收益 | `office/skills/finance/t0/` |

调用示例：
```python
from skills.finance import t0
profit = t0(buy_price=11.99, sale_price=12.26, shares=700)
print(profit)
```

---

## Image 图像处理

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `compress_image` | 压缩图像 | `office/skills/image/compress_image/` |
| `image2gif` | 图像转 GIF | `office/skills/image/image2gif/` |
| `add_watermark` | 给图片加水印 | `office/skills/image/add_watermark/` |
| `img2Cartoon` | 图片转卡通风格 | `office/skills/image/img2Cartoon/` |
| `down4img` | 下载图片 | `office/skills/image/down4img/` |
| `txt2wordcloud` | 生成词云 | `office/skills/image/txt2wordcloud/` |
| `pencil4img` | 图片转铅笔画 | `office/skills/image/pencil4img/` |
| `decode_qrcode` | 解析二维码 | `office/skills/image/decode_qrcode/` |
| `del_watermark` | 删除图片水印 | `office/skills/image/del_watermark/` |

调用示例：
```python
from skills.image import add_watermark
add_watermark(file='test.png', mark='python-office')
```

---

## Markdown 处理

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `excel2markdown` | Excel 转 Markdown | `office/skills/markdown/excel2markdown/` |

---

## OCR 识别

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `VatInvoiceOCR2Excel` | 增值税发票 OCR 识别并导出 Excel | `office/skills/ocr/VatInvoiceOCR2Excel/` |

---

## PDF 处理

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `pdf2docx` | PDF 转 Word | `office/skills/pdf/pdf2docx/` |
| `pdf2imgs` | PDF 转图片 | `office/skills/pdf/pdf2imgs/` |
| `txt2pdf` | 文本文件转 PDF | `office/skills/pdf/txt2pdf/` |
| `split4pdf` | 拆分 PDF 文件 | `office/skills/pdf/split4pdf/` |
| `encrypt4pdf` | 加密 PDF 文件 | `office/skills/pdf/encrypt4pdf/` |
| `decrypt4pdf` | 解密 PDF 文件 | `office/skills/pdf/decrypt4pdf/` |
| `add_text_watermark` | 添加文本水印 | `office/skills/pdf/add_text_watermark/` |
| `merge2pdf` | 合并多个 PDF 文件 | `office/skills/pdf/merge2pdf/` |
| `del4pdf` | 删除 PDF 指定页面 | `office/skills/pdf/del4pdf/` |
| `add_img_water` | 给 PDF 添加图片水印 | `office/skills/pdf/add_img_water/` |
| `add_watermark` | 给 PDF 添加水印（交互模式） | `office/skills/pdf/add_watermark/` |
| `add_mark` | 给 PDF 添加水印 | `office/skills/pdf/add_mark/` |
| `add_watermark_by_parameters` | 参数化添加水印 | `office/skills/pdf/add_watermark_by_parameters/` |

---

## PPT 处理

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `ppt2pdf` | PPT 转 PDF | `office/skills/ppt/ppt2pdf/` |
| `ppt2img` | PPT 转图片 | `office/skills/ppt/ppt2img/` |
| `merge4ppt` | 合并多个 PPT 文件 | `office/skills/ppt/merge4ppt/` |

---

## Tools 工具

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `transtools` | 翻译工具 | `office/skills/tools/transtools/` |
| `qrcodetools` | 生成二维码 | `office/skills/tools/qrcodetools/` |
| `passwordtools` | 生成密码 | `office/skills/tools/passwordtools/` |
| `weather` | 获取当前天气 | `office/skills/tools/weather/` |
| `url2ip` | URL 转 IP 地址 | `office/skills/tools/url2ip/` |
| `lottery8ticket` | 生成 8 位彩票号码 | `office/skills/tools/lottery8ticket/` |
| `create_article` | 自动创建文章 | `office/skills/tools/create_article/` |
| `pwd4wifi` | 生成 WiFi 密码列表 | `office/skills/tools/pwd4wifi/` |
| `net_speed_test` | 网络速度测试 | `office/skills/tools/net_speed_test/` |
| `course` | 显示课程信息 | `office/skills/tools/course/` |

---

## Video 视频处理

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `video2mp3` | 视频转 MP3 | `office/skills/video/video2mp3/` |
| `audio2txt` | 音频提取文字 | `office/skills/video/audio2txt/` |
| `mark2video` | 给视频添加水印 | `office/skills/video/mark2video/` |
| `txt2mp3` | 文本转语音 | `office/skills/video/txt2mp3/` |

---

## WeChat 微信

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `send_message` | 发送消息给指定联系人 | `office/skills/wechat/send_message/` |
| `send_message_by_time` | 定时发送消息 | `office/skills/wechat/send_message_by_time/` |
| `chat_by_keywords` | 关键词自动聊天 | `office/skills/wechat/chat_by_keywords/` |
| `send_file` | 发送文件 | `office/skills/wechat/send_file/` |
| `group_send` | 群发消息 | `office/skills/wechat/group_send/` |
| `receive_message` | 接收微信消息 | `office/skills/wechat/receive_message/` |
| `chat_robot` | 智能聊天 | `office/skills/wechat/chat_robot/` |

---

## Word 文档处理

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `docx2pdf` | Word 转 PDF | `office/skills/word/docx2pdf/` |
| `merge4docx` | 合并多个 Docx 文件 | `office/skills/word/merge4docx/` |
| `doc2docx` | Doc 转 Docx | `office/skills/word/doc2docx/` |
| `docx2doc` | Docx 转 Doc | `office/skills/word/docx2doc/` |
| `docx4imgs` | 从 Word 提取图片 | `office/skills/word/docx4imgs/` |

---

## Ruiming 测试 API

| Skill | 功能 | 所在路径 |
|-------|------|----------|
| `screen_unmarked_image` | 筛选未标记的图像 | `office/skills/ruiming/screen_unmarked_image/` |
| `change_label_in_xml` | 修改 XML 中的 label | `office/skills/ruiming/change_label_in_xml/` |
| `screen_without_label_json_file` | 筛选无 label JSON 的文件 | `office/skills/ruiming/screen_without_label_json_file/` |

---

## 设计说明

每个 Skill 的目录结构：

```
office/skills/<category>/<skill_name>/
├── SKILL.md       # Skill 的详细说明文档
└── __init__.py    # 暴露 Skill 接口，让用户可以单独调用
```

- **细粒度**：每个方法对应一个独立 Skill
- **可单独调用**：每个 Skill 都可通过 `from skills.<category> import <skill_name>` 单独使用
- **文档齐全**：每个 Skill 都有对应的 `SKILL.md` 详细说明

---

## 统计

- 总计：**73 个 Skill**，涵盖 12 个分类
- 各分类 Skill 数量：
  - Excel：7
  - File：9
  - Finance：1
  - Image：9
  - Markdown：1
  - OCR：1
  - PDF：13
  - PPT：3
  - Tools：10
  - Video：4
  - WeChat：7
  - Word：5
  - Ruiming：3
