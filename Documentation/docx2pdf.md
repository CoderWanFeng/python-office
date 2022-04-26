
>Python官网发布了Python自动化办公的库：python-office，相关信息：[重磅！官网发布第三方库：python-office，为Python自动化办公而生](https://mp.weixin.qq.com/s/v2n0DTVTZUaw7QOnA0Zlow)
>不需要自己写代码，直接调用写好的方法就行。

大家好，这里是程序员晚枫，专注于分享：Python自动化办公。
**这个系列教程，用来逐一介绍python-office自动化办公的功能。**
## 功能介绍
今天我们介绍这个库的功能之一：
> 自动化批量Word转PDF，你只需要输入存放Wor的文件的文件夹位置，剩下的，交给python吧
## 使用说明

#### 下载python-office

只需要下面这一条命令，就可以自动下载和安装python-office
```
pip install python-office
```
> 也欢迎大家参与python-office这个开源项目的建设：
>开源地址：
>https://gitee.com/CoderWanFeng/python-office
>https://github.com/CoderWanFeng/python-office
#### 调用功能
```python
import office # 导入python-office

path = '.'  # path这里，填写你存放word文件的位置，例如：C:/app/workbook
office.word.docx2pdf(path=path)

```
> 注意：这个功能，目前只支持docx格式的文件。

## 更多阅读
- [深度盘点丨史上最全的Python自动化办公库（34个）](https://mp.weixin.qq.com/s/RsBG_cg8GsB2P-9zmhrA1Q)
- [xlwings库 | Excel与Python的完美结合（附使用文档）](https://mp.weixin.qq.com/s/2_qNnsPK6fjEAUu3jf-NFA)
- [Python-Docx库 | Word与Python的完美结合（附使用文档）](https://mp.weixin.qq.com/s/_QzBRGeXsqF65-xlzQfFjQ)
