"""
md-studio + python-office 联动极简示例
功能流程：
1. 使用 md-studio 将 markdown 文件转为 Word
2. 使用 python-office 读取、修改生成后的 Word 文件
"""

# 安装依赖命令
# pip install python-office md-studio

import office
# 导入md-studio转换工具
from md_studio.converter import MdToWord

def simple_md_office_flow():
    # 1. md 转 word
    converter = MdToWord()
    converter.convert("demo.md", "output.docx")

    # 2. 使用 python-office 读取生成的word文档
    word = office.Word("output.docx")
    content = word.read_text()
    print("读取到md转换后的文档内容：", content[:100])

    # 3. 追加一行文本到word
    word.add_paragraph("本文件由 md-studio + python-office 联合处理")
    word.save()
    print("文档处理完成！")

if __name__ == "__main__":
    simple_md_office_flow()