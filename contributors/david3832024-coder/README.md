# Batch Image Converter

This contribution adds a Pillow-based helper for batch image conversion.

## Features

- Convert JPG, PNG, BMP, WEBP, TIFF, and GIF files in batch.
- Optionally resize images to a fixed canvas.
- Preserve RGBA transparency for formats that support it.
- Fill resized images with white or transparent background.
- Create animated GIF files with configurable frame duration.

## Install dependency

```bash
pip install Pillow
```

## Command line usage

Convert all images in a folder to PNG:

```bash
python batch_image_converter.py convert ./images ./output --format png
```

Convert to WEBP and resize to an 800x600 canvas:

```bash
python batch_image_converter.py convert ./images ./output --format webp --size 800x600
```

Create an animated GIF:

```bash
python batch_image_converter.py gif ./images ./output/demo.gif --duration 300
```

## Python usage

```python
from batch_image_converter import convert_images, create_gif

convert_images(
    input_path="./images",
    output_dir="./output",
    output_format="png",
    size=(800, 600),
    background="transparent",
)

create_gif(
    input_path="./images",
    output_file="./output/demo.gif",
    duration=300,
    size=(800, 600),
)
```
