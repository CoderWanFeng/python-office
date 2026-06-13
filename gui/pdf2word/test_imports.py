# -*- coding: UTF-8 -*-
"""Test imports for PDF to Word converter GUI.

PDF转Word转换器GUI的导入测试。

This script tests if all modules can be imported correctly.

该脚本测试所有模块是否可以正确导入。
"""

import sys
from pathlib import Path

# Add parent directory to path
# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

print("\n" + "="*50)
print("Testing Module Imports")
print("测试模块导入")
print("="*50 + "\n")

try:
    print("Importing models...")
    from gui.pdf2word.models.converter import PDFConverter
    print("✓ models.converter imported successfully")
    
    print("\nImporting utils...")
    from gui.pdf2word.utils.file_manager import FileManager
    print("✓ utils.file_manager imported successfully")
    
    print("\nImporting views (requires PyQt5)...")
    try:
        from gui.pdf2word.views.main_window import MainWindow
        print("✓ views.main_window imported successfully")
    except ImportError as e:
        print(f"⚠ views.main_window import failed: {e}")
        print("  Note: PyQt5 may not be installed. Install with: pip install PyQt5")
    
    print("\nImporting controllers (requires PyQt5)...")
    try:
        from gui.pdf2word.controllers.converter_controller import ConverterController
        print("✓ controllers.converter_controller imported successfully")
    except ImportError as e:
        print(f"⚠ controllers.converter_controller import failed: {e}")
        print("  Note: PyQt5 may not be installed. Install with: pip install PyQt5")
    
    print("\n" + "="*50)
    print("Import Test Completed!")
    print("导入测试完成！")
    print("="*50 + "\n")
    
except Exception as e:
    print(f"\n✗ Import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
# -*- coding: UTF-8 -*-
"""Test imports for PDF to Word converter GUI.

PDF转Word转换器GUI的导入测试。

This script tests if all modules can be imported correctly.

该脚本测试所有模块是否可以正确导入。
"""

import sys
from pathlib import Path

# Add parent directory to path
# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

print("\n" + "="*50)
print("Testing Module Imports")
print("测试模块导入")
print("="*50 + "\n")

try:
    print("Importing models...")
    from gui.pdf2word.models.converter import PDFConverter
    print("✓ models.converter imported successfully")
    
    print("\nImporting utils...")
    from gui.pdf2word.utils.file_manager import FileManager
    print("✓ utils.file_manager imported successfully")
    
    print("\nImporting views (requires PyQt5)...")
    try:
        from gui.pdf2word.views.main_window import MainWindow
        print("✓ views.main_window imported successfully")
    except ImportError as e:
        print(f"⚠ views.main_window import failed: {e}")
        print("  Note: PyQt5 may not be installed. Install with: pip install PyQt5")
    
    print("\nImporting controllers (requires PyQt5)...")
    try:
        from gui.pdf2word.controllers.converter_controller import ConverterController
        print("✓ controllers.converter_controller imported successfully")
    except ImportError as e:
        print(f"⚠ controllers.converter_controller import failed: {e}")
        print("  Note: PyQt5 may not be installed. Install with: pip install PyQt5")
    
    print("\n" + "="*50)
    print("Import Test Completed!")
    print("导入测试完成！")
    print("="*50 + "\n")
    
except Exception as e:
    print(f"\n✗ Import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
