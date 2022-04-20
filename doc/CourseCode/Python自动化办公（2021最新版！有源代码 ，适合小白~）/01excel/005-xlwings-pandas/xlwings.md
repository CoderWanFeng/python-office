### 为什么是xlwings ？

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/SAHDhZ6pPOibuS0xkxf1HGCtV1KxmOy2ic2qcAEQxDSsa1icC6on0bibkxBRHPxgqZ3rVuI4UnwGcscibcpO3Ifwzjg/640?wx_fmt=jpeg)

之前给大家整理过Python用来处理Excel的全部可用库，以及它们的优缺点：[全解析！9个处理Excel的Python库，到底哪个最好用？](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247489016&idx=1&sn=189adc7795cebc6e71543d6bbeebb735&chksm=eaf6b4cddd813ddb53f2db0e1e901e293569b2292179801dc73223799e5ea90d4dfe049b30a9#rd)

> 每个人来学习都是想一步到位，不会考虑那些功能不全的库。

这其中最强大的库是Pandas，之前已经给大家推荐过相关的课程和全部文档了。大家可以去免费i学习~

除了Pandas，只有两个库：**xlwings**和win32com，具有全部操作权限，然而win32com，因为各种技术原因在使用中经常出难解决的问题。所以只剩下xlwings是最佳选项了。

#### xlwings具有以下优点：

- xlwings能够非常方便的读写Excel文件中的数据，并且能够进行单元格格式的修改
- 可以和matplotlib以及pandas无缝连接
- 可以调用Excel文件中VBA写好的程序，也可以让VBA调用用Python写的程序。
- 开源免费，一直在更新

我们今天就来讲解一下，xlwings如何使用~

> xlwings的详细官方使用文档，获取方式见文末~



### 安装

工欲善其事必先利其器，

如果是在开始xlwings之前，您还没有安装Python+开发工具，请花10分钟的时间，移步此链接：链接，先把Python+开发工具，可以吗？安装过程中，有问题可以来交流群提问：交流群

#### Python环境下安装（推荐）

```
pip install xlwings
```

#### Anaconda环境下安装

```
conda install xlwings
```
不推荐使用anaconda
    - 这个东西很大，100库，但是和自动化办公无关
        - 8G，2G，100库
    - anaconda独立的编程环境，这套课很多技术不能用
        - 多学一些无用知识，浪费时间

### 使用演示

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91cGxvYWQtaW1hZ2VzLmppYW5zaHUuaW8vdXBsb2FkX2ltYWdlcy8yOTc5MTk2LTRhMmFiMGJhZjllMjZkNjcucG5n?x-oss-process=image/format,png)

#### 1、打开/新建Excel文档

```python
import xlwings as xw
wb = xw.Book()  # 新建一个文档
wb = xw.Book('test.xlsx')  # 打开一个已有的文档
```

#### 2、读取/写入数据

```python
sht = wb.sheets['Sheet1'] # 找到指定sheet
print(sht.range('A1').value) # 读取指定单元格的数据，这里读的是A1
sht.range('B1').value = 10 # 给指定的空白单元格赋值，这里赋值的是B1
```

#### 3、保存文件、退出程序

```python
wb.save(r'test.xlsx') #保存Excel文档，命名为test.xlsx，并保存在D盘
wb.close() # 退出程序，该步骤不可省略
```

#### 4、连接pandas处理复杂数据

```python
import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
sht.range('A1').value = df
sht.range('A1').options(pd.DataFrame, expand='table').value
```

#### 5、连接**Matplotlib** 画图

```python
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sht.pictures.add(fig, name='MyPlot', update=True)
```



### 其他资源

可以在Python-Docx的GitHub页面上找到更多示例代码。