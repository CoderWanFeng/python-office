# python-office 构建版本



## 1 关于本分支

此项目源代码并非由 SmallPigPig 书写（即本文档作者），我仅是为自己喜欢的项目提供更方便的使用方式

### 1.1 本分支的用途

本分支旨在为开发者提供更灵活的选择以及为用户提供更方便的使用方式

该说明文档将会教您如何打包属于您自己的 python-office 可执行文件，打包指令和逻辑通用，希望能帮助到您

**您可以获得到：**

- 打包程序的方式与指令
- 已经构建好的 python-office



## 2 准备工作

### 2.1 下载源码

**源码链接：**[python-office gui 分支](https://github.com/CoderWanFeng/python-office/tree/gui)

<img src="python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405124426102.png" alt="image-20230405124426102" style="zoom:80%;" />

打开后将源码下载下来，并打开文件夹

![image-20230405124514185](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405124514185.png)

### 2.2 部署项目

为了让打包顺利进行，我们先确保源码能正常运行

一般来说，源码能运行打包后的构建版本（exe）也不会有太大问题

因此让我们先安装环境吧！

建议使用 **Pycharm** 创建虚拟环境。目前 Nuitka（打包工具）支持并不完善，建议使用虚拟环境以避免导入不需要的包

![image-20230405124756021](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405124756021.png)

打开终端，输入 `pip install -r requirements.txt`

等待跑码完成

> **注意：**
>
> - 在跑码过程中，部分库的安装依赖于“Microsoft C++Build Tools”（C++ 生成工具），如果缺失会提醒您下载。依照它给出的链接下载即可
> - 如果打包过程中出现 `no module named "xxx"`导致环境部署终止的话，输入`pip install xxx`（xxx 就是刚刚提示缺失的库名）即可解决问题



### 2.3 安装工具

我们的打包依赖于一个十分好用的打包工具：**Nuitka**

为了方便下一步操作，让我们安装一下它

![image-20230405125545921](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405125545921.png)

输入 `pip install Nuitka`，等待跑码完成

> 如果下载 Nuitka 太慢，使用这个指令：`pip install Nuitka -i https://pypi.tuna.tsinghua.edu.cn/simple`

下载完成后，使用 `Nuitka --version` 检查是否成功

#### 2.3.1  可能遇到的问题

首次安装 Nuitka 打包时会初始化下载工具包。国内下载可能较慢或者无法下载，如果遇到此类问题请下载 [Nuitka 环境下载](https://pan.baidu.com/s/1CpdGxZj2hRsU_Z0ukp6kqg&pwd=8888) 中的以下文件

![image-20230405130427827](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405130427827.png)

下载完成后注意配置环境变量，例如我的保存在 D:\ 文件夹下

![image-20230405130618489](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405130618489.png)

`Win + S` 搜索 **高级系统设置**

![image-20230405130730961](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405130730961.png)

点击环境变量

![image-20230405130809007](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405130809007.png)

点击 Path

![image-20230405130838660](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405130838660.png)

根据实际情况写路径（即你把解压出来的文件的保存路径）

![image-20230405130919931](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405130919931.png)

一路点确定保存设置，之后输入 `gcc --version` 检查是否成功

![image-20230405131059290](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405131059290.png)



## 3 开始打包

### 3.1 生成构建文件

让我们开始吧！请注意，我给出的指令不一定适用于您所使用的系统，请根据系统情况自行调整

![image-20230405131211283](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405131211283.png)

输入`nuitka --standalone --show-progress --enable-plugin=pyqt5 --windows-icon-from-ico=icon.ico main.py --mingw64 --nofollow-import-to=tkinter  --include-module=qt_material --disable-console`，按下回车，正常来说就在跑码了

![image-20230405131305018](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405131305018.png)

下面让我们来看看这段指令的意思

- **Nuitka：**没什么好说的，打包工具而已
- **standalone：**怎么解释呢·······这么说吧，就相当于集成了一个 python 在里边。这样对方就算没有 python 也可以运行
- **show-progress：**显示进度
- **enable-plugin=pyqt5：**这是一个 pyqt5 项目，所以我们要让 Nuitka 搜索 pyqt5 的相关依赖
- **windows-icon-from-ico=icon.ico：**设置程序图标
- **main.py：**指定程序主入口（即要打包的文件）
- **mingw64：**是一个可自由使用和自由发布的Windows特定头文件和使用GNU工具集导入库的集合，建议开启（默认启用）
- **nofollow-import-to=tkinter：**既然是 pyqt5，那就不用导入 tkinter 了，把它给移除节省空间
- **include-module=qt_material：**额外引用 qt_material。这个库是作者 gui 界面的皮肤，但这个选项似乎不起作用
- **disable-console：**禁用控制台，这样就不会有个黑窗口和你的程序一起运行

如果你打包成功了，在项目下会多出这两个文件夹

![image-20230405133052810](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133052810.png)



### 3.2 补全缺失内容

点开 **main.dist**，另一个不用管，是打包的缓存

![image-20230405133149729](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133149729.png)

由于有一些文件是需要的但引用的方式不能被 Nuitka 检测出来，所以我们需要手动补全

![image-20230405133251908](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133251908.png)

把这些文件复制

![image-20230405133316963](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133316963.png)

粘贴进目录



其次，我们需要补全 gui 的主题：`qt_material`



![image-20230405133410697](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133410697.png)

打开 venv 



![image-20230405133520855](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133520855.png)

点 `Lib`，`site-packages`，进入到库文件保存位置

> 如果您没有使用 pycharm 进行打包，请自行搜索 python 库安装位置

![image-20230405133650070](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133650070.png)

搜索 `qt_material`，复制第一个（不要选 `xxx.dist-info` ！那个不是库文件本体！）

![image-20230405133827282](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133827282.png)

粘贴回 main.dist，理论上来说你就可以正常使用了

![image-20230405133914439](python-office%20%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC.assets/image-20230405133914439.png)

点击 **main.exe**，就可以看到这样的界面啦！快把你打包好的程序分享给你需要的朋友吧！