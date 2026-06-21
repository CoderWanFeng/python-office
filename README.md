<p align="center">
    <a target="_blank" href='https://pypi.org/project/python-office/'>
    <img src="https://raw.atomgit.com/CoderWanFeng1/website/raw/main/github-nav.jpg" alt="python-office"/>
    </a>
</p>

<p align="center">
    👉 <a target="_blank" href="https://www.python-office.com/">项目官网</a> ·
    <a target="_blank" href="https://www.python4office.cn/wechat-group/">交流群</a> ·
    <a target="_blank" href="https://www.python4office.cn/python-office/profile/">中文文档</a> ·
    <a target="_blank" href="https://www.python-office.com/video/video.html">视频教程</a> 👈
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
        <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群"/>
    </a>
</p>

---

## 📚 简介

**python-office** 是一个专注于**办公自动化**的 Python 第三方库。
每个功能只需 **一行代码** 即可完成，让你不学 Python 也能自动化办公。

> ✨ 功能持续更新中，欢迎提交你的功能需求 → [开发者微信](https://www.python4office.cn/wechat-qrcode/)

### 🍺 为什么选择 python-office？

| 特点 | 说明 |
|------|------|
| 🚀 **一行代码** | 90% 的功能只需要一行代码，零基础也能用 |
| 🎯 **场景驱动** | 覆盖 PDF、Word、Excel、PPT、邮件、微信、图片、视频等真实办公场景 |
| 🧩 **Skills 体系** | 内置 73 个开箱即用的 Skill，每个 Skill 独立可调用 |
| 🤖 **AI 友好** | 完整 `SKILL.md` + YAML 描述，可被 Codex / Claude / Cursor 等 AI 直接识别 |
| 🛠️ **可拆可合** | 按需 `pip install popdf / poimage / poword ...`，不冗余 |
| 💬 **中文友好** | 全中文文档、视频教程、微信答疑群 |

---

## ✨ Skills 体系（73 个开箱即用）

`python-office` 内置了一套 **Skill 体系**：把库里的 73 个方法封装成 73 个独立可调用的 Skill，
每个 Skill 有自己的 `SKILL.md` 文档，可以单独 import，也可以整体使用。

```bash
# 方式 1：直接调用具体 Skill
from skills.image import compress_image
compress_image(input_file='photo.jpg', output_file='photo_small.jpg', quality=30)

# 方式 2：按分类批量导入
from skills.pdf import pdf2docx
pdf2docx(input_file='report.pdf', output_file='report.docx')
```

### 📋 13 个分类速查表

| 分类 | Skill 数量 | 典型 Skill |
|------|----------|-----------|
| 📊 Excel | 7 | `fake2excel` / `merge2excel` / `excel2pdf` |
| 📁 File | 9 | `replace4filename` / `get_files` |
| 💰 Finance | 1 | `t0`（股票做 T 收益计算）|
| 🖼️ Image | 9 | `compress_image` / `add_watermark` / `txt2wordcloud` |
| 📝 Markdown | 1 | `excel2markdown` |
| 🔍 OCR | 1 | `VatInvoiceOCR2Excel`（增值税发票识别）|
| 📕 PDF | 13 | `pdf2docx` / `pdf2imgs` / `merge2pdf` / `encrypt4pdf` |
| 🎬 PPT | 3 | `ppt2pdf` / `ppt2img` / `merge4ppt` |
| 🛠️ Tools | 10 | `transtools` / `qrcodetools` / `passwordtools` |
| 🎥 Video | 4 | `video2mp3` / `audio2txt` / `txt2mp3` |
| 💬 WeChat | 7 | `send_message` / `chat_robot` / `receive_message` |
| 📄 Word | 5 | `docx2pdf` / `merge4docx` / `docx4imgs` |
| �️ Ruiming | 3 | `screen_unmarked_image` / `change_label_in_xml` |

👉 查看完整 Skill 索引：[`skills/README.md`](./skills/README.md)

---

## 📦 安装

```bash
# 一键安装（推荐）
pip install -i https://mirrors.aliyun.com/pypi/simple/ python-office -U

# 按需安装子库（更轻量）
pip install popdf      # 只用 PDF 处理
pip install poimage    # 只用图片处理
pip install poword     # 只用 Word 处理
pip install poexcel    # 只用 Excel 处理
```

> Python 版本要求：**Python 3.7+**

---

## � 5 行代码快速体验

```python
# 1. PDF 转 Word
from skills.pdf import pdf2docx
pdf2docx(input_file='report.pdf', output_file='report.docx')

# 2. 批量压缩图片
from skills.image import compress_image
compress_image(input_file='big.jpg', output_file='small.jpg', quality=30)

# 3. 给图片加水印
from skills.image import add_watermark
add_watermark(file='photo.jpg', mark='@python-office')

# 4. 文本生成词云
from skills.image import txt2wordcloud
txt2wordcloud(filename='article.txt', result_file='wordcloud.png')

# 5. 生成二维码
from skills.tools import qrcodetools
qrcodetools(url='https://www.python-office.com', output='qrcode.png')
```

---

## 🛠️ 功能分类

每个功能既支持传统的 `import office` 方式，也支持从 `skills.xxx` 单独调用。

| 模块 | 功能 | Skills 路径 |
|------|------|-------------|
| PyOfficeRobot | 微信机器人 | `skills/wechat/` |
| poocr | 文字识别（发票、表格、图片）| `skills/ocr/` |
| popdf | PDF 转 Word / 图片 / 拆分 / 合并 / 加密 | `skills/pdf/` |
| poemail | 自动发邮件 | `office/api/email.py` |
| porobot | AI 机器人 | `office/api/tools.py` |
| poimage | 图片压缩 / 水印 / 词云 / 滤镜 | `skills/image/` |
| poai | AI 工具集 | `office/lib/` |
| poexcel | Excel 合并 / 拆分 / 模拟数据 | `skills/excel/` |
| poword | Word 转 PDF / 提取图片 | `skills/word/` |
| pofile | 文件批量重命名 / 整理 | `skills/file/` |
| search4file | 文档搜索 | `skills/file/` |
| poppt | PPT 转 PDF / 图片 | `skills/ppt/` |
| wftools | 翻译 / 二维码 / 密码生成等小工具 | `skills/tools/` |
| pofinance | 股票做 T 计算 | `skills/finance/` |
| pohan | 中文编程 | - |
| povideo | 视频转音频 / 语音识别 | `skills/video/` |
| potime | 时间工具 | - |
| poprogress | 进度条工具 | - |
| pocode | 代码管理 | - |

---

## 💡 精选 Skill 一览

<details>
<summary>📊 <b>Excel 处理</b>（点击展开）</summary>

```python
from skills.excel import fake2excel
fake2excel(columns=['name', 'phone'], rows=1000, path='test.xlsx')

from skills.excel import merge2excel
merge2excel(dir_path='./my_excels', output_file='all.xlsx')
```
</details>

<details>
<summary>📕 <b>PDF 处理</b>（点击展开）</summary>

```python
from skills.pdf import pdf2docx       # PDF → Word
from skills.pdf import pdf2imgs        # PDF → 图片
from skills.pdf import merge2pdf       # 合并多个 PDF
from skills.pdf import split4pdf       # 拆分 PDF
from skills.pdf import encrypt4pdf     # 加密 PDF
from skills.pdf import add_watermark_by_parameters  # PDF 加水印
```
</details>

<details>
<summary>🖼️ <b>Image 图像处理</b>（点击展开）</summary>

```python
from skills.image import compress_image       # 压缩图片
from skills.image import add_watermark        # 加水印
from skills.image import del_watermark        # 去水印
from skills.image import txt2wordcloud        # 生成词云
from skills.image import pencil4img           # 转铅笔画
from skills.image import img2Cartoon          # 转卡通风格
from skills.image import decode_qrcode        # 解析二维码
```
</details>

<details>
<summary>💬 <b>微信机器人</b>（点击展开）</summary>

```python
from skills.wechat import send_message
send_message(who='文件传输助手', message='Hello!')

from skills.wechat import send_message_by_time
send_message_by_time(who='文件传输助手', message='早安', time='08:00:00')
```
</details>

<details>
<summary>🎬 <b>Video 视频处理</b>（点击展开）</summary>

```python
from skills.video import video2mp3       # 视频 → MP3
from skills.video import audio2txt       # 音频 → 文字
from skills.video import txt2mp3         # 文字 → 语音
from skills.video import mark2video      # 视频加文字水印
```
</details>

---

## 📝 文档

- � [中文文档](https://github.com/CoderWanFeng/python-office/tree/develop/.qoder/repowiki/zh/content)
- 📗 [English Document](https://github.com/CoderWanFeng/python-office/tree/develop/.qoder/repowiki/en/content)
- 🎬 [视频教程](https://www.python-office.com/video/video.html)
- 🤖 [Skills 索引](./skills/README.md)

---

## 🤝 贡献代码

python-office 欢迎任何人来添砖加瓦。建议提交的 PR 放在一个独立的文件夹下：

- 在 [contributors](./contributors/) 文件夹中，用自己的 GitHub 名字建一个文件夹；
- 把自己的所有代码，都提交到这个自己的文件夹里；
- **不要修改其它任何文件夹下的代码**；
- 对现有代码有疑问，可以直接提 issue。

### 代码风格

1. **注释**：请为每个新函数的参数、返回值添加说明
2. **格式**：只能格式化自己写的代码
3. **测试**：单元测试可选，但强烈推荐
4. **Skill**：新增方法时，建议同时在 `skills/<分类>/<方法名>/` 下加 Skill 封装

---

## 🐞 提供 Bug 反馈或建议

提交问题反馈时，请务必填写和 python-office 代码本身有关的问题，不进行 Python 学习或个人练习的答疑。

- [GitHub Issue](https://github.com/CoderWanFeng/python-office/issues)
- [Gitee Issue](https://gitee.com/CoderWanFeng/python-office/issues)
- [AtomGit Issue](https://atomgit.com/CoderWanFeng1/python-office/issues)

---

## ⭐ Star History

[![Stargazers over time](https://starchart.cc/CoderWanFeng/python-office.svg)](https://starchart.cc/CoderWanFeng/python-office)

---

## 📌 联系作者

<p align="center">
    <a target="_blank" href='https://www.python4office.cn/wechat-qrcode/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/c52fb12c-7cb7-4684-8a3e-020a4bec8888/f0501b73cd57eba391ab4fc5a6654669.jpg" width="60%"/>
    </a>
</p>

<p align="center">
    👉 <a target="_blank" href='https://www.python4office.cn/wechat-group/'>加入开源交流群</a> ·
    <a target="_blank" href='https://www.python4office.cn/wechat-qrcode/'>联系作者微信</a> 👈
</p>

---

<p align="center">
    <sub>如果这个项目对你有帮助，欢迎 ⭐ Star 支持一下！</sub>
</p>
