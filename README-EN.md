<p align="center">
    <a target="_blank" href='https://pypi.org/project/python-office/'>
    <img src="https://raw.atomgit.com/CoderWanFeng1/website/raw/main/github-nav.jpg" alt="python-office"/>
    </a>
</p>

<p align="center">
    👉 <a target="_blank" href="https://www.python-office.com/">Official Site</a> ·
    <a target="_blank" href="https://www.python4office.cn/wechat-group/">Community</a> ·
    <a target="_blank" href="https://www.python4office.cn/python-office/profile/">Documentation</a> ·
    <a target="_blank" href="https://www.python-office.com/video/video.html">Video Tutorials</a> 👈
</p>

<p align="center">
    <a href="https://github.com/CoderWanFeng/python-office/stargazers">
        <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="GitHub stars"/>
    </a>
    <a href="https://gitee.com/CoderWanFeng/python-office/stargazers">
        <img src='https://gitee.com/CoderWanFeng/python-office/badge/star.svg?theme=dark' alt='Gitee stars'/>
    </a>
    <a href="https://static.pepy.tech/badge/python-office">
        <img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads"/>
    </a>
    <a href="https://www.python-office.com/">
        <img src="https://img.shields.io/badge/python-3.7%2B-blue" alt="Python Version"/>
    </a>
    <a href="https://www.python4office.cn/wechat-group/">
        <img src="https://img.shields.io/badge/Join-AI%20Group-brightgreen" alt="AI Community"/>
    </a>
</p>

---

## 📚 Introduction

**python-office** is a Python third-party library focused on **office automation**.
Every feature is just **one line of code** — automate your office work without even learning Python.

> ✨ Features are continuously updated. Submit your feature requests → [Contact the developer](https://www.python4office.cn/wechat-qrcode/)

### 🍺 Why python-office?

| Feature | Description |
|---------|-------------|
| 🚀 **One-line code** | 90% of features require only a single line — zero learning curve |
| 🎯 **Scenario-driven** | Covers PDF, Word, Excel, PPT, Email, WeChat, Images, Video, and more real office tasks |
| 🧩 **Skills system** | 73 ready-to-use Skills, each independently importable |
| 🤖 **AI-friendly** | Complete `SKILL.md` + YAML metadata, directly recognizable by Codex / Claude / Cursor |
| 🛠️ **Modular** | `pip install popdf / poimage / poword ...` — install only what you need |
| 💬 **Beginner-friendly** | Full tutorials, video guides, and an active WeChat community |

---

## ✨ Skills System (73 ready-to-use Skills)

`python-office` ships with a built-in **Skill system**: the library's 73 methods are wrapped as 73 independently importable Skills, each with its own `SKILL.md` documentation.

```python
# Option 1: Import a specific Skill
from skills.image import compress_image
compress_image(input_file='photo.jpg', output_file='photo_small.jpg', quality=30)

# Option 2: Import by category
from skills.pdf import pdf2docx
pdf2docx(input_file='report.pdf', output_file='report.docx')
```

### 📋 13 Categories at a Glance

| Category | Skill Count | Typical Skills |
|----------|-------------|----------------|
| 📊 Excel | 7 | `fake2excel` / `merge2excel` / `excel2pdf` |
| 📁 File | 9 | `replace4filename` / `get_files` |
| 💰 Finance | 1 | `t0` (stock T+0 return calculator) |
| 🖼️ Image | 9 | `compress_image` / `add_watermark` / `txt2wordcloud` |
| 📝 Markdown | 1 | `excel2markdown` |
| 🔍 OCR | 1 | `VatInvoiceOCR2Excel` (VAT invoice recognition) |
| 📕 PDF | 13 | `pdf2docx` / `pdf2imgs` / `merge2pdf` / `encrypt4pdf` |
| 🎬 PPT | 3 | `ppt2pdf` / `ppt2img` / `merge4ppt` |
| 🛠️ Tools | 10 | `transtools` / `qrcodetools` / `passwordtools` |
| 🎥 Video | 4 | `video2mp3` / `audio2txt` / `txt2mp3` |
| 💬 WeChat | 7 | `send_message` / `chat_robot` / `receive_message` |
| 📄 Word | 5 | `docx2pdf` / `merge4docx` / `docx4imgs` |
| 🏷️ Ruiming | 3 | `screen_unmarked_image` / `change_label_in_xml` |

👉 Full index: [`skills/README.md`](./skills/README.md)

---

## 📦 Installation

```bash
# Install everything (recommended)
pip install -i https://mirrors.aliyun.com/pypi/simple/ python-office -U

# Install only what you need (lighter)
pip install popdf      # PDF processing only
pip install poimage    # Image processing only
pip install poword     # Word processing only
pip install poexcel    # Excel processing only
```

> Python version: **Python 3.7+**

---

## 🚀 5-line Quick Start

```python
# 1. PDF → Word
from skills.pdf import pdf2docx
pdf2docx(input_file='report.pdf', output_file='report.docx')

# 2. Compress an image
from skills.image import compress_image
compress_image(input_file='big.jpg', output_file='small.jpg', quality=30)

# 3. Add a watermark to an image
from skills.image import add_watermark
add_watermark(file='photo.jpg', mark='@python-office')

# 4. Generate a word cloud
from skills.image import txt2wordcloud
txt2wordcloud(filename='article.txt', result_file='wordcloud.png')

# 5. Generate a QR code
from skills.tools import qrcodetools
qrcodetools(url='https://www.python-office.com', output='qrcode.png')
```

---

## 🛠️ Components

Each feature is accessible via the traditional `import office` style, or directly from `skills.xxx`.

| Module | Description | Skills Path |
|--------|-------------|-------------|
| PyOfficeRobot | WeChat bot | `skills/wechat/` |
| poocr | OCR (invoice, table, image) | `skills/ocr/` |
| popdf | PDF → Word / image / split / merge / encrypt | `skills/pdf/` |
| poemail | Auto-send emails | `office/api/email.py` |
| porobot | AI bot | `office/api/tools.py` |
| poimage | Image compress / watermark / word cloud / filters | `skills/image/` |
| poai | AI utilities | `office/lib/` |
| poexcel | Excel merge / split / mock data | `skills/excel/` |
| poword | Word → PDF / extract images | `skills/word/` |
| pofile | Batch file rename / organize | `skills/file/` |
| search4file | Document search | `skills/file/` |
| poppt | PPT → PDF / image | `skills/ppt/` |
| wftools | Translation / QR code / password generator, etc. | `skills/tools/` |
| pofinance | Stock T+0 calculator | `skills/finance/` |
| pohan | Chinese programming | - |
| povideo | Video → audio / speech recognition | `skills/video/` |
| potime | Time utilities | - |
| poprogress | Progress bar utilities | - |
| pocode | Code management | - |

---

## 💡 Featured Skills

<details>
<summary>📊 <b>Excel Processing</b> (click to expand)</summary>

```python
from skills.excel import fake2excel
fake2excel(columns=['name', 'phone'], rows=1000, path='test.xlsx')

from skills.excel import merge2excel
merge2excel(dir_path='./my_excels', output_file='all.xlsx')
```
</details>

<details>
<summary>📕 <b>PDF Processing</b> (click to expand)</summary>

```python
from skills.pdf import pdf2docx       # PDF → Word
from skills.pdf import pdf2imgs        # PDF → images
from skills.pdf import merge2pdf       # Merge multiple PDFs
from skills.pdf import split4pdf       # Split a PDF
from skills.pdf import encrypt4pdf     # Encrypt a PDF
from skills.pdf import add_watermark_by_parameters  # PDF watermark
```
</details>

<details>
<summary>🖼️ <b>Image Processing</b> (click to expand)</summary>

```python
from skills.image import compress_image       # Compress images
from skills.image import add_watermark        # Add watermark
from skills.image import del_watermark        # Remove watermark
from skills.image import txt2wordcloud        # Generate word cloud
from skills.image import pencil4img           # Pencil-sketch style
from skills.image import img2Cartoon          # Cartoon style
from skills.image import decode_qrcode        # Decode QR code
```
</details>

<details>
<summary>💬 <b>WeChat Bot</b> (click to expand)</summary>

```python
from skills.wechat import send_message
send_message(who='File Transfer', message='Hello!')

from skills.wechat import send_message_by_time
send_message_by_time(who='File Transfer', message='Good morning', time='08:00:00')
```
</details>

<details>
<summary>🎬 <b>Video Processing</b> (click to expand)</summary>

```python
from skills.video import video2mp3       # Video → MP3
from skills.video import audio2txt       # Audio → text
from skills.video import txt2mp3         # Text → speech
from skills.video import mark2video      # Video watermark
```
</details>

---

## 📝 Documentation

- 📘 [Chinese Documentation](https://github.com/CoderWanFeng/python-office/tree/develop/.qoder/repowiki/zh/content)
- 📗 [English Documentation](https://github.com/CoderWanFeng/python-office/tree/develop/.qoder/repowiki/en/content)
- 🎬 [Video Tutorials](https://www.python-office.com/video/video.html)
- 🤖 [Skills Index](./skills/README.md)

---

## 🤝 Contributing

Contributions are welcome. Please submit your PR in a dedicated folder:

- Create a folder with your GitHub username under [contributors](./contributors/)
- Put all your code inside that folder
- **Do not modify any other folders**
- For questions about existing code, please open an issue

### Code Style

1. **Comments**: Document every parameter and return value of new functions
2. **Formatting**: Format only your own code
3. **Tests**: Unit tests are optional but strongly recommended
4. **Skills**: When adding a new method, also add a Skill wrapper under `skills/<category>/<method>/`

---

## 🐞 Bug Reports & Suggestions

Please only submit issues related to the python-office codebase itself. We don't answer general Python learning questions.

- [GitHub Issues](https://github.com/CoderWanFeng/python-office/issues)
- [Gitee Issues](https://gitee.com/CoderWanFeng/python-office/issues)
- [AtomGit Issues](https://atomgit.com/CoderWanFeng1/python-office/issues)

---

## ⭐ Star History

[![Stargazers over time](https://starchart.cc/CoderWanFeng/python-office.svg)](https://starchart.cc/CoderWanFeng/python-office)

---

## 📌 Contact the Author

<p align="center">
    <a target="_blank" href='https://www.python4office.cn/wechat-qrcode/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/c52fb12c-7cb7-4684-8a3e-020a4bec8888/f0501b73cd57eba391ab4fc5a6654669.jpg" width="60%"/>
    </a>
</p>

<p align="center">
    👉 <a target="_blank" href='https://www.python4office.cn/wechat-group/'>Join the open-source community</a> ·
    <a target="_blank" href='https://www.python4office.cn/wechat-qrcode/'>WeChat the author</a> 👈
</p>

---

<p align="center">
    <sub>If this project helps you, a ⭐ Star is the best encouragement!</sub>
</p>
