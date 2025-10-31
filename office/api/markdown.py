import pomarkdown


def excel2markdown(input_file, output_file=r'./excel2markdown.md', sheet_name=None):
    """将Excel文件转换为Markdown格式的文件。
    
    本函数利用pomarkdown库中的excel2markdown函数执行转换操作。
    主要负责定义转换的输入输出路径及工作表名称。
    
    Args:
        input_file (str): 输入Excel文件的路径
        output_file (str, optional): 输出Markdown文件的路径，默认为当前目录下的'excel2markdown.md'
        sheet_name (str, optional): 需要转换的Excel工作表名称，默认为None，表示转换所有工作表
    
    Returns:
        None
    """
    # 调用pomarkdown库中的excel2markdown函数执行Excel到Markdown的转换
    pomarkdown.excel2markdown(input_file, output_file, sheet_name)

