"""Batch image conversion helper based on Pillow.

Features:
- convert images between JPG, PNG, BMP, WEBP, TIFF, and GIF
- resize images with optional aspect-ratio padding
- preserve RGBA when the target format supports transparency
- compose multiple images into an animated GIF
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

from PIL import Image, ImageSequence


SUPPORTED_FORMATS = {"jpg", "jpeg", "png", "bmp", "webp", "tiff", "gif"}
TRANSPARENT_FORMATS = {"png", "webp", "tiff", "gif"}


def _normalize_format(image_format: str) -> str:
    image_format = image_format.lower().lstrip(".")
    if image_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported image format: {image_format}")
    return "jpeg" if image_format == "jpg" else image_format


def _parse_size(size: Optional[str]) -> Optional[Tuple[int, int]]:
    if not size:
        return None
    width, height = size.lower().split("x", maxsplit=1)
    return int(width), int(height)


def _background_color(mode: str, background: str):
    if background == "transparent":
        return (255, 255, 255, 0) if mode == "RGBA" else 0
    return "white"


def _iter_image_files(input_path: Path, include_subfolders: bool = False) -> List[Path]:
    if input_path.is_file():
        return [input_path]

    pattern = "**/*" if include_subfolders else "*"
    files = [
        file_path
        for file_path in input_path.glob(pattern)
        if file_path.is_file()
        and file_path.suffix.lower().lstrip(".") in SUPPORTED_FORMATS
    ]
    return sorted(files)


def _flatten_alpha(image: Image.Image, background: str = "white") -> Image.Image:
    if image.mode not in ("RGBA", "LA"):
        return image.convert("RGB")

    rgba_image = image.convert("RGBA")
    canvas = Image.new("RGBA", rgba_image.size, _background_color("RGBA", background))
    canvas.alpha_composite(rgba_image)
    return canvas.convert("RGB")


def _resize_with_canvas(
    image: Image.Image,
    size: Optional[Tuple[int, int]],
    background: str = "white",
    keep_aspect_ratio: bool = True,
) -> Image.Image:
    if size is None:
        return image.copy()

    if not keep_aspect_ratio:
        return image.resize(size, Image.LANCZOS)

    resized = image.copy()
    resized.thumbnail(size, Image.LANCZOS)
    mode = "RGBA" if resized.mode in ("RGBA", "LA") else "RGB"
    canvas = Image.new(mode, size, _background_color(mode, background))
    left = (size[0] - resized.width) // 2
    top = (size[1] - resized.height) // 2

    if resized.mode in ("RGBA", "LA"):
        canvas.paste(resized.convert("RGBA"), (left, top), resized.convert("RGBA"))
    else:
        canvas.paste(resized.convert(mode), (left, top))

    return canvas


def _prepare_image(
    image: Image.Image,
    output_format: str,
    size: Optional[Tuple[int, int]] = None,
    background: str = "white",
    keep_aspect_ratio: bool = True,
) -> Image.Image:
    first_frame = next(ImageSequence.Iterator(image)).copy()
    first_frame = _resize_with_canvas(
        first_frame, size=size, background=background, keep_aspect_ratio=keep_aspect_ratio
    )

    if output_format not in TRANSPARENT_FORMATS:
        return _flatten_alpha(first_frame, background=background)

    if first_frame.mode not in ("RGBA", "RGB"):
        first_frame = first_frame.convert("RGBA")
    return first_frame


def convert_images(
    input_path: str,
    output_dir: str,
    output_format: str = "png",
    size: Optional[Tuple[int, int]] = None,
    background: str = "white",
    keep_aspect_ratio: bool = True,
    include_subfolders: bool = False,
    overwrite: bool = True,
) -> List[Path]:
    """Batch-convert images and return generated file paths."""
    source = Path(input_path)
    target_dir = Path(output_dir)
    output_format = _normalize_format(output_format)
    target_dir.mkdir(parents=True, exist_ok=True)

    output_files: List[Path] = []
    for image_file in _iter_image_files(source, include_subfolders=include_subfolders):
        output_file = target_dir / f"{image_file.stem}.{output_format}"
        if output_file.exists() and not overwrite:
            continue

        with Image.open(image_file) as image:
            converted = _prepare_image(
                image,
                output_format=output_format,
                size=size,
                background=background,
                keep_aspect_ratio=keep_aspect_ratio,
            )
            converted.save(output_file, format=output_format.upper())

        output_files.append(output_file)

    return output_files


def create_gif(
    input_path: str,
    output_file: str,
    duration: int = 500,
    size: Optional[Tuple[int, int]] = None,
    background: str = "white",
    include_subfolders: bool = False,
    loop: int = 0,
) -> Path:
    """Create an animated GIF from images in a file or directory."""
    image_files = _iter_image_files(Path(input_path), include_subfolders=include_subfolders)
    if not image_files:
        raise ValueError("No images found for GIF creation.")

    frames = []
    for image_file in image_files:
        with Image.open(image_file) as image:
            frame = _prepare_image(
                image,
                output_format="gif",
                size=size,
                background=background,
                keep_aspect_ratio=True,
            )
            frames.append(frame.convert("P", palette=Image.ADAPTIVE))

    gif_path = Path(output_file)
    gif_path.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=loop,
    )
    return gif_path


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Batch image converter based on Pillow.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    convert_parser = subparsers.add_parser("convert", help="Batch convert image format.")
    convert_parser.add_argument("input_path", help="Input file or directory.")
    convert_parser.add_argument("output_dir", help="Directory for converted images.")
    convert_parser.add_argument("--format", default="png", help="Output format.")
    convert_parser.add_argument("--size", help="Resize target, for example 800x600.")
    convert_parser.add_argument("--background", default="white", choices=["white", "transparent"])
    convert_parser.add_argument("--stretch", action="store_true", help="Resize without padding.")
    convert_parser.add_argument("--include-subfolders", action="store_true")
    convert_parser.add_argument("--skip-existing", action="store_true")

    gif_parser = subparsers.add_parser("gif", help="Create animated GIF from images.")
    gif_parser.add_argument("input_path", help="Input file or directory.")
    gif_parser.add_argument("output_file", help="Output GIF path.")
    gif_parser.add_argument("--duration", type=int, default=500, help="Frame duration in ms.")
    gif_parser.add_argument("--size", help="Resize target, for example 800x600.")
    gif_parser.add_argument("--background", default="white", choices=["white", "transparent"])
    gif_parser.add_argument("--include-subfolders", action="store_true")

    return parser


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = _build_parser().parse_args(argv)
    size = _parse_size(args.size)

    if args.command == "convert":
        results = convert_images(
            input_path=args.input_path,
            output_dir=args.output_dir,
            output_format=args.format,
            size=size,
            background=args.background,
            keep_aspect_ratio=not args.stretch,
            include_subfolders=args.include_subfolders,
            overwrite=not args.skip_existing,
        )
        print(f"Converted {len(results)} image(s).")
        return

    gif_path = create_gif(
        input_path=args.input_path,
        output_file=args.output_file,
        duration=args.duration,
        size=size,
        background=args.background,
        include_subfolders=args.include_subfolders,
    )
    print(f"Created GIF: {gif_path}")


if __name__ == "__main__":
    main()
