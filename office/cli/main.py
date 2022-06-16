"""
python-office Command Line Interface
====================================

```script
python -m office --help
```
"""
from typer import Typer

app = Typer(name="python-office CLI")


#
# @app.command()
# def ppt2pdf(dir_path: str):
#     """ppt导出为PDF，需要Microsoft Office环境"""
#     try:
#         from office.ppt import ppt2pdf
#     except ImportError:
#         from office.ppt import ppt2pdf
#     return ppt2pdf(dir_path)
#

@app.command()
def docx2pdf(dir_path: str, suffix="docx"):
    """docx转pdf"""
    from office.word import docx2pdf
    Typer.launch("http://www.python4office.cn/wechat-group/")
    return docx2pdf(dir_path, suffix)


@app.command()
def hello():
    print(666)


#
#
# @app.command()
# def pdf_encrypt(input_path: str, password: str, output_path: str = None):
#     """加密PDF 输入路径 密码 [输出路径(默认与输入相同)]"""
#     try:
#         from .pdf import encrypt4pdf
#     except ImportError:
#         from pdf import encrypt4pdf
#     return encrypt4pdf(input_path, password, output_path or input_path)
#
#
# @app.command()
# def pdf_decrypt(input_path: str, password: str, output_path: str = None):
#     """解密PDF 输入路径 密码 [输出路径(默认与输入相同)]"""
#     try:
#         from .pdf import decrypt4pdf
#     except ImportError:
#         from pdf import decrypt4pdf
#     return decrypt4pdf(input_path, password, output_path or input_path)
#
#
# @app.command()
# def pdf_merge(paths: list[str], output_path: str):
#     """合并PDF 若干pdf路径 最后一个参数为合并后的PDF的路径"""
#     try:
#         from .pdf import merge2pdf
#     except ImportError:
#         from pdf import merge2pdf
#     return merge2pdf(paths, output_path)
#
#
# @app.command()
# def watermark(path: str, mark: str, out_dir="output", color="#8B8B1B", size=30, opacity=0.15, space=75, angle=30):
#     """图片水印 文件(夹)路径 水印文本 [输出文件夹] [颜色] [字号] [透明度] [字间距] [倾角]"""
#     try:
#         from .image import add_watermark
#     except ImportError:
#         from image import add_watermark
#     return add_watermark(path, mark, out_dir, color, size, opacity, space, angle)
#
#
# @app.command()
# def txt2pdf(txt_path: str, pdf_path: str):
#     """创建纯文本PDF 输入路径 输出路径"""
#     try:
#         from .pdf import txt2pdf
#     except ImportError:
#         from pdf import txt2pdf
#     return txt2pdf(txt_path, pdf_path)
#
#
# @app.command()
# def rename(path: str, old: str, new=""):
#     """批量修改文件名 目录路径 子字符串 [新字符串]"""
#     try:
#         from .file import replace4filename
#     except ImportError:
#         from file import replace4filename
#     return replace4filename(path, old, new)
#
#
# @app.command()
# def fake(path="./fake2excel.xlsx", rows=1, columns=("name",), language='zh_CN'):
#     """生成假数据Excel文件 [导出文件路径] [行数] [列名列表] [语种]"""
#     try:
#         from .excel import fake2excel
#     except ImportError:
#         from excel import fake2excel
#     return fake2excel(columns, rows, language, path)
#
#
# @app.command()
# def pwd(length: int = 8):
#     """生成随机密码"""
#     try:
#         from .tools import passwordtools
#     except ImportError:
#         from tools import passwordtools
#     return passwordtools(length)
#
#
# @app.command()
# def extract_audio(input_path: str, output_path: str = None):
#     """从视频中提取音频"""
#     try:
#         from .video import video2mp3
#     except ImportError:
#         from video import video2mp3
#     return video2mp3(input_path,
#                      (input_path[:input_path.rindex(".")] or output_path.removesuffix(".mp3")) + ".mp3")
#

if __name__ == '__main__':
    app()
