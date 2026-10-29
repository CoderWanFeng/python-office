# 导入兼容性检查模块（必须在其他导入之前）
from office.compatibility import check_compatibility

# 执行兼容性检查
compatibility_checker = check_compatibility()

# Python >= 3.7：api 模块按需懒加载（PEP 562），`import office` 不再拖入
# 整个 po* 依赖树——只用 pdf 的用户无需安装 povideo/poocr 等重型依赖。
# 首次访问 office.pdf / office.excel 等属性时才导入对应模块，
# `import office` + `office.pdf.xxx()` 与 `from office import pdf` 等既有用法不变。
import sys

if sys.version_info >= (3, 7):
    import importlib

    _LAZY_MODULES = {
        name: "office.api." + name
        for name in (
            "email", "excel", "file", "finance", "image", "pdf", "ppt",
            "tools", "video", "web", "wechat", "word", "markdown", "ocr",
        )
    }
    _LAZY_MODULES["api"] = "office.api"
    # 以下是beta版本
    _LAZY_MODULES["ruiming"] = "office.api.testApi.ruiming"

    def __getattr__(name):
        module_path = _LAZY_MODULES.get(name)
        if module_path is None:
            raise AttributeError("module 'office' has no attribute %r" % name)
        module = importlib.import_module(module_path)
        globals()[name] = module  # 缓存，后续访问零开销
        return module

    def __dir__():
        return sorted(set(globals()) | set(_LAZY_MODULES))

    # 保持 `from office import *` 与急切导入时代一致
    __all__ = sorted(_LAZY_MODULES)
else:
    # Python 3.6 无 PEP 562，保持原有的急切导入
    from office.api import email
    from office.api import excel
    from office.api import file
    from office.api import finance
    from office.api import image
    from office.api import pdf
    from office.api import ppt
    from office.api import tools
    from office.api import video
    from office.api import web
    from office.api import wechat
    from office.api import word
    from office.api import markdown
    from office.api import ocr
    # 以下是beta版本
    from office.api.testApi import ruiming

__doc__ = """【python-office库】，功能持续更新中
使用有问题 or 提交你的功能需求 or 参与项目开发
1、项目【官方文档】：https://www.python-office.com
2、请+【项目交流群】：https://www.python4office.cn/wechat-group
3、本开源项目的【源代码】：https://github.com/CoderWanFeng/python-office"""

__version__ = '1.1.2'
