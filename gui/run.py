# -*- coding: utf-8 -*-
"""启动入口：``python -m gui.run`` 或 ``python-office-gui``。"""

import os
import sys
import importlib
from pathlib import Path

sys.dont_write_bytecode = True
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")


def _runtime_log(base: Path, message: str) -> None:
    if not os.environ.get("PYTHON_OFFICE_GUI_DEBUG"):
        return
    try:
        with (base / "python-office-gui-runtime.log").open(
            "a", encoding="utf-8"
        ) as fh:
            fh.write(message.rstrip() + "\n")
    except OSError:
        pass


def _prepare_bundled_runtime() -> None:
    """Allow Nuitka standalone builds to load copied pure/binary packages.

    The build script places large third-party packages in ``<dist>/lib`` so
    they can remain normal Python packages instead of being compiled into C.
    """
    base = Path(sys.executable).resolve().parent
    lib_dir = base / "lib"
    if not lib_dir.is_dir():
        return

    lib_path = str(lib_dir)
    if lib_path not in sys.path:
        sys.path.insert(0, lib_path)
    for extra in (
        lib_dir / "win32",
        lib_dir / "win32" / "lib",
        lib_dir / "site-packages" / "win32" / "lib",
    ):
        if extra.is_dir():
            extra_path = str(extra)
            if extra_path not in sys.path:
                sys.path.insert(0, extra_path)
    os.environ["PATH"] = lib_path + os.pathsep + os.environ.get("PATH", "")

    dll_dirs = [lib_dir]
    for child_name in (
        "numpy.libs",
        "pandas.libs",
        "cv2",
        "PIL",
        "pymupdf",
        "pywin32_system32",
        "win32",
    ):
        child = lib_dir / child_name
        if child.is_dir():
            dll_dirs.append(child)

    add_dll_directory = getattr(os, "add_dll_directory", None)
    for dll_dir in dll_dirs:
        dll_path = str(dll_dir)
        os.environ["PATH"] = dll_path + os.pathsep + os.environ.get("PATH", "")
        if add_dll_directory is not None:
            try:
                add_dll_directory(dll_path)
            except OSError as exc:
                _runtime_log(base, f"add_dll_directory failed: {dll_path}: {exc}")

    _runtime_log(base, f"bundled lib enabled: {lib_dir}")
    _runtime_log(base, "dll dirs: " + "; ".join(str(p) for p in dll_dirs))


_prepare_bundled_runtime()


def _run_self_test() -> int:
    base = Path(sys.executable).resolve().parent
    modules = [
        "office.api.pdf",
        "office.api.excel",
        "office.api.word",
        "office.api.ppt",
        "office.api.image",
        "office.api.file",
        "office.api.video",
        "office.api.email",
        "office.api.tools",
        "popdf",
        "poexcel",
        "poword",
        "poppt",
        "poimage",
        "pofile",
        "povideo",
        "poemail",
        "wftools",
        "numpy",
        "pandas",
        "fitz",
        "cv2",
        "PIL",
    ]
    failures = []
    for module_name in modules:
        try:
            importlib.import_module(module_name)
        except Exception as exc:
            failures.append(f"{module_name}: {exc!r}")

    log_path = base / "python-office-gui-self-test.log"
    with log_path.open("w", encoding="utf-8") as fh:
        if failures:
            fh.write("FAILED\n")
            fh.write("\n".join(failures))
            fh.write("\n")
        else:
            fh.write("OK\n")
    return 1 if failures else 0


if "--self-test" in sys.argv:
    sys.exit(_run_self_test())


def _run_startup_probe() -> int:
    import time

    base = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path.cwd()
    start = time.perf_counter()
    from gui.app import create_app
    from gui.main_window import MainWindow

    app = create_app([])
    window = MainWindow()
    elapsed = time.perf_counter() - start
    with (base / "python-office-gui-startup-probe.log").open("w", encoding="utf-8") as fh:
        fh.write(f"{elapsed:.3f}\n")
    window.deleteLater()
    app.quit()
    return 0


if "--startup-probe" in sys.argv:
    sys.exit(_run_startup_probe())

from gui.app import main

if __name__ == "__main__":
    sys.exit(main())
