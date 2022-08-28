import base64
import pathlib


def markdown_link_image_to_base64(markdown_path):
    markdown_path = pathlib.Path(markdown_path)
    if markdown_path.is_file() and markdown_path.suffix == ".md":
        i = 0  # 图片计数变量
        image_base64_list = []  # 图片base64编码列表
        markdown_file = open(markdown_path, encoding="utf-8")
        new_markdown_file = open(markdown_path.parent.joinpath(markdown_path.name[:-3:] + "(base64).md"), "x",
                                 encoding="utf-8")
        markdown_file = markdown_file.readlines()
        for line in markdown_file:
            # 按行遍历文件
            if line[:2:] == "![":
                # 如果该行有链接图片
                i = i + 1
                this_image_path = pathlib.Path(line[line.rfind("(") + 1:line.rfind(")"):])
                if not this_image_path.is_absolute():
                    # Python文件和markdown文件通常不在同一路径，相对路径基准不同，故需要判断链接图片路径是否为绝对路径。
                    this_image_path = markdown_path.parent.joinpath(this_image_path).resolve()
                this_image_file = open(this_image_path, "rb")
                this_image_base64_data = base64.b64encode(this_image_file.read())
                # 对链接的图片进行base64编码
                line = line[:line.index("("):] + f"[image{str(i)}]" + "\n"
                image_base64_list.append(
                    f"[image{str(i)}]: " + "data:image/" + this_image_path.suffix + ";base64," + str(
                        this_image_base64_data)[2:-1:] + "\n")
            new_markdown_file.writelines(line)
        for i in image_base64_list:
            # 遍历存放base64编码的列表
            if markdown_file[-1] != "\n":
                new_markdown_file.writelines("\n")
            # 判断最后一行是否为空行，如果不是则写入换行符
            new_markdown_file.writelines(i)
            # 将图片的base64编码写入新文件
    elif not markdown_path.is_file():
        print("markdown文件路径输入有误，请检查！")
    elif markdown_path.suffix != ".md":
        print("请输入.md文件的路径！")


if __name__ == '__main__':
    markdown_link_image_to_base64("./test/test.md")
