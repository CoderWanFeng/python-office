import pathlib
import openpyxl


def output_file_list_to_excel(dir_path: str):
    """
    :param dir_path: 需要生成文件列表的目录
    """
    dir_path = pathlib.Path(dir_path).resolve()
    if dir_path.is_dir():
        dir_path_list = list(dir_path.glob("**/*"))
        output_excel = openpyxl.Workbook()
        output_excel_sheet = output_excel.active
        output_excel_sheet.append(["完整路径", "文件所在路径", "文件名"])
        for file_path in dir_path_list:
            if file_path.is_file():
                output_excel_sheet.append([str(file_path), str(file_path.parent), str(file_path.name)])
        output_excel.save(dir_path.joinpath("本目录文件列表.xlsx"))
    else:
        print("请输入正确的文件路径！")


if __name__ == '__main__':
    output_file_list_to_excel(".")
