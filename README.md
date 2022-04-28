# Python自动化办公学习指南

## 版本说明

| 版本号 | 版本信息            | 发布日期  |
| ------ | ------------------- | --------- |
| 0.0.1  | 项目初始化          | 2022-4-19 |
| 0.0.2  | 添加基础库          | 2022-4-21 |
| 0.0.3  | 增加matplotlib和easyocr | 2022-4-24 |
| 0.0.4  | 修改配置文件为setup.cfg | 2022-4-24 |
| 0.0.5  | 发布wheel文件 | 2022-4-24 |
| 0.0.6  | 增加功能：word批量转pdf | 2022-4-24 |
| 0.0.7  | 修复功能：word批量转pdf | 2022-4-24 |
| 0.0.8  | 增加功能：单个pdf添加水印 | 2022-4-25 |
| 0.0.9  | 因为安装包太大，去掉matplotlib；添加项目交流群 | 2022-4-25 |
| 0.0.10  | add 【词云功能】 | 2022-4-28 |

> 关于版本更新，如有疑问，请私信微博@[程序员晚枫](http://www.python4office.cn/weibo-qaq/)
>
> 或者，欢迎有学习/定制功能/加入项目需求的同学，直接加入我们的项目交流群👉[点我直达](http://www.python4office.cn/images/2-free-group.jpg)


[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/zDSXSxxV3hKiaoXW8JVY1TsKFYiaKP52tbhV3S5SXcziam69C8BqqiaRjAGLs412Ph2cb7picSKniaclGUehOM7d6vzA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg3MDU3OTgxMg==&mid=2247490887&idx=1&sn=4b127c7bd829514e45ff3a577f940286&chksm=ce8af64cf9fd7f5a69cb743c0e467307bb7ade480edd6b457f6fae581fadf9c86c9b9bc0fd31&scene=21#wechat_redirect)



大家好，这里是法学院毕业的程序员晚枫，专注于Python自动化办公知识分享。技术交流微信👉[CoderWanFeng](https://mp.weixin.qq.com/s?__biz=MzkyMzIwOTgzMA==&mid=2247485697&idx=1&sn=19fd2c7cc0193e7ca529e05519bd67e9&scene=21#wechat_redirect)



最近Pypi官网发布了一个Python自动化办公的神器：python-office，内含所有Python自动化办公的第三方库，可以帮助小白快速学会Python自动化办公。



安装命令：



```
pip install python-office
```

## 项目来源

Python自动化办公是一个最近几年刚刚兴起的方向，需要安装的第三方库非常多且杂。

在开发的过程中，需要不断重复pip install some-packages。

**有没有一个第三方库**，可以像Anaconda汇总了所有的Python数据分析库一样，**可以一键安装所有Python自动化办公的第三方库呢？**

于是就有了今天的python-office库：可以一键完成所有Python自动化办公的开发环境的安装，其中包含的第三方库的功能和使用说明，之前给大家整理过：[深度盘点丨史上最全的Python自动化办公库（34个）](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247494263&idx=2&sn=20233004805dbc3934e524aeecfb69b3&chksm=eaf54b42dd82c254c2fb81c0dc1441861be9ac511f61bbbe0df1b005f43c312883ad491c8b43&scene=21#wechat_redirect)

> “
>
> 目前项目已上线，下载地址：

```
Python库的地址：[https://pypi.org/project/python-office/](https://pypi.org/project/python-office/)
```

## 下载和使用

本项目旨在开发一个第三方库：python-office，可以帮助需要进行Python自动化办公的朋友，**尤其是小白，**通过下列方式，一键安装完成进行Python自动化办公的开发环境。

```
pip install python-office
```

作用：
- 一键搭建所有Python + 自动化办公的编程环境。
- 一行代码，解决大部分自动化办公的问题，不需要小白学习Python知识，自己苦哈哈的写代码


## 功能文档（持续更新）
- word：
    - word 转 pdf：[python-office库：只要2行Python代码，实现Word批量转换PDF](https://mp.weixin.qq.com/s/6SM_66BjCIzUkkRWrDe5pQ)
- pdf：
    - pdf添加水印：[一行Python代码，给PDF文件添加水印，快速而且免费~python-office自动化办公，YYDS](https://mp.weixin.qq.com/s/yJDs5RoytRL5hl-ybXkZOA)
- image：
    - 自动生成词云：[逆天！1 行代码就可以生成可视化词云，python-office自动化办公发布新功能！](https://mp.weixin.qq.com/s/ifmt7MDleACNQKxk77EeNA)

## 目前包含的第三方库有


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




## 加入我们

#### 项目介绍

本项目旨在打包所有Python + 自动化办公的技术，方便大家的自动化办公使用。
欢迎大家提交PR（pull request），一起来丰富这个项目！
> “
>
> 欢迎感兴趣的朋友，通过提交PR的方式，参与该项目的更新与维护，我每天下午merge一次。源码地址如下

- Gitee地址：[https://gitee.com/CoderWanFeng/python-office](https://gitee.com/CoderWanFeng/python-office)

- GitHub地址：[https://github.com/CoderWanFeng/python-office](https://github.com/CoderWanFeng/python-office)

  
## 参考资料 
- 关于setup.py的参数说明
    - https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#install-requires
- 如何使用setup.cfg
    - https://zhuanlan.zhihu.com/p/261579357
- 打包pip
    - https://mp.weixin.qq.com/s/zzD4pxNMFd0ZuWqXlVFdAg