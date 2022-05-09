# Python自动化办公学习指南


![图片](https://f10.baidu.com/it/u=442371958,171656815&fm=30&app=106&f=JPEG&access=215967316?w=640&h=201&s=D923707E86D40D7216227510020080DA)



大家好，这里是法学院毕业的程序员晚枫，专注于Python自动化办公知识分享。
> 自动化办公，学习交流群[👉【戳我加入】](http://www.python4office.cn/wechat-group/)

最近Pypi官网发布了一个Python自动化办公的神器：python-office，内含所有Python自动化办公的第三方库，可以帮助小白【快速使用】Python自动化办公。



# 下载和使用

本项目旨在开发一个第三方库：python-office，可以帮助需要进行Python自动化办公的朋友，**尤其是小白，**通过下列方式，一键安装完成进行Python自动化办公的开发环境。
> 目前项目已上线Python官网：[传送门](https://pypi.org/project/python-office)

0. 安装这个库之前，你的电脑上，需要有python环境
没有的同学，请移步这个6分钟的安装视频：[来，手把手带你搭建Python环境](https://www.bilibili.com/video/BV1Q44y1u7rV)

1. 安装好后，打开pycharm的terminal，输入以下命令，即可自动安装
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U
```

作用：
- 一键搭建所有Python + 自动化办公的编程环境。
- 一行代码，解决大部分自动化办公的问题，不需要小白学习Python知识，自己苦哈哈的写代码


# 功能文档（持续更新）

本部分内容，旨在介绍python-office的所有已有功能，持续更新中
### 一、Word操作

#### 1、word转pdf
[python-office库：只要2行Python代码，实现Word批量转换PDF](https://mp.weixin.qq.com/s/6SM_66BjCIzUkkRWrDe5pQ)
```python
import office # 导入python-office

path = '.'  # path这里，填写你存放word文件的位置，例如：C:/app/workbook
office.word.docx2pdf(path=path) # 程序就可以自动将该目录下的所有word文档，自动转换成pdf文档了
```
### 二、PDF操作
#### 1、pdf添加水印
[一行Python代码，给PDF文件添加水印，快速而且免费~python-office自动化办公，YYDS](https://mp.weixin.qq.com/s/yJDs5RoytRL5hl-ybXkZOA)
```python
import office  # 导入python-office

office.pdf.add_watermark() # 不需要对代码进行任何修改，直接运行
```
#### 2、pdf加密、解密
```python
import office

office.pdf.encrypt4pdf('1.API参考.pdf', password='123456')

office.pdf.decrypt4pdf(path='encrypt.pdf',password='123456')
```
### 三、图片操作

#### 1、文字生成词云
[逆天！1 行代码就可以生成可视化词云，python-office自动化办公发布新功能！](https://mp.weixin.qq.com/s/ifmt7MDleACNQKxk77EeNA)
```python
import office  # 导入python-office

office.image.txt2wordcloud(filename='yes-minister.txt', 
                            color='black', 
                            result_file="your_wordcloud.png")

参数说明
filename：这里填写你需要生成词云的txt文档的路径，例如：d:/work/ciyun.txt
color：这个是词云的底色，可以设置任何颜色；可以不填，默认是白色底色。
result_file：生成词云图片的名字，格式必须是png；可以不填，默认是：your_wordcloud.png
```

#### 2、图片添加水印
```python
import office

office.image.add_watermark('anaconda2.jpg','公众号：程序员晚枫')
```
### 四、文件和文件夹操作
#### 1、批量重命名文件和文件夹
```python
import office
path = 'D:\\QMDownload\\'
office.file.replace4filename(path=path,del_content='新建文件夹',replace_content='5')

```
### 五、视频操作
#### 1、从视频里提取MP3
```python
import office
path = 'D:\\QMDownload\\'
office.video.video2mp3(path=path,mp3_name='result')
```
# 目前包含的第三方库有


#### Excel

- xlrd：读取excel

- xlwt：写入Excel

- xlutils：调整Excel的格式

- xlwings：[xlwings库 | Excel与Python的完美结合（附使用文档）](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247492034&idx=1&sn=b677b3f285b1426c0c83dbba7708a5d7&chksm=eaf540f7dd82c9e1ff2bfa197580f5e88c4d45ad1c18e9c9ef534d7b3e5ae006dca62c3546bf&scene=21#wechat_redirect)

- openpyxl：灵活处理Excel的数据

- xlswriter：功能扩展库

- pandas：[系统性的学会 Pandas， 看这一篇就够了！](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247495847&idx=1&sn=056789b0e560c014d8f9530fbf63d584&chksm=eaf55192dd82d884f69c48d657e3f76654a6cb5f9e9a4a70780be69320fd525e0fe3773c543c&scene=21#wechat_redirect)

- pyxll：一个强大的插件库

  

#### Word

- python-docx：[Python-Docx库 | Word与Python的完美结合（附使用文档）](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247491631&idx=1&sn=c169f107acfb03b2f37661a4b6f50587&chksm=eaf5411add82c80c59af213553db3020d0b5a439b84dcb21086258a6a9b2de2719df0390e32a&scene=21#wechat_redirect)

#### PPT

- python-pptx：[python-pptx库 | PPT与Python的完美结合（附使用文档）](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247492263&idx=1&sn=2d7f601b34913415238b7a232acba13c&chksm=eaf54392dd82ca844a6fc653e3492bdac12d96a332d305f05ea15d01c916e5f7f81fa3decae3&scene=21#wechat_redirect)

#### PDF

- PyPDF2：[PyPDF2库 | PDF与Python的完美结合（附使用文档）](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247492209&idx=1&sn=55152c540a1c927bb9fcb79005327b29&chksm=eaf54344dd82ca5295e6e2d1e11712f97118871f6639d593826200f1bce45b98c0c03d494de7&scene=21#wechat_redirect)
- 待完善

#### OCR

- easyocr：图片识别库，支持80+语言
- 待完善

#### 爬虫

- scrapy：一键开启爬虫，爬取全站资源

#### 网站开发

- django：[深度盘点 | 史上最全Python网站开发库（37个）](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247494188&idx=1&sn=3e0d887d9588399e4c6035dd7916f8fc&chksm=eaf54b19dd82c20f9ae7bf3f5a7f9606d456b85e63f31ebe41d6938ed77c88f438a6b08cdab7&scene=21#wechat_redirect)
- flask：一键生成网站

#### 数据分析 & 数据可视化

- pandas
- numpy
- matplotlib：[278页PDF：《Python数据分析基础》，0基础入门专用~](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247496126&idx=3&sn=b4bb4d3551e6486baa1b70ef72414a8e&chksm=eaf5508bdd82d99db0bd1b6ed9307328bc6954de87b5f26ef5ae222b2e4fd7c500890a20dd7e&scene=21#wechat_redirect)




# 加入项目

#### 项目介绍

本项目旨在打包所有Python + 自动化办公的技术，方便大家的自动化办公使用。
欢迎大家提交PR（pull request），一起来丰富这个项目！
> “
>
> 欢迎感兴趣的朋友，通过提交PR的方式，参与该项目的更新与维护，我每天下午merge一次。源码地址如下

- Gitee地址：[https://gitee.com/CoderWanFeng/python-office](https://gitee.com/CoderWanFeng/python-office)

- GitHub地址：[https://github.com/CoderWanFeng/python-office](https://github.com/CoderWanFeng/python-office)


# 版本说明

| 版本号 | 版本信息            | 发布日期  |
| ------ | ------------------- | --------- |
| 0.0.1  | init：项目初始化          | 2022-4-19 |
| 0.0.2  | init：添加基础库          | 2022-4-21 |
| 0.0.3  | init：matplotlib和easyocr | 2022-4-24 |
| 0.0.4  | init：修改配置文件为setup.cfg | 2022-4-24 |
| 0.0.5  | init：发布wheel文件 | 2022-4-24 |
| 0.0.6  | add：word批量转pdf | 2022-4-24 |
| 0.0.7  | patch：word批量转pdf | 2022-4-24 |
| 0.0.8  | add：单个pdf添加水印 | 2022-4-25 |
| 0.0.9  | patch：因为安装包太大，去掉matplotlib；添加项目交流群 | 2022-4-25 |
| 0.0.10  | add：txt文本转词云功能 | 2022-4-28 |
| 0.0.11  | update：word批量转pdf | 2022-5-1 |
| 0.0.12  | add：重命名指定路径下的文件/文件夹 | 2022-5-4 |
| 0.0.13  | update：因为c++14的原因，去掉wordcloud库，需要的同学，自行install即可 | 2022-5-6 |
| 0.0.14  | add：给图片加水印、生成二维码、提取音频、翻译 | 2022-5-6 |
| 0.0.15  | add：pdf加密、解密 | 2022-5-9 |

> 关于版本更新，如有疑问，请私信微博@[程序员晚枫](http://www.python4office.cn/weibo-qaq/)
>
> 或者，欢迎有学习/定制功能/加入项目需求的同学，直接加入我们的项目交流群👉[点我直达](http://www.python4office.cn/images/2-free-group.jpg)

## 参考资料 
- 关于setup.py的参数说明
    - https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#install-requires
- 如何使用setup.cfg
    - https://zhuanlan.zhihu.com/p/261579357
- 打包pip
    - https://mp.weixin.qq.com/s/zzD4pxNMFd0ZuWqXlVFdAg