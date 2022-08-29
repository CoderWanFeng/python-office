import pathlib
import shutil

'''
子包的名字：Ruiming
'''


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
            dir_path_file_list = list(dir_path.iterdir())
            print(dir_path_file_list)
            for file_name in dir_path_file_list:
                if file_name.is_file():
                    if file_name.suffix == image_name_extension:
                        image_name_root_set.add(file_name.name.replace(image_name_extension, ""))
                    if file_name.suffix == marked_file_name_extension:
                        marked_file_name_root_set.add(file_name.name.replace(marked_file_name_extension, ""))
            unmarked_image_list = list(image_name_root_set - marked_file_name_root_set)
            print(image_name_root_set)
            print(marked_file_name_root_set)
            print(unmarked_image_list)
            for i in unmarked_image_list:
                shutil.move(dir_path.joinpath(i + image_name_extension),
                            unmarked_image_storage_path.joinpath(i + image_name_extension))
        else:
            print("路径输入有误，请检查！")


if __name__ == '__main__':
    ruiming = MainRuiming()
    ruiming.screen_unmarked_image("./test1")
'''
test1文件夹下有1.jpg、2.jpg、1.xml三个文件
执行完毕后，2.jpg被移动到./test1/未标注图片/中
'''
