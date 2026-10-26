# -*- coding: UTF-8 -*-
"""excel2json Skill - 把 Excel 工作表转换成 JSON。

实现代码位于 contributors/my12yyds/，该目录不随 python-office 包一起发布
（setup.cfg 的 packages = find: 只收集带 __init__.py 的目录），
所以这里用 try/except 兜底：源码仓库中可直接导入，安装包中调用时给出明确提示。
"""

try:
    from contributors.my12yyds.excel2json import excel2json
except ImportError as _import_error:  # pragma: no cover - 仅在安装包环境触发
    # except 块结束后 Python 会自动 del 掉 as 绑定的异常名，
    # 因此把它存到模块级变量，供下面的兜底函数保留异常链。
    _CONTRIBUTORS_IMPORT_ERROR = _import_error

    def excel2json(*args, **kwargs):
        """未找到贡献者实现时的兜底函数。

        Raises:
            ImportError: 该 Skill 的实现位于源码仓库的 contributors 目录中。
        """
        raise ImportError(
            '该 Skill 的实现位于仓库的 contributors/my12yyds/excel2json.py，'
            '该目录不随 python-office 一起发布。'
            '请克隆源码仓库后使用，或直接复制该文件到项目中。'
        ) from _CONTRIBUTORS_IMPORT_ERROR


__all__ = ['excel2json']
