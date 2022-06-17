import os
import time

from office.lib.ppt.ppt2pdf_service import ppt2pdf_single


class MainPPT():

    def ppt2pdf(self, path):
        """
        @Author & Date  : CoderWanFeng 2022/5/9 23:34
        @Desc  : path:存放ppt的路径，必须写绝对路径~！
        """
        # 列出指定目录的内容
        filenames = os.listdir(path)
        # for循环依次访问指定目录的所有文件名
        for filename in filenames:
            # 判断文件的类型，对所有的ppt文件进行处理(ppt文件以ppt或者pptx结尾的)
            if filename.endswith('ppt') or filename.endswith('pptx'):
                # print(filename)           # PPT素材1.pptx -> PPT素材1.pdf
                # 将filename以.进行分割，返回2个信息，文件的名称和文件的后缀名
                base, ext = filename.split('.')  # base=PPT素材1 ext=pdf
                new_name = base + '.pdf'  # PPT素材1.pdf
                # ppt文件的完整位置: C:/Users/Administrator/Desktop/PPT办公自动化/ppt/PPT素材1.pptx
                filename = path + '/' + filename
                # pdf文件的完整位置: C:/Users/Administrator/Desktop/PPT办公自动化/ppt/PPT素材1.pdf
                output_filename = path + '/' + new_name
                # 将ppt转成pdf文件
                ppt2pdf_single(filename, output_filename)
                time.sleep(3)
