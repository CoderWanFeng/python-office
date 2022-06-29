<p align="center">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://www.python-office.com/api/img-cdn/github-nav.jpg" alt="github license"/>
    </a>   
</p>
<p align="center">
	👉 <a href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a href="https://www.python-office.com/api/img-cdn/python-office.jpg">本开源项目的交流群</a> 👈
</p>


<p align="center" name="'github">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/contributors/CoderWanFeng/python-office" alt="github contributors"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/forks/CoderWanFeng/python-office" alt="github forks"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues/CoderWanFeng/python-office" alt="github issues"/>
    </a>	
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues-pr/CoderWanFeng/python-office" alt="github license"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/license/CoderWanFeng/python-office" alt="github license"/>
    </a>   
</p>

<p align="center" name="gitee">
	<a target="_blank" href='https://gitee.com/CoderWanFeng/python-office/'>
		<img src='https://gitee.com/CoderWanFeng/python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
		<img src="https://gitee.com/CoderWanFeng/python-office/badge/fork.svg?theme=dark" alt="gitee fork"/>
	</a>
	<a href="http://www.python4office.cn/images/qq.jpg">
	<img src="https://img.shields.io/badge/QQ-1090738447-orange"/></a>
</p>





-------------------------------------------------------------------------------

[**🌎English Documentation**](README-EN.md)

-------------------------------------------------------------------------------

## 📚简介

Python-office 是一个 Python 自动化办公第三方库，能解决大部分自动化办公的问题。而且每个功能只需一行代码，不需要小白用户学习 Python 知识，做到了真正的开箱即用。
> 功能持续更新中，提交你的功能需求/参与项目开发，联系👉[开发者微信](http://t.cn/A6XVQXAk)

### 🍺特点
- 一键搭建所有 Python + 自动化办公的编程环境。
- 使用一行代码解决大部分自动化办公的问题，不需要小白学习 Python 知识
- 贴合职场办公需求
- 极简编程，学习成本极低，工作效率提升显著


-------------------------------------------------------------------------------

## 📦安装

### 🍊pip 自动下载&更新

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U
```


-------------------------------------------------------------------------------

## 📝文档

[📘中文文档](https://www.python-office.com/)


[🎬视频介绍](https://www.bilibili.com/video/BV1pT4y1k7FH)


-------------------------------------------------------------------------------

## 🛠️包含组件

以下所有功能，都在逐步搭建中。

| 模块                   |     介绍                                                                          |
| ----------------------|---------------------------------------------------------------------------------- |
| excel                 |     excel处理                                              |
| word                  |     word处理                                              |
| ppt                   |     ppt处理                                                                     |
| pdf                   |     pdf处理                                              |
| file                  |     文件和文件夹的操作                                          |
| tools                 |     便捷小工具                                        |
| web                   |     网站快捷搭建                                         |
| email                 |     邮件功能                                                        |
| image                 |     图片处理            |
| video                 |     视频处理                                          |
| ocr                   |     识别功能：文字识别、语音识别                                                         |

可以根据需求对每个模块单独引入，也可以通过`import office`方式引入所有模块。


-------------------------------------------------------------------------------

## 🏗️添砖加瓦


### 📐PR的建议

python-office欢迎任何人来添砖加瓦，贡献代码，建议提交的pr（pull request）符合一些规范，规范如下：

参与项目建设的步骤：
- 例如：你需要给python-office添加一个add方法。
   1. 你的Github账户名为：demo
   2. 于是你在./contributors新建了文件夹./demo
   3. 新建了add.py文件，编辑你的代码
   4. 编辑完成，提交pr到master分支（gitee或者GitHub，都可以）。可以注明你对自己功能的取名建议
   5. 晚枫收到后，会对各位的代码进行测试后，合并后打包上传到python官方库

### 📐代码规范

1. 注释完备，尤其每个新增的方法应按照Google Python文档规范标明方法说明、参数说明、返回值说明等信息，必要时请添加单元测试，如果愿意，也可以加上你的大名。
2. python-office的文档，需要进行格式化。注意：只能格式化你自己的代码
3. 请直接pull request到`master`分支。`master`是主分支，表示已经发布pypi库的版本。**未来参与人数增多，会开辟新的分支，请留意本文档的更新。**
4. 我们如果关闭了你的issue或pr，请不要诧异，这是我们保持问题处理整洁的一种方式，你依旧可以继续讨论，当有讨论结果时我们会重新打开。


### 🧬贡献代码的步骤

1. 在Gitee或者Github上fork项目到自己的repo
2. 把fork过去的项目也就是你的项目clone到你的本地
3. 修改代码
4. commit后push到自己的库
5. 登录Gitee或Github在你首页可以看到一个 pull request 按钮，点击它，填写一些说明信息，然后提交到master分支即可。
6. 等待维护者合并

### 🎋分支说明

python-office的源码分为两个分支，功能如下：

| 分支       | 作用                                                          |
|-----------|---------------------------------------------------------------|
| master | 主分支，pypi发布版本使用的分支,可以直接pr |
| develop    | 开发分支，供大家各自开发使用                 |

### 🐞提供bug反馈或建议

提交问题反馈时，请务必填写和python-office代码本身有关的问题，不进行有关python学习，甚至是个人练习的知识答疑和讨论。

- [Gitee issue](https://gitee.com/CoderWanFeng/python-office/issues)
- [Github issue](https://github.com/CoderWanFeng/python-office/issues)

-------------------------------------------------------------------------------

## 🪙支持python-office

### 💳捐赠

如果你觉得python-office不错，可以捐赠请维护者喝杯咖啡~，在此表示感谢^_^。

[捐赠给项目](https://gitee.com/CoderWanFeng/python-office) 👈该项捐赠仅用于支持本项目发展使用

[捐赠给程序员晚枫](http://python4office.cn/images/wechat-pay.jpg)


-------------------------------------------------------------------------------

## ⭐Star python-office

[![Stargazers over time](https://starchart.cc/CoderWanFeng/python-office.svg)](https://starchart.cc/CoderWanFeng/python-office)

## 📌公众号&开源小组

<div align="center">
	<img src="http://www.python4office.cn/images/account-display/10-gzh.jpg" height="150">
	<img src="https://www.python-office.com/api/img-cdn/python-office.jpg" height="150">
</div>
