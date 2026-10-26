from pathlib import Path

import pofile


def main():
    """获取当前目录下的 Python 文件。"""
    files = pofile.get_files(
        path=str(Path(__file__).resolve().parent),
        name="py",
    )
    print("\n".join(files))


if __name__ == "__main__":
    main()