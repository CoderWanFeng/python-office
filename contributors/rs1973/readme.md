# 批量图片尺寸与通道处理工具

**Creator:** rs1973  
**E-mail:** dingzheng_2023@qq.com / gunshi98@gmail.com  

本工具支持对 **单张图片** 或 **整个目录的全部图片** 进行批量处理，包括：

- 调整图片尺寸
- 统一色彩通道（可选择去除或保留透明通道 alpha）
- 批量导出到指定目录
- 支持 `.jpg / .jpeg / .png / .bmp / .tiff / .webp` 格式
- 支持 GIF 合成（单线程）

程序内部使用 **多线程** 加速大量图片处理,默认为5线程。

---

##  功能特点

| 功能 | 说明                                                             |
|-----|----------------------------------------------------------------|
| 批量筛选图片 | 自动忽略非图片文件                                                      |
| 多线程处理 | 提升处理速度,默认为5线程                                                  |
| 支持保留 / 去除透明通道 | 当输出格式支持alpha,可以选择保留或丢弃,丢弃时会将原本的alpha像素替换成白色(后续会添加颜色选择选项)       |
| 自适应缩放或填充模式 | 保证目标尺寸一致：当目标大小小于原图时,会缩放/拉伸原图,大于且长宽比例与目标大小相同时,则直接缩放,反之则会用白色填充图片 |
| GIF 合成 | 可根据延迟参数调节帧率,默认300ms/帧                                          |

---

##  基本使用示例

```python
from contributors.rs1973.process_img1.py import main

src = r"C:\path\to\input_dir"
out = r"C:\path\to\output_dir"
size = (1000, 1000)

main(
    srcpath=src,
    outpath=out,
    img_size=size,
    alpha=False,      # 是否保留透明通道
    kind='.png',      # 输出格式
    duration=300      # GIF 合成时的帧间隔，仅在 kind='.gif' 时使用
)