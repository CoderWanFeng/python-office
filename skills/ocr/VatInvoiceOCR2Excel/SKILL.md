---
name: VatInvoiceOCR2Excel
description: 用 OCR 技术识别增值税发票图片并导出到 Excel，支持批量处理和翻译。当用户提到发票识别、增值税发票 OCR、电子发票识别、发票汇总时使用。
---

# VatInvoiceOCR2Excel Skill

> 使用 OCR 技术将增值税发票信息提取并导出到 Excel 文件

## 功能描述

使用光学字符识别（OCR）技术识别增值税发票图片中的信息，并将结果导出到 Excel 文件中。支持批量处理多个发票图片。

## 所属分类

`office/skills/ocr/VatInvoiceOCR2Excel/`

## 调用方式

```python
from skills.ocr import VatInvoiceOCR2Excel

VatInvoiceOCR2Excel(
    input_path='./invoices',
    output_path='./',
    output_excel='invoices.xlsx',
    id='your_baidu_id',
    key='your_baidu_key'
)
```

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_path` | str | 是 | - | 发票图片文件路径或包含多个发票图片的文件夹路径 |
| `output_path` | str | 否 | `'./'` | 输出 Excel 文件的文件夹路径 |
| `output_excel` | str | 否 | `'VatInvoiceOCR2Excel.xlsx'` | 输出 Excel 文件的名称 |
| `img_url` | str | 否 | `None` | 网络发票图片的 URL。如果提供了 input_path，则此参数将被忽略 |
| `id` | str | 否 | `None` | 百度 OCR API 的识别 ID |
| `key` | str | 否 | `None` | 百度 OCR API 的密钥 |
| `file_name` | bool | 否 | `False` | 是否使用图片文件名作为 Sheet 名称 |
| `trans` | bool | 否 | `False` | 是否将识别结果翻译成英文 |

## 返回值

`None`：函数将结果直接写入到指定的 Excel 文件中

## 使用示例

```python
from skills.ocr import VatInvoiceOCR2Excel
VatInvoiceOCR2Excel(input_path='./发票图片', output_excel='所有发票汇总.xlsx')
```

## 原始函数

`office.api.ocr.VatInvoiceOCR2Excel`
