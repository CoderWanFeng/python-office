import pathlib
import shutil
import xml.etree.ElementTree
import json


class MainRuiming():
    def __make_dir(self, dir_path, dir_name):
        """

        :param dir_path: 准备新建的位置
        :param dir_name: 新建文件夹的名称
        """
        new_dir_path = dir_path.joinpath(dir_name)
        if not new_dir_path.is_dir():
            new_dir_path.mkdir()
        elif list(new_dir_path.iterdir()) != []:
            exit("目录\"" + str(new_dir_path) + "\"存在且不为空，请检查！")

    def screen_unmarked_image(self, dir_path, image_name_extension: str = ".jpg",
                              marked_file_name_extension: str = ".xml"):
        """

        :param dir_path: 图片及标注文件的存放路径
        :param image_name_extension: 图片文件的后缀，默认为.jpg
        :param marked_file_name_extension: 标注文件的后缀，默认为.xml
        """
        dir_path = pathlib.Path(dir_path).resolve()
        if dir_path.is_dir():
            unmarked_image_storage_path = dir_path.joinpath("未标注图片")
            self.__make_dir(dir_path, "未标注图片")
            image_name_root_set = set()
            marked_file_name_root_set = set()
            # 创建集合
            dir_path_file_list = list(dir_path.iterdir())
            for file_name in dir_path_file_list:
                # 按文件类型添加文件名到对应的集合
                if file_name.is_file():
                    if file_name.suffix == image_name_extension:
                        image_name_root_set.add(file_name.name.replace(image_name_extension, ""))
                    if file_name.suffix == marked_file_name_extension:
                        marked_file_name_root_set.add(file_name.name.replace(marked_file_name_extension, ""))
            unmarked_image_list = list(image_name_root_set - marked_file_name_root_set)
            for i in unmarked_image_list:
                shutil.move(dir_path.joinpath(i + image_name_extension),
                            unmarked_image_storage_path.joinpath(i + image_name_extension))
            print("筛选完成")
        else:
            print("路径输入有误，请检查！")

    def change_label_in_xml(self, dir_path, old_label, new_label):
        """

        :param dir_path: 图片及标注文件的存放路径
        :param old_label: 需要修改的标签
        :param new_label: 修改后的标签
        """
        dir_path = pathlib.Path(dir_path).resolve()
        if dir_path.is_dir():
            file_list = list(dir_path.iterdir())
            for file in file_list:
                if file.suffix == ".xml":
                    xml_file = xml.etree.ElementTree.parse(str(file))
                    xml_root = xml_file.getroot()
                    label_xpath = "./object/name"
                    label_list = xml_root.findall(label_xpath)
                    for label in label_list:
                        if label.text == old_label:
                            label.text = new_label
                    xml_file.write(str(file), encoding="utf-8")
        else:
            print("请输入正确的路径！")

    def screen_without_label_json_file(self, dir_path):
        dir_path = pathlib.Path(dir_path).resolve()
        if dir_path.is_dir():
            print("正在筛选无标签内容的json文件")
            without_label_json_storage_path = dir_path.joinpath("无标签json文件")
            self.__make_dir(dir_path, "无标签json文件")
            dir_path_file_list = list(dir_path.iterdir())
            for file_name in dir_path_file_list:
                if file_name.is_file() and file_name.suffix == ".json":
                    json_file = open(file_name, "r")
                    json_file_text = json.load(json_file)
                    json_file.close()
                    if json_file_text["shapes"] == []:
                        shutil.move(dir_path.joinpath(file_name.name),
                                    without_label_json_storage_path.joinpath(file_name.name))
            print("筛选完成")
        else:
            print("路径输入有误，请检查！")
