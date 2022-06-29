from faker import Faker
import pandas as pd
from alive_progress import alive_bar
from office.lib.utils import pandas_mem
import os
from pathlib import Path


class MainExcel():

    def fake2excel(self, columns, rows, path, language):
        """
        @Author & Date  : CoderWanFeng 2022/5/13 0:12
        @Desc  : columns:list，每列的数据名称，默认是名称
                rows：多少行，默认是1
                language：什么语言，可以填english，默认是中文
                path：输出excel的位置，有默认值
        """
        # 可以选择英语
        if language.lower() == 'english':
            language = 'en_US'
        else:
            language = 'zh_CN'
        # 开始造数
        fake = Faker(language)
        excel_dict = {}
        with alive_bar(len(columns) * rows) as bar:
            for column in columns:
                excel_dict[column] = list()
                # excel_dict[column] = map(lambda x: eval('fake.{func}()'.format(func=x)), [column] * rows) # 使用map，会报错
                while len(excel_dict[column]) < rows:
                    excel_dict[column].append(eval('fake.{func}()'.format(func=column)))
                    bar()
            # 用pandas，将模拟数据，写进excel里面
            writer = pd.ExcelWriter(path)
            data = pd.DataFrame(excel_dict)
            data = pandas_mem.reduce_pandas_mem_usage(data)
            data.to_excel(writer, index=False)
            # writer.save()
            writer.close()

    def merge2excel(self, dir_path, output_file,xlsxSuffix=".xlsx"):
        """
        :param dir_path:
        :param output_file:
        :return:
        """
        if not output_file.endswith(xlsxSuffix):
            raise Exception(f'您自定义的输出文件名，不是以{xlsxSuffix}结尾的')
        file_path_dict = self.getfile(dir_path)  # excel文件所在的文件夹
        try:
            writer = pd.ExcelWriter(output_file)  # 合并后的excel名称
        except PermissionError:
            raise Exception(f'小可爱，你的输出文件，是不是上次打开了没关闭呀？这是你自己指定的输出文件名称：{output_file}')
        for file, path in file_path_dict.items():
            if file.endswith("xlsx"):
                df = pd.read_excel(path)
            if file.endswith("csv"):
                df = pd.read_csv(path)
            df.to_excel(writer, sheet_name=file.split('.')[0], index=False)
        print(f'您指定的Excel文件已经合并完毕，合并后的文件名是{output_file}')
        writer.save()

    def getfile(self, dirpath):
        path = Path(dirpath)
        file_path_dict = {}
        for root, dirs, files in os.walk(dirpath):
            for file in files:
                if file.endswith("xlsx") or file.endswith("csv"):
                    file_path_dict[file] = (path / file)
        return file_path_dict
