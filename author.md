大二暑假实训做的项目，实现了word转pdf（批量），ppt转pdf（批量），pdf加密，加水印等功能
## 版本：python版本3.6.6      
## 提示：将代码打包，安装好需要的包， 文件夹里面运行main.py文件即可运行窗口
## 用到的外部包：
PyQt5用于框架和界面的设计
pathlib 用于路径的获取和拼接

1. word功能：word转pdf功能用到comtypes包，pathlib包；word关键字替换功能用到win32com包path包
2. PPT功能：ppt转图片和转pdf功能用到comtypes包，pathlib包， ppt图片提取用到zipfile包，pathlib包和win32com包以及shutil包
3. PDF功能：PDF添加水印用到pathlib包，PyPDF2包，reportlab包；pdf加密解密功能用到PyPdf2以及pathlib
4. 文件整理中的冗余文件处理用到filecmp包和pathlib包，文件分类功能仅用pathlib包
5. 界面美化用了qt_material库 开源链接https://github.com/UN-GCPDS/qt-material