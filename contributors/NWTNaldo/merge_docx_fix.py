import os
import re
from docx import Document
from docxcomposer import Composer

def merge4docx(input_path: str, output_path: str, new_word_name: str = "merged.docx") -> str:
    """
    合并指定文件夹下的所有 .docx 文件

    :param input_path: 输入 Word 文件的文件夹路径
    :param output_path: 合并后 Word 文件的输出文件夹路径
    :param new_word_name: 合并后的新文件名（如 "111.docx"）
    :return: 合并后文件的完整输出路径
    """
    # 1. 自动处理目录路径与创建
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    # 2. 规范化文件名（防止重复拼接 .docx 后缀）
    if not new_word_name.lower().endswith('.docx'):
        new_word_name = f"{new_word_name}.docx"

    final_output_file = os.path.join(output_path, new_word_name)

    # 3. 过滤临时文件（以 ~$ 开头）并仅保留 .docx 格式文件
    all_files = [
        f for f in os.listdir(input_path)
        if f.lower().endswith('.docx') and not f.startswith('~$')
    ]

    # 4. 自然排序算法（确保 1.docx, 2.docx, 10.docx 按常规数字顺序合并）
    def natural_sort_key(filename: str):
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', filename)]

    all_files.sort(key=natural_sort_key)

    if not all_files:
        raise FileNotFoundError(f"在路径 '{input_path}' 下未找到有效的 .docx 文件")

    # 5. 排除输出文件本身（防止同目录合并时递归循环）
    files_to_merge = []
    for file in all_files:
        full_path = os.path.abspath(os.path.join(input_path, file))
        if full_path == os.path.abspath(final_output_file):
            continue
        files_to_merge.append(full_path)

    if not files_to_merge:
        raise ValueError("没有可用于合并的目标文件")

    # 6. 以第一个文件为主文档初始化 Composer
    master_doc = Document(files_to_merge[0])
    composer = Composer(master_doc)

    # 7. 依次合并后续文件并添加分页符
    for file_path in files_to_merge[1:]:
        doc_to_append = Document(file_path)
        master_doc.add_page_break()  # 在文档末尾追加分页
        composer.append(doc_to_append)

    # 8. 保存合并后的文档
    composer.save(final_output_file)
    return final_output_file
