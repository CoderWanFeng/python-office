# -*- coding: UTF-8 -*-
"""
python-office Skills 模块

将 python-office 库的所有方法封装为独立的 Skill（技能），
每个 Skill 都是一个独立的子目录，可以单独调用。

使用方式：
    from skills.excel import fake2excel
    fake2excel(rows=10)

    from skills.image import add_watermark
    add_watermark(file='test.png', mark='python-office')

详细功能列表见本目录下的 README.md。
"""
