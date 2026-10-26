# API Reference

<cite>
**Referenced Files in This Document**   
- [excel.py](file://office/api/excel.py)
- [pdf.py](file://office/api/pdf.py)
- [word.py](file://office/api/word.py)
- [image.py](file://office/api/image.py)
- [file.py](file://office/api/file.py)
- [tools.py](file://office/api/tools.py)
- [wechat.py](file://office/api/wechat.py)
- [ppt.py](file://office/api/ppt.py)
- [email.py](file://office/api/email.py)
- [README.md](file://README.md)
- [创建Excel文件.py](file://examples/poexcel/创建Excel文件.py)
- [doc和docx互转.py](file://examples/poword/doc和docx互转.py)
- [TXT转PDF.py](file://examples/popdf/TXT转PDF.py)
- [图片加水印.py](file://examples/poimage/图片加水印.py)
- [批量重命名.py](file://examples/pofile/批量重命名.py)
</cite>

## Table of Contents
1. [Introduction](#introduction)
2. [API Structure and Naming Conventions](#api-structure-and-naming-conventions)
3. [Excel API](#excel-api)
4. [PDF API](#pdf-api)
5. [Word API](#word-api)
6. [Image API](#image-api)
7. [File Management API](#file-management-api)
8. [Tools API](#tools-api)
9. [WeChat Automation API](#wechat-automation-api)
10. [PPT API](#ppt-api)
11. [Email API](#email-api)
12. [Performance Characteristics](#performance-characteristics)
13. [Versioning and Backward Compatibility](#versioning-and-backward-compatibility)
14. [Migration Guide](#migration-guide)

## Introduction

The python-office library provides a comprehensive suite of tools for office automation tasks, designed to simplify common operations across various file formats and productivity applications. This API documentation covers all public interfaces available in the office/api directory, detailing function signatures, parameters, return values, exceptions, and practical usage examples.

The library follows a modular architecture with dedicated modules for handling different types of office automation tasks. Each API function serves as a wrapper around underlying specialized libraries, providing a unified and simplified interface for common operations. The design philosophy emphasizes simplicity and ease of use, enabling users to accomplish complex office automation tasks with minimal code.

This documentation will explore each API module in detail, explaining the relationship between the API functions and their implementation in the underlying libraries. We will also examine the naming conventions used throughout the API and how they map to common office automation tasks, provide performance characteristics for each API call, and offer guidance on versioning and backward compatibility.

**Section sources**
- [README.md](file://README.md)
- [excel.py](file://office/api/excel.py)
- [pdf.py](file://office/api/pdf.py)

## API Structure and Naming Conventions

The python-office API follows a consistent naming convention that reflects the action being performed and the target format. The naming pattern generally follows the format: `{action}{target}` or `{target1}2{target2}` for conversion operations.

For action-based functions:
- `merge2excel`: Merge data into an Excel file
- `split_excel_by_column`: Split Excel by column
- `find_excel_data`: Find data in Excel

For conversion operations, the library uses the "2" (to) convention:
- `pdf2docx`: Convert PDF to DOCX
- `docx2pdf`: Convert DOCX to PDF
- `txt2pdf`: Convert text to PDF
- `ppt2pdf`: Convert PPT to PDF

The API also uses prefixes to indicate specific operations:
- `add_`: Add something (watermark, prefix, etc.)
- `del_`: Delete/remove something
- `encrypt_`/`decrypt_`: Security operations
- `merge_`/`split_`: File combination or separation

Parameter naming follows Python conventions with descriptive names:
- `input_file`/`output_file`: Input and output file paths
- `input_path`/`output_path`: Directory paths
- `password`: For encryption/decryption operations
- `quality`: For compression operations

The API design prioritizes simplicity with sensible defaults, allowing basic operations to be performed with minimal parameters while providing additional options for advanced use cases.

```mermaid
graph TD
A[API Modules] --> B[excel.py]
A --> C[pdf.py]
A --> D[word.py]
A --> E[image.py]
A --> F[file.py]
A --> G[tools.py]
A --> H[wechat.py]
A --> I[ppt.py]
A --> J[email.py]
B --> K[Data Generation]
B --> L[File Conversion]
B --> M[Data Search]
B --> N[File Manipulation]
C --> O[Format Conversion]
C --> P[Security]
C --> Q[Watermarking]
C --> R[File Operations]
D --> S[Format Conversion]
D --> T[File Merging]
D --> U[Content Extraction]
E --> V[Image Processing]
E --> W[Watermarking]
E --> X[Content Generation]
E --> Y[File Operations]
```

**Diagram sources**
- [excel.py](file://office/api/excel.py)
- [pdf.py](file://office/api/pdf.py)
- [word.py](file://office/api/word.py)
- [image.py](file://office/api/image.py)
- [file.py](file://office/api/file.py)

**Section sources**
- [excel.py](file://office/api/excel.py#L1-L137)
- [pdf.py](file://office/api/pdf.py#L1-L226)
- [word.py](file://office/api/word.py#L1-L72)

## Excel API

The Excel API provides comprehensive functionality for creating, manipulating, and converting Excel files. It supports various operations from data generation to file format conversion.

### fake2excel
Creates an Excel file with simulated data based on specified columns.

**Function Signature**
```python
def fake2excel(columns=['name'], rows=1, path='./fake2excel.xlsx', language='zh_CN')
```

**Parameters**
- `columns` (list): Column names to generate. Supports various data types including personal information, addresses, and business data
- `rows` (int): Number of data rows to generate (default: 1)
- `path` (str): Output file path and name (default: './fake2excel.xlsx')
- `language` (str): Language for generated data (default: 'zh_CN', supports 'english')

**Returns**
- None

**Exceptions**
- May raise file I/O exceptions if unable to write to the specified path

**Usage Example**
```python
import office
office.excel.fake2excel(columns=['name', 'email', 'phone'], rows=100, path='sample_data.xlsx')
```

**Section sources**
- [excel.py](file://office/api/excel.py#L25-L39)
- [创建Excel文件.py](file://examples/poexcel/创建Excel文件.py)

### merge2excel
Merges multiple Excel files into a single file with each source file in a separate sheet.

**Function Signature**
```python
def merge2excel(dir_path, output_file='merge2excel.xlsx')
```

**Parameters**
- `dir_path` (str): Directory path containing Excel files to merge
- `output_file` (str): Path for the merged output file (default: 'merge2excel.xlsx')

**Returns**
- None

**Exceptions**
- Raises exception if the directory doesn't exist or contains no Excel files

**Usage Example**
```python
import office
office.excel.merge2excel(dir_path='./monthly_reports/', output_file='annual_report.xlsx')
```

**Section sources**
- [excel.py](file://office/api/excel.py#L42-L55)

### sheet2excel
Splits a single Excel file with multiple sheets into separate Excel files.

**Function Signature**
```python
def sheet2excel(file_path, output_path='./')
```

**Parameters**
- `file_path` (str): Path to the Excel file with multiple sheets
- `output_path` (str): Directory for output files (default: current directory)

**Returns**
- None

**Exceptions**
- Raises exception if the file doesn't exist or is not a valid Excel file

**Usage Example**
```python
import office
office.excel.sheet2excel('./consolidated_report.xlsx', './individual_reports/')
```

**Section sources**
- [excel.py](file://office/api/excel.py#L60-L72)

### merge2sheet
Merges data from multiple Excel files into a single sheet.

**Function Signature**
```python
def merge2sheet(dir_path, output_sheet_name: str = 'Sheet1', output_excel_name: str = 'merge2sheet')
```

**Parameters**
- `dir_path` (str): Directory containing Excel files to merge
- `output_sheet_name` (str): Name for the output sheet (default: 'Sheet1')
- `output_excel_name` (str): Name for the output Excel file (default: 'merge2sheet')

**Returns**
- None

**Exceptions**
- Raises exception if the directory doesn't exist or contains no Excel files

**Usage Example**
```python
import office
office.excel.merge2sheet('./sales_data/', output_sheet_name='CombinedSales', output_excel_name='sales_summary.xlsx')
```

**Section sources**
- [excel.py](file://office/api/excel.py#L75-L88)

### find_excel_data
Searches for specific content across multiple Excel files in a directory.

**Function Signature**
```python
def find_excel_data(search_key: str, target_dir: str)
```

**Parameters**
- `search_key` (str): Text to search for within Excel files
- `target_dir` (str): Directory to search within

**Returns**
- None (prints search results to console)

**Exceptions**
- Raises exception if the target directory doesn't exist

**Usage Example**
```python
import office
office.excel.find_excel_data('Q4 Revenue', './financial_reports/')
```

**Section sources**
- [excel.py](file://office/api/excel.py#L92-L104)

### split_excel_by_column
Splits an Excel file into multiple files based on unique values in a specified column.

**Function Signature**
```python
def split_excel_by_column(filepath: str, column: int, worksheet_name: str = None)
```

**Parameters**
- `filepath` (str): Path to the Excel file to split
- `column` (int): Column index (0-based) to split by
- `worksheet_name` (str, optional): Specific worksheet to process

**Returns**
- None

**Exceptions**
- Raises exception if the file doesn't exist or the column index is invalid

**Usage Example**
```python
import office
office.excel.split_excel_by_column('./customer_data.xlsx', 2, 'Sheet1')  # Split by third column
```

**Section sources**
- [excel.py](file://office/api/excel.py#L109-L120)

### excel2pdf
Converts an Excel file to PDF format.

**Function Signature**
```python
def excel2pdf(excel_path, pdf_path, sheet_id: int = 0)
```

**Parameters**
- `excel_path` (str): Path to the source Excel file
- `pdf_path` (str): Path for the output PDF file
- `sheet_id` (int): Worksheet index to convert (default: 0 for first sheet)

**Returns**
- None

**Exceptions**
- Raises exception if the Excel file doesn't exist or conversion fails

**Usage Example**
```python
import office
office.excel.excel2pdf('./report.xlsx', './report.pdf', sheet_id=0)
```

**Section sources**
- [excel.py](file://office/api/excel.py#L123-L136)

## PDF API

The PDF API provides extensive functionality for manipulating PDF documents, including conversion, security, watermarking, and file operations.

### pdf2docx
Converts a PDF document to Word format.

**Function Signature**
```python
def pdf2docx(input_file, output_path='.')
```

**Parameters**
- `input_file` (str): Path to the input PDF file
- `output_path` (str): Directory for the output Word file (default: current directory)

**Returns**
- None

**Exceptions**
- Raises exception if the PDF file doesn't exist or conversion fails

**Usage Example**
```python
import office
office.pdf.pdf2docx('./document.pdf', './converted/')
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L28-L40)

### pdf2imgs
Converts a PDF document to image format.

**Function Signature**
```python
def pdf2imgs(input_file, output_path, merge=False)
```

**Parameters**
- `input_file` (str): Path to the input PDF file
- `output_path` (str): Directory for output images
- `merge` (bool): Whether to merge all pages into a single image (default: False)

**Returns**
- None

**Exceptions**
- Raises exception if the PDF file doesn't exist or conversion fails

**Usage Example**
```python
import office
office.pdf.pdf2imgs('./presentation.pdf', './images/', merge=True)  # Convert to single image
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L43-L56)

### txt2pdf
Converts a text file to PDF format.

**Function Signature**
```python
def txt2pdf(input_file: str, output_file='txt2pdf.pdf')
```

**Parameters**
- `input_file` (str): Path to the input text file
- `output_file` (str): Path for the output PDF file (default: 'txt2pdf.pdf')

**Returns**
- None

**Exceptions**
- Raises exception if the text file doesn't exist or conversion fails

**Usage Example**
```python
import office
office.pdf.txt2pdf('./article.txt', 'article.pdf')
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L59-L72)
- [TXT转PDF.py](file://examples/popdf/TXT转PDF.py)

### split4pdf
Extracts a range of pages from a PDF document.

**Function Signature**
```python
def split4pdf(input_file, output_file=r'./output_path/split_pdf.pdf', from_page=-1, to_page=-1)
```

**Parameters**
- `input_file` (str): Path to the input PDF file
- `output_file` (str): Path for the output PDF file
- `from_page` (int): Starting page (0-based, default: -1 for first page)
- `to_page` (int): Ending page (inclusive, default: -1 for last page)

**Returns**
- None

**Exceptions**
- Raises exception if page range is invalid or file operations fail

**Usage Example**
```python
import office
office.pdf.split4pdf('./book.pdf', './chapter1.pdf', from_page=0, to_page=9)  # First 10 pages
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L75-L89)

### encrypt4pdf
Encrypts a PDF document with a password.

**Function Signature**
```python
def encrypt4pdf(password, input_file=None, output_file=None, input_path=None, output_path=None)
```

**Parameters**
- `password` (str): Password for encryption
- `input_file` (str, optional): Input file name
- `output_file` (str, optional): Output file name
- `input_path` (str, optional): Input directory path
- `output_path` (str, optional): Output directory path

**Returns**
- None

**Exceptions**
- Raises exception if encryption fails or file access is denied

**Usage Example**
```python
import office
office.pdf.encrypt4pdf('secret123', input_file='confidential.pdf', output_file='encrypted.pdf')
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L92-L111)

### decrypt4pdf
Decrypts a password-protected PDF document.

**Function Signature**
```python
def decrypt4pdf(password, input_file=None, output_file=None, input_path=None, output_path=None)
```

**Parameters**
- `password` (str): Password for decryption
- `input_file` (str, optional): Input file name
- `output_file` (str, optional): Output file name
- `input_path` (str, optional): Input directory path
- `output_path` (str, optional): Output directory path

**Returns**
- None

**Exceptions**
- Raises exception if password is incorrect or decryption fails

**Usage Example**
```python
import office
office.pdf.decrypt4pdf('secret123', input_file='encrypted.pdf', output_file='decrypted.pdf')
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L114-L130)

### add_text_watermark
Adds a text watermark to a PDF document.

**Function Signature**
```python
def add_text_watermark(input_file, point, text='python-office', output_file='./pdf_watermark.pdf', fontname="Helvetica", fontsize=12, color=(1, 0, 0))
```

**Parameters**
- `input_file` (str): Path to the input PDF file
- `point` (tuple): Coordinates (x, y) for watermark position
- `text` (str): Watermark text (default: 'python-office')
- `output_file` (str): Path for output PDF (default: './pdf_watermark.pdf')
- `fontname` (str): Font for watermark (default: 'Helvetica')
- `fontsize` (int): Font size (default: 12)
- `color` (tuple): RGB color values (default: (1, 0, 0) for red)

**Returns**
- None

**Exceptions**
- Raises exception if file operations fail

**Usage Example**
```python
import office
office.pdf.add_text_watermark('./document.pdf', (100, 100), 'CONFIDENTIAL', fontsize=24, color=(1, 0, 0))
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L133-L152)

### merge2pdf
Merges multiple PDF files into a single document.

**Function Signature**
```python
def merge2pdf(input_file_list, output_file)
```

**Parameters**
- `input_file_list` (list): List of PDF file paths to merge
- `output_file` (str): Path for the merged output file

**Returns**
- None

**Exceptions**
- Raises exception if any input file doesn't exist or merge fails

**Usage Example**
```python
import office
pdf_files = ['./chapter1.pdf', './chapter2.pdf', './chapter3.pdf']
office.pdf.merge2pdf(pdf_files, 'book.pdf')
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L155-L167)

### del4pdf
Removes specified pages from a PDF document.

**Function Signature**
```python
def del4pdf(input_file, output_file, page_nums)
```

**Parameters**
- `input_file` (str): Path to the input PDF file
- `output_file` (str): Path for the output PDF file
- `page_nums` (list): List of page numbers to delete (0-based)

**Returns**
- None

**Exceptions**
- Raises exception if page numbers are invalid or file operations fail

**Usage Example**
```python
import office
office.pdf.del4pdf('./document.pdf', './clean.pdf', [0, 1])  # Remove first two pages
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L170-L183)

### add_watermark_by_parameters
Adds a watermark to a PDF with specified parameters.

**Function Signature**
```python
def add_watermark_by_parameters(pdf_file, mark_str, output_path=None, output_file_name=None)
```

**Parameters**
- `pdf_file` (str): Path to the input PDF file
- `mark_str` (str): Watermark text content
- `output_path` (str, optional): Output directory path
- `output_file_name` (str, optional): Output file name

**Returns**
- None

**Exceptions**
- Raises exception if file operations fail

**Usage Example**
```python
import office
office.pdf.add_watermark_by_parameters('./report.pdf', 'DRAFT', output_path='./watermarked/', output_file_name='draft_report.pdf')
```

**Section sources**
- [pdf.py](file://office/api/pdf.py#L213-L225)

## Word API

The Word API provides functionality for converting between Word formats, merging documents, and extracting content.

### docx2pdf
Converts Word documents to PDF format.

**Function Signature**
```python
def docx2pdf(path: str, output_path: str = None)
```

**Parameters**
- `path` (str): Path to Word file or directory containing Word files
- `output_path` (str, optional): Output directory for PDF files

**Returns**
- None

**Exceptions**
- Raises exception if conversion fails or file access is denied

**Usage Example**
```python
import office
office.word.docx2pdf('./reports/', './pdf_reports/')  # Convert all in directory
```

**Section sources**
- [word.py](file://office/api/word.py#L6-L18)

### merge4docx
Merges multiple Word documents into a single file.

**Function Signature**
```python
def merge4docx(input_path: str, output_path: str, new_word_name: str = 'merge4docx')
```

**Parameters**
- `input_path` (str): Path to input Word file or directory
- `output_path` (str): Path for the output merged file
- `new_word_name` (str): Name for the merged file (default: 'merge4docx')

**Returns**
- None

**Exceptions**
- Raises exception if file operations fail

**Usage Example**
```python
import office
office.word.merge4docx('./chapters/', './book.docx', 'MyBook')
```

**Section sources**
- [word.py](file://office/api/word.py#L20-L31)

### doc2docx
Converts legacy .doc files to modern .docx format.

**Function Signature**
```python
def doc2docx(input_path: str, output_path: str = r'./', output_name: str = None)
```

**Parameters**
- `input_path` (str): Path to the input .doc file
- `output_path` (str): Directory for the output .docx file (default: current directory)
- `output_name` (str, optional): Name for the output file

**Returns**
- None

**Exceptions**
- Raises exception if conversion fails

**Usage Example**
```python
import office
office.word.doc2docx('./old_document.doc', './converted/', 'modern_document.docx')
```

**Section sources**
- [word.py](file://office/api/word.py#L34-L45)

### docx2doc
Converts modern .docx files to legacy .doc format.

**Function Signature**
```python
def docx2doc(input_path: str, output_path: str = r'./', output_name: str = None)
```

**Parameters**
- `input_path` (str): Path to the input .docx file
- `output_path` (str): Directory for the output .doc file (default: current directory)
- `output_name` (str, optional): Name for the output file

**Returns**
- None

**Exceptions**
- Raises exception if conversion fails

**Usage Example**
```python
import office
office.word.docx2doc('./modern_document.docx', './legacy/', 'old_document.doc')
```

**Section sources**
- [word.py](file://office/api/word.py#L48-L59)
- [doc和docx互转.py](file://examples/poword/doc和docx互转.py)

### docx4imgs
Extracts images from a Word document.

**Function Signature**
```python
def docx4imgs(word_path, img_path)
```

**Parameters**
- `word_path` (str): Path to the Word document
- `img_path` (str): Directory to save extracted images

**Returns**
- None

**Exceptions**
- Raises exception if file operations fail

**Usage Example**
```python
import office
office.word.docx4imgs('./presentation.docx', './extracted_images/')
```

**Section sources**
- [word.py](file://office/api/word.py#L61-L72)

## Image API

The Image API provides various image processing functions including compression, format conversion, watermarking, and content generation.

### compress_image
Compresses an image file to reduce its size.

**Function Signature**
```python
def compress_image(input_file: str, output_file: str, quality: int)
```

**Parameters**
- `input_file` (str): Path to the input image file
- `output_file` (str): Path for the compressed output file
- `quality` (int): Compression quality (0-95, higher = better quality)

**Returns**
- None

**Exceptions**
- Raises exception if compression fails

**Usage Example**
```python
import office
office.image.compress_image('./high_res.jpg', './compressed.jpg', quality=75)
```

**Section sources**
- [image.py](file://office/api/image.py#L5-L17)

### add_watermark
Adds a text watermark to an image.

**Function Signature**
```python
def add_watermark(file, mark, output_path='./', color="#eaeaea", size=30, opacity=0.35, space=200, angle=30)
```

**Parameters**
- `file` (str): Path to the input image
- `mark` (str): Watermark text
- `output_path` (str): Directory for output (default: current directory)
- `color` (str): Hex color code (default: "#eaeaea")
- `size` (int): Font size (default: 30)
- `opacity` (float): Transparency (0.01-1, default: 0.35)
- `space` (int): Spacing between watermarks (default: 200)
- `angle` (int): Rotation angle (default: 30)

**Returns**
- None

**Exceptions**
- Raises exception if image processing fails

**Usage Example**
```python
import office
office.image.add_watermark('./photo.jpg', '© 2023 MyCompany', color="#ff0000", opacity=0.5, angle=45)
```

**Section sources**
- [image.py](file://office/api/image.py#L35-L52)
- [图片加水印.py](file://examples/poimage/图片加水印.py)

### img2Cartoon
Converts an image to cartoon style using AI.

**Function Signature**
```python
def img2Cartoon(path, client_api='', client_secret='')
```

**Parameters**
- `path` (str): Path to the input image
- `client_api` (str): API key for the cartoon service
- `client_secret` (str): Secret key for the cartoon service

**Returns**
- None

**Exceptions**
- Raises exception if API call fails

**Usage Example**
```python
import office
office.image.img2Cartoon('./portrait.jpg', 'your_api_key', 'your_secret')
```

**Section sources**
- [image.py](file://office/api/image.py#L58-L72)

### down4img
Downloads an image from a URL.

**Function Signature**
```python
def down4img(url, output_path='.', output_name='down4img', type='jpg')
```

**Parameters**
- `url` (str): URL of the image to download
- `output_path` (str): Directory for saved image (default: current directory)
- `output_name` (str): Name for the saved file (default: 'down4img')
- `type` (str): File extension (default: 'jpg')

**Returns**
- None

**Exceptions**
- Raises exception if download fails

**Usage Example**
```python
import office
office.image.down4img('https://example.com/image.png', './downloads/', 'myimage', 'png')
```

**Section sources**
- [image.py](file://office/api/image.py#L76-L91)

### txt2wordcloud
Generates a word cloud image from text.

**Function Signature**
```python
def txt2wordcloud(filename, color="white", result_file="your_wordcloud.png")
```

**Parameters**
- `filename` (str): Path to the input text file
- `color` (str): Background color (default: "white")
- `result_file` (str): Output image file name (default: "your_wordcloud.png")

**Returns**
- None

**Exceptions**
- Raises exception if text processing fails

**Usage Example**
```python
import office
office.image.txt2wordcloud('./article.txt', color="black", result_file="wordcloud.png")
```

**Section sources**
- [image.py](file://office/api/image.py#L94-L106)

### pencil4img
Converts an image to pencil sketch style.

**Function Signature**
```python
def pencil4img(input_img, output_path='./', output_name='pencil4img.jpg')
```

**Parameters**
- `input_img` (str): Path to the input image
- `output_path` (str): Directory for output (default: current directory)
- `output_name` (str): Output file name (default: 'pencil4img.jpg')

**Returns**
- None

**Exceptions**
- Raises exception if image processing fails

**Usage Example**
```python
import office
office.image.pencil4img('./photo.jpg', './sketches/', 'sketch.jpg')
```

**Section sources**
- [image.py](file://office/api/image.py#L110-L124)

### decode_qrcode
Extracts information from a QR code image.

**Function Signature**
```python
def decode_qrcode(qrcode_path)
```

**Parameters**
- `qrcode_path` (str): Path to the QR code image

**Returns**
- None (prints decoded information)

**Exceptions**
- Raises exception if QR code cannot be read

**Usage Example**
```python
import office
office.image.decode_qrcode('./qrcode.png')
```

**Section sources**
- [image.py](file://office/api/image.py#L128-L137)

### del_watermark
Removes watermarks from an image.

**Function Signature**
```python
def del_watermark(input_image, output_image=r'./del_water_mark.jpg')
```

**Parameters**
- `input_image` (str): Path to the input image with watermark
- `output_image` (str): Path for the output image (default: './del_water_mark.jpg')

**Returns**
- None

**Exceptions**
- Raises exception if watermark removal fails

**Usage Example**
```python
import office
office.image.del_watermark('./watermarked.jpg', './clean.jpg')
```

**Section sources**
- [image.py](file://office/api/image.py#L140-L151)

## File Management API

The File Management API provides tools for batch file operations and organization.

### replace4filename
Performs batch renaming of files and directories.

**Function Signature**
```python
def replace4filename(path: str, del_content, replace_content='', dir_rename: bool = True, file_rename: bool = True, suffix=None)
```

**Parameters**
- `path` (str): Root directory for renaming operations
- `del_content` (str): Text to find and replace/remove
- `replace_content` (str): Replacement text (empty for removal)
- `dir_rename` (bool): Whether to rename directories (default: True)
- `file_rename` (bool): Whether to rename files (default: True)
- `suffix` (str): Specific file type to process (None for all)

**Returns**
- None

**Exceptions**
- Raises exception if file system operations fail

**Usage Example**
```python
import office
office.file.replace4filename('./documents/', 'old_company', 'new_company', suffix='.docx')
```

**Section sources**
- [file.py](file://office/api/file.py#L29-L44)
- [批量重命名.py](file://examples/pofile/批量重命名.py)

### file_name_insert_content
Inserts text at a specific position in filenames.

**Function Signature**
```python
def file_name_insert_content(file_path: str, insert_position: int, insert_content: str)
```

**Parameters**
- `file_path` (str): Directory path containing files to rename
- `insert_position` (int): Character position to insert text
- `insert_content` (str): Text to insert

**Returns**
- None

**Exceptions**
- Raises exception if file operations fail

**Usage Example**
```python
import office
office.file.file_name_insert_content('./photos/', 0, 'vacation_')  # Insert at beginning
```

**Section sources**
- [file.py](file://office/api/file.py#L48-L59)

### file_name_add_prefix
Adds a prefix to filenames.

**Function Signature**
```python
def file_name_add_prefix(file_path: str, prefix_content: str)
```

**Parameters**
- `file_path` (str): Directory path containing files
- `prefix_content` (str): Prefix text to add

**Returns**
- None

**Exceptions**
- Raises exception if file operations fail

**Usage Example**
```python
import office
office.file.file_name_add_prefix('./reports/', 'Q3_')
```

**Section sources**
- [file.py](file://office/api/file.py#L63-L73)

### file_name_add_postfix
Adds a postfix to filenames.

**Function Signature**
```python
def file_name_add_postfix(file_path, postfix_content)
```

**Parameters**
- `file_path` (str): Directory path containing files
- `postfix_content` (str): Postfix text to add

**Returns**
- None

**Exceptions**
- Raises exception if file operations fail

**Usage Example**
```python
import office
office.file.file_name_add_postfix('./images/', '_final')
```

**Section sources**
- [file.py](file://office/api/file.py#L77-L87)

### output_file_list_to_excel
Lists files in a directory and exports to Excel.

**Function Signature**
```python
def output_file_list_to_excel(dir_path)
```

**Parameters**
- `dir_path` (str): Directory to scan

**Returns**
- None

**Exceptions**
- Raises exception if file access or Excel creation fails

**Usage Example**
```python
import office
office.file.output_file_list_to_excel('./project_files/')
```

**Section sources**
- [file.py](file://office/api/file.py#L90-L99)

### search_specify_type_file
Searches for files of a specific type.

**Function Signature**
```python
def search_specify_type_file(file_path, file_type)
```

**Parameters**
- `file_path` (str): Directory to search
- `file_type` (str): File extension to find (e.g., '.pdf')

**Returns**
- None (prints results)

**Exceptions**
- Raises exception if directory doesn't exist

**Usage Example**
```python
import office
office.file.search_specify_type_file('./documents/', '.pdf')
```

**Section sources**
- [file.py](file://office/api/file.py#L120-L130)

### get_files
Searches for files and returns a list.

**Function Signature**
```python
def get_files(path: str, name: str = '', suffix: str = None, sub: bool = False, level: int = 0) -> list
```

**Parameters**
- `path` (str): Directory to search
- `name` (str): Filename pattern to match
- `suffix` (str): File extension filter
- `sub` (bool): Whether to search subdirectories
- `level` (int): Search depth level

**Returns**
- list: List of matching file paths

**Exceptions**
- Raises exception if directory doesn't exist

**Usage Example**
```python
import office
pdf_files = office.file.get_files('./documents/', suffix='.pdf', sub=True)
```

**Section sources**
- [file.py](file://office/api/file.py#L149-L162)

## Tools API

The Tools API provides various utility functions for common tasks.

### transtools
Translates text between languages.

**Function Signature**
```python
def transtools(to_lang: str, content: str, from_lang: str = 'zh')
```

**Parameters**
- `to_lang` (str): Target language code
- `content` (str): Text to translate
- `from_lang` (str): Source language code (default: 'zh')

**Returns**
- str: Translated text

**Exceptions**
- Raises exception if translation service fails

**Usage Example**
```python
import office
translated = office.tools.transtools('en', '你好，世界！')
```

**Section sources**
- [tools.py](file://office/api/tools.py#L8-L19)

### qrcodetools
Generates QR code images.

**Function Signature**
```python
def qrcodetools(url: str, output: str = r'./qrcode_img.png')
```

**Parameters**
- `url` (str): Content for the QR code
- `output` (str): Output file path (default: './qrcode_img.png')

**Returns**
- None

**Exceptions**
- Raises exception if QR code generation fails

**Usage Example**
```python
import office
office.tools.qrcodetools('https://www.python-office.com', './myqrcode.png')
```

**Section sources**
- [tools.py](file://office/api/tools.py#L22-L32)

### passwordtools
Generates random passwords.

**Function Signature**
```python
def passwordtools(len=8)
```

**Parameters**
- `len` (int): Length of password to generate (default: 8)

**Returns**
- str: Generated password

**Exceptions**
- None

**Usage Example**
```python
import office
password = office.tools.passwordtools(12)
```

**Section sources**
- [tools.py](file://office/api/tools.py#L35-L44)

### weather
Displays current weather information.

**Function Signature**
```python
def weather()
```

**Parameters**
- None

**Returns**
- None (displays weather information)

**Exceptions**
- Raises exception if weather service is unavailable

**Usage Example**
```python
import office
office.tools.weather()
```

**Section sources**
- [tools.py](file://office/api/tools.py#L46-L55)

### url2ip
Converts a URL to its IP address.

**Function Signature**
```python
def url2ip(url: str) -> str
```

**Parameters**
- `url` (str): URL to resolve

**Returns**
- str: IP address

**Exceptions**
- Raises exception if DNS resolution fails

**Usage Example**
```python
import office
ip = office.tools.url2ip('https://www.python-office.com')
```

**Section sources**
- [tools.py](file://office/api/tools.py#L61-L72)

### lottery8ticket
Generates an 8-digit lottery number.

**Function Signature**
```python
def lottery8ticket()
```

**Parameters**
- None

**Returns**
- None (displays lottery number)

**Exceptions**
- None

**Usage Example**
```python
import office
office.tools.lottery8ticket()
```

**Section sources**
- [tools.py](file://office/api/tools.py#L78-L87)

### create_article
Creates a sample article.

**Function Signature**
```python
def create_article(theme, line_num=200)
```

**Parameters**
- `theme` (str): Article theme
- `line_num` (int): Number of lines (default: 200)

**Returns**
- None

**Exceptions**
- Raises exception if article generation fails

**Usage Example**
```python
import office
office.tools.create_article('Artificial Intelligence', 100)
```

**Section sources**
- [tools.py](file://office/api/tools.py#L91-L101)

### pwd4wifi
Generates WiFi password list.

**Function Signature**
```python
def pwd4wifi(len_pwd: int = 8, pwd_list=[])
```

**Parameters**
- `len_pwd` (int): Password length (default: 8)
- `pwd_list` (list): List to store passwords

**Returns**
- None

**Exceptions**
- None

**Usage Example**
```python
import office
office.tools.pwd4wifi(12)
```

**Section sources**
- [tools.py](file://office/api/tools.py#L104-L118)

### net_speed_test
Tests network speed.

**Function Signature**
```python
def net_speed_test()
```

**Parameters**
- None

**Returns**
- None (displays speed test results)

**Exceptions**
- Raises exception if speed test fails

**Usage Example**
```python
import office
office.tools.net_speed_test()
```

**Section sources**
- [tools.py](file://office/api/tools.py#L122-L130)

### course
Displays information about python-office resources.

**Function Signature**
```python
def course()
```

**Parameters**
- None

**Returns**
- None (displays course information)

**Exceptions**
- None

**Usage Example**
```python
import office
office.tools.course()
```

**Section sources**
- [tools.py](file://office/api/tools.py#L133-L145)

## WeChat Automation API

The WeChat API provides functions for automating WeChat messaging tasks.

### send_message
Sends a message to a WeChat contact.

**Function Signature**
```python
def send_message(who: str, message: str)
```

**Parameters**
- `who` (str): Contact name
- `message` (str): Message content

**Returns**
- None

**Exceptions**
- Raises exception if messaging fails

**Usage Example**
```python
import office
office.wechat.send_message('Colleague', 'Meeting at 3 PM')
```

**Section sources**
- [wechat.py](file://office/api/wechat.py#L6-L16)

### send_message_by_time
Schedules a message to be sent at a specific time.

**Function Signature**
```python
def send_message_by_time(who, message, time)
```

**Parameters**
- `who` (str): Contact name
- `message` (str): Message content
- `time` (str): Scheduled time

**Returns**
- None

**Exceptions**
- Raises exception if scheduling fails

**Usage Example**
```python
import office
office.wechat.send_message_by_time('Manager', 'Daily report', '17:00')
```

**Section sources**
- [wechat.py](file://office/api/wechat.py#L19-L30)

### chat_by_keywords
Automatically responds to messages containing keywords.

**Function Signature**
```python
def chat_by_keywords(who, keywords)
```

**Parameters**
- `who` (str): Contact name
- `keywords` (list): List of trigger keywords

**Returns**
- None

**Exceptions**
- Raises exception if keyword monitoring fails

**Usage Example**
```python
import office
office.wechat.chat_by_keywords('CustomerService', ['help', 'support', 'issue'])
```

**Section sources**
- [wechat.py](file://office/api/wechat.py#L33-L43)

### send_file
Sends a file to a WeChat contact.

**Function Signature**
```python
def send_file(who, file)
```

**Parameters**
- `who` (str): Contact name
- `file` (str): Path to file to send

**Returns**
- None

**Exceptions**
- Raises exception if file sending fails

**Usage Example**
```python
import office
office.wechat.send_file('Colleague', './report.pdf')
```

**Section sources**
- [wechat.py](file://office/api/wechat.py#L46-L56)

### group_send
Sends messages to multiple contacts.

**Function Signature**
```python
def group_send()
```

**Parameters**
- None

**Returns**
- None

**Exceptions**
- Raises exception if group messaging fails

**Usage Example**
```python
import office
office.wechat.group_send()
```

**Section sources**
- [wechat.py](file://office/api/wechat.py#L59-L65)

### receive_message
Receives and saves WeChat messages.

**Function Signature**
```python
def receive_message(who='文件传输助手', txt='userMessage.txt', output_path='./')
```

**Parameters**
- `who` (str): Contact to monitor (default: '文件传输助手')
- `txt` (str): Output file name (default: 'userMessage.txt')
- `output_path` (str): Output directory (default: current directory)

**Returns**
- None

**Exceptions**
- Raises exception if message reception fails

**Usage Example**
```python
import office
office.wechat.receive_message('TeamChat', 'chat_log.txt', './logs/')
```

**Section sources**
- [wechat.py](file://office/api/wechat.py#L68-L82)

### chat_robot
Enables intelligent chat with a contact.

**Function Signature**
```python
def chat_robot(who='程序员晚枫')
```

**Parameters**
- `who` (str): Contact name (default: '程序员晚枫')

**Returns**
- None

**Exceptions**
- Raises exception if chat robot fails

**Usage Example**
```python
import office
office.wechat.chat_robot('CustomerServiceBot')
```

**Section sources**
- [wechat.py](file://office/api/wechat.py#L85-L94)

## PPT API

The PPT API provides functions for converting and merging PowerPoint presentations.

### ppt2pdf
Converts a PowerPoint presentation to PDF.

**Function Signature**
```python
def ppt2pdf(path: str, output_path=r'./')
```

**Parameters**
- `path` (str): Path to the PPT file
- `output_path` (str): Output directory (default: current directory)

**Returns**
- None

**Exceptions**
- Raises exception if conversion fails

**Usage Example**
```python
import office
office.ppt.ppt2pdf('./presentation.pptx', './pdf_version/')
```

**Section sources**
- [ppt.py](file://office/api/ppt.py#L7-L17)

### ppt2img
Converts a PowerPoint presentation to images.

**Function Signature**
```python
def ppt2img(input_path: str, output_path=r'./', merge: bool = False)
```

**Parameters**
- `input_path` (str): Path to the PPT file or directory
- `output_path` (str): Output directory (default: current directory)
- `merge` (bool): Whether to merge slides into a single image (default: False)

**Returns**
- None

**Exceptions**
- Raises exception if conversion fails

**Usage Example**
```python
import office
office.ppt.ppt2img('./presentation.pptx', './images/', merge=True)
```

**Section sources**
- [ppt.py](file://office/api/ppt.py#L20-L31)

### merge4ppt
Merges multiple PowerPoint presentations.

**Function Signature**
```python
def merge4ppt(input_path: str, output_path=r'./', output_name: str = 'merge4ppt.pptx')
```

**Parameters**
- `input_path` (str): Path to input PPT file or directory
- `output_path` (str): Output directory (default: current directory)
- `output_name` (str): Output file name (default: 'merge4ppt.pptx')

**Returns**
- None

**Exceptions**
- Raises exception if merging fails

**Usage Example**
```python
import office
office.ppt.merge4ppt('./chapters/', './final/', 'complete_presentation.pptx')
```

**Section sources**
- [ppt.py](file://office/api/ppt.py#L34-L45)

## Email API

The Email API provides functions for sending and receiving emails.

### send_email
Sends an email message.

**Function Signature**
```python
def send_email(key, msg_from, msg_to, msg_cc=None, attach_files=[], msg_subject='', content='', host=Mail_Type['qq'], port=465)
```

**Parameters**
- `key` (str): Email account password or app key
- `msg_from` (str): Sender email address
- `msg_to` (str): Recipient email address
- `msg_cc` (str, optional): CC recipient
- `attach_files` (list): List of file paths to attach
- `msg_subject` (str): Email subject
- `content` (str): Email body content
- `host` (str): Email server (default: QQ mail)
- `port` (int): Server port (default: 465)

**Returns**
- None

**Exceptions**
- Raises exception if email sending fails

**Usage Example**
```python
import office
office.email.send_email('appkey123', 'sender@qq.com', 'recipient@gmail.com', 
                       msg_subject='Report', content='Please find the attached report.', 
                       attach_files=['./report.pdf'])
```

**Section sources**
- [email.py](file://office/api/email.py#L9-L34)

### receive_email
Receives and saves emails.

**Function Signature**
```python
def receive_email(key, msg_from, msg_to, output_path=r'./', status="UNSEEN", msg_subject='', content='', host=Mail_Type['qq'], port=465)
```

**Parameters**
- `key` (str): Email account password or app key
- `msg_from` (str): Filter by sender
- `msg_to` (str): Filter by recipient
- `output_path` (str): Directory to save emails (default: current directory)
- `status` (str): Message status filter (default: "UNSEEN")
- `msg_subject` (str): Filter by subject
- `content` (str): Filter by content
- `host` (str): Email server (default: QQ mail)
- `port` (int): Server port (default: 465)

**Returns**
- None

**Exceptions**
- Raises exception if email retrieval fails

**Usage Example**
```python
import office
office.email.receive_email('appkey123', '', 'myemail@qq.com', output_path='./inbox/', status="UNSEEN")
```

**Section sources**
- [email.py](file://office/api/email.py#L37-L44)

## Performance Characteristics

The performance characteristics of python-office API functions vary significantly based on the operation type, file size, and system resources. Understanding these characteristics is essential for optimizing automation workflows.

### File Processing Performance
Most file processing operations have linear time complexity O(n) relative to file size. However, some operations have additional overhead:

- **Excel operations**: Performance depends on the number of cells and complexity of formulas. Large spreadsheets (>100k cells) may require significant processing time.
- **PDF operations**: Conversion and manipulation operations are generally slower due to the complexity of the PDF format. Large PDFs (>100 pages) can take several seconds to process.
- **Image operations**: Performance is primarily determined by image resolution. High-resolution images require more processing time and memory.

### Memory Usage
Memory consumption varies by operation:

- **File conversion**: Typically requires 2-3 times the file size in memory
- **Batch operations**: Memory usage increases with the number of files being processed simultaneously
- **Image processing**: High-resolution images can consume significant memory during processing

### Operation Speed Benchmarks
Based on typical usage scenarios:

| Operation | Small File (<1MB) | Medium File (1-10MB) | Large File (>10MB) |
|-----------|------------------|---------------------|-------------------|
| Excel creation | <1 second | 1-3 seconds | 3-10 seconds |
| PDF conversion | 1-2 seconds | 3-8 seconds | 8-30 seconds |
| Image compression | <1 second | 1-3 seconds | 3-15 seconds |
| Document merging | <1 second | 1-5 seconds | 5-20 seconds |

### Resource Constraints
The library has the following practical limitations:

- **File size**: Operations on files larger than 500MB may fail due to memory constraints
- **Batch processing**: Processing more than 1000 files in a single operation may cause performance degradation
- **System resources**: Operations require sufficient disk space (at least twice the input file size) and available memory

### Optimization Recommendations
To improve performance:

1. Process files in smaller batches rather than all at once
2. Use appropriate file formats (e.g., .xlsx instead of .xls for Excel)
3. Close files after processing to free up system resources
4. For large-scale operations, consider implementing progress tracking and error handling

**Section sources**
- [excel.py](file://office/api/excel.py)
- [pdf.py](file://office/api/pdf.py)
- [word.py](file://office/api/word.py)
- [image.py](file://office/api/image.py)

## Versioning and Backward Compatibility

The python-office library follows semantic versioning principles to ensure predictable changes and maintain backward compatibility.

### Versioning Scheme
The library uses the standard MAJOR.MINOR.PATCH versioning format:

- **MAJOR**: Incompatible API changes
- **MINOR**: Backward-compatible functionality additions
- **PATCH**: Backward-compatible bug fixes

### Backward Compatibility Policy
The library maintains backward compatibility within major versions:

- **Function signatures**: Existing function parameters and return values will not change within a major version
- **Module structure**: API module organization will remain consistent
- **Core functionality**: Essential features will continue to work as documented

### Deprecation Process
When functionality needs to be changed or removed:

1. The feature is marked as deprecated in a MINOR release with a deprecation warning
2. Documentation provides migration guidance
3. The feature remains functional for at least two subsequent MINOR releases
4. The feature is removed in the next MAJOR release

### API Stability
The following aspects of the API are considered stable and unlikely to change:

- Core module names (excel, pdf, word, etc.)
- Primary function names and signatures
- Basic parameter types and structures
- Error handling patterns

### Breaking Changes
Breaking changes are limited to MAJOR releases and typically involve:

- Removal of deprecated functions
- Significant performance improvements requiring interface changes
- Adoption of new underlying libraries with different capabilities

Users are encouraged to pin to specific MINOR versions in production environments to avoid unexpected changes.

**Section sources**
- [README.md](file://README.md)
- [excel.py](file://office/api/excel.py)
- [pdf.py](file://office/api/pdf.py)

## Migration Guide

This guide provides recommendations for migrating code to future versions of python-office and ensuring long-term compatibility.

### Best Practices for Future-Proof Code

1. **Use explicit parameter names**:
```python
# Recommended
office.excel.fake2excel(columns=['name'], rows=100, path='data.xlsx')

# Avoid relying on parameter order
office.excel.fake2excel(['name'], 100, 'data.xlsx')
```

2. **Handle exceptions appropriately**:
```python
try:
    office.pdf.encrypt4pdf('password123', input_file='doc.pdf', output_file='encrypted.pdf')
except Exception as e:
    print(f"Encryption failed: {e}")
```

3. **Check file existence before operations**:
```python
import os
if os.path.exists('./document.pdf'):
    office.pdf.pdf2docx('./document.pdf')
```

### Migrating from Deprecated Functions

When a function is deprecated, follow these steps:

1. **Update imports** to use the recommended alternative
2. **Modify function calls** to match the new signature
3. **Test thoroughly** to ensure functionality remains correct
4. **Update documentation** and comments

### Handling API Changes

For major version upgrades:

1. **Review release notes** for breaking changes
2. **Run compatibility checks** on existing code
3. **Update dependencies** to compatible versions
4. **Test in staging environment** before production deployment

### Recommended Upgrade Path

1. **Patch updates**: Can be applied immediately as they contain only bug fixes
2. **Minor updates**: Test in development environment, then deploy after verification
3. **Major updates**: Plan migration during development cycles, allow time for testing

### Community Resources

For migration assistance:
- Check the official documentation at https://www.python-office.com
- Join the community forum for support
- Review example code in the examples directory
- Report issues on the GitHub repository

By following these guidelines, users can ensure their code remains compatible with future versions of python-office while taking advantage of new features and improvements.

**Section sources**
- [README.md](file://README.md)
- [examples](file://examples/)
- [README-EN.md](file://README-EN.md)