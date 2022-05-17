## 如何使用

```python
from contributors.CNSeniorious000.pdf import PDF

# 将sample.pdf中的所有页面以300ppi的分辨率导出为jpg到output文件夹
PDF("sample.pdf").save_images("output", encode="jpg", dpi=300)
```

## 整体结构

- `pdf.py`是对pdf栅格化的相关工具
- `ocr.py`是对图片ocr的一些常用封装
- `tests`文件夹下是单元测试，使用`pytest`框架
    - 测试样例在`PyCharm`中运行，其他方式运行会