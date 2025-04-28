# -*- coding: UTF-8 -*-

from poprogress import simple_progress

for i in simple_progress(range(10000000), desc='当前进度'):
    pass
