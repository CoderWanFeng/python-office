---
title: txt2wordcloud
date: 2022-04-28 10:25:24
tags:
---


>Python官网发布了Python自动化办公的库：python-office，相关信息：[重磅！官网发布第三方库：python-office，为Python自动化办公而生](https://mp.weixin.qq.com/s/v2n0DTVTZUaw7QOnA0Zlow)
>不需要自己写代码，直接调用写好的方法就行。

大家好，这里是程序员晚枫，专注于分享：Python自动化办公。
**这个系列教程[【python-office】功能文档](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI2Nzg5MjgyNg==&action=getalbum&album_id=2371443069708992513&scene=173&from_msgid=2247496501&from_itemidx=1&count=3&nolastread=1#wechat_redirect)，用来逐一介绍python-office自动化办公的功能。**
## 1、功能介绍

上次我们介绍了python-office这个库的功能之二：[一行代码给PDF加水印](https://mp.weixin.qq.com/s/yJDs5RoytRL5hl-ybXkZOA)，
今天我们介绍这个库的功能之三：
> 一行代码，自动根据你提供的文档，生成下图所示的词云

## 2、代码使用

#### 下载python-office
> 因为python-office这个库更新的很快，
> 所以不论你的电脑有没有安装过python-office，都需要运行一下下面这个命令，作用如下：
- 如果你是第一次使用python-office，这条命令可以把python-office自动安装到你的电脑里。
- 如果你之前使用过，这条命令可以在不卸载的情况下，把你本地的python-office更新到最新版本
```python
pip install --upgrade python-office
```
#### 调用功能
安装完python-office，直接复制粘贴，运行下面这个代码
```python
import office  # 导入python-office

office.image.txt2wordcloud(filename='yes-minister.txt', color='black', result_file="your_wordcloud.png")

```
- 参数说明
    - filename：这里填写你需要生成词云的txt文档的路径，例如：d:/work/ciyun.txt
    - color：这个是词云的底色，可以设置任何颜色；可以不填，默认是白色底色。
    - result_file：生成词云图片的名字，格式必须是png；可以不填，默认是：your_wordcloud.png

填写好对应的参数，就可以直接运行程序生成词云图片啦~


## 3、关于python-office
python-office是pypi开源的第三方库，专为python自动化办公而生。
欢迎大家加入python-office这个库的技术交流群👇

>也欢迎大家参与python-office这个开源项目的建设：
> - https://gitee.com/CoderWanFeng/python-office
> - https://github.com/CoderWanFeng/python-office

## 更多阅读
- [深度盘点丨史上最全的Python自动化办公库（34个）](https://mp.weixin.qq.com/s/RsBG_cg8GsB2P-9zmhrA1Q)
- [xlwings库 | Excel与Python的完美结合（附使用文档）](https://mp.weixin.qq.com/s/2_qNnsPK6fjEAUu3jf-NFA)
- [Python-Docx库 | Word与Python的完美结合（附使用文档）](https://mp.weixin.qq.com/s/_QzBRGeXsqF65-xlzQfFjQ)
