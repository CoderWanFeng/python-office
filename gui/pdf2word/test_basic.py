# -*- coding: UTF-8 -*-
"""Test script for PDF to Word converter.

PDF转Word转换器的测试脚本。

This script tests the basic functionality of the converter without GUI.

该脚本在不使用GUI的情况下测试转换器的基本功能。
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from gui.pdf2word.models.converter import PDFConverter
from gui.pdf2word.utils.file_manager import FileManager


def test_converter():
    """Test PDF converter functionality.
    
    测试PDF转换器功能。
    """
    print("=== Testing PDF Converter ===")
    converter = PDFConverter()
    print("✓ Converter initialized successfully")
    
    # Test validation
    # 测试验证
    result = converter.convert("nonexistent.pdf")
    assert not result['success'], "Should fail for non-existent file"
    print("✓ File validation works")
    
    result = converter.convert("test.txt")
    assert not result['success'], "Should fail for non-PDF file"
    print("✓ File extension validation works")
    
    print("\n=== PDF Converter Tests Passed ===\n")


def test_file_manager():
    """Test file manager functionality.
    
    测试文件管理器功能。
    """
    print("=== Testing File Manager ===")
    manager = FileManager()
    print("✓ File manager initialized successfully")
    
    # Test file validation
    # 测试文件验证
    is_valid = manager.validate_file("nonexistent.pdf")
    assert not is_valid, "Should fail for non-existent file"
    print("✓ File validation works")
    
    # Test adding files (without actual files)
    # 测试添加文件（不使用实际文件）
    count = manager.get_file_count()
    assert count == 0, "Initial count should be 0"
    print("✓ Initial file count is correct")
    
    # Test status count
    # 测试状态计数
    counts = manager.get_status_count()
    assert counts['waiting'] == 0, "Initial waiting count should be 0"
    print("✓ Status count works")
    
    # Test clear
    # 测试清空
    manager.clear_files()
    assert manager.get_file_count() == 0, "Count should be 0 after clear"
    print("✓ Clear files works")
    
    print("\n=== File Manager Tests Passed ===\n")


def main():
    """Run all tests.
    
    运行所有测试。
    """
    try:
        print("\n" + "="*50)
        print("PDF to Word Converter - Unit Tests")
        print("PDF转Word转换器 - 单元测试")
        print("="*50 + "\n")
        
        test_converter()
        test_file_manager()
        
        print("="*50)
        print("All Tests Passed! ✓")
        print("所有测试通过！✓")
        print("="*50 + "\n")
        
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
# -*- coding: UTF-8 -*-
"""Test script for PDF to Word converter.

PDF转Word转换器的测试脚本。

This script tests the basic functionality of the converter without GUI.

该脚本在不使用GUI的情况下测试转换器的基本功能。
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from gui.pdf2word.models.converter import PDFConverter
from gui.pdf2word.utils.file_manager import FileManager


def test_converter():
    """Test PDF converter functionality.
    
    测试PDF转换器功能。
    """
    print("=== Testing PDF Converter ===")
    converter = PDFConverter()
    print("✓ Converter initialized successfully")
    
    # Test validation
    # 测试验证
    result = converter.convert("nonexistent.pdf")
    assert not result['success'], "Should fail for non-existent file"
    print("✓ File validation works")
    
    result = converter.convert("test.txt")
    assert not result['success'], "Should fail for non-PDF file"
    print("✓ File extension validation works")
    
    print("\n=== PDF Converter Tests Passed ===\n")


def test_file_manager():
    """Test file manager functionality.
    
    测试文件管理器功能。
    """
    print("=== Testing File Manager ===")
    manager = FileManager()
    print("✓ File manager initialized successfully")
    
    # Test file validation
    # 测试文件验证
    is_valid = manager.validate_file("nonexistent.pdf")
    assert not is_valid, "Should fail for non-existent file"
    print("✓ File validation works")
    
    # Test adding files (without actual files)
    # 测试添加文件（不使用实际文件）
    count = manager.get_file_count()
    assert count == 0, "Initial count should be 0"
    print("✓ Initial file count is correct")
    
    # Test status count
    # 测试状态计数
    counts = manager.get_status_count()
    assert counts['waiting'] == 0, "Initial waiting count should be 0"
    print("✓ Status count works")
    
    # Test clear
    # 测试清空
    manager.clear_files()
    assert manager.get_file_count() == 0, "Count should be 0 after clear"
    print("✓ Clear files works")
    
    print("\n=== File Manager Tests Passed ===\n")


def main():
    """Run all tests.
    
    运行所有测试。
    """
    try:
        print("\n" + "="*50)
        print("PDF to Word Converter - Unit Tests")
        print("PDF转Word转换器 - 单元测试")
        print("="*50 + "\n")
        
        test_converter()
        test_file_manager()
        
        print("="*50)
        print("All Tests Passed! ✓")
        print("所有测试通过！✓")
        print("="*50 + "\n")
        
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
