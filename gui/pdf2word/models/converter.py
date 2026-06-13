# -*- coding: UTF-8 -*-
"""PDF to Word converter module.

PDF转Word转换器模块。

This module provides the core conversion functionality using office.pdf.pdf2docx API.

该模块使用office.pdf.pdf2docx API提供核心转换功能。
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import office module
# 添加父目录到路径以导入office模块
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

import office


class PDFConverter:
    """PDF to Word converter class.
    
    PDF转Word转换器类。
    
    This class encapsulates the PDF to Word conversion logic and provides methods
    for converting single or multiple PDF files to Word documents.
    
    该类封装了PDF转Word的转换逻辑，提供转换单个或多个PDF文件为Word文档的方法。
    """
    
    def __init__(self):
        """Initialize the PDF converter.
        
        初始化PDF转换器。
        """
        pass
    
    def convert(self, input_file, output_path=None):
        """Convert a PDF file to Word document.
        
        将PDF文件转换为Word文档。
        
        Args:
            input_file (str): path to the input PDF file / 输入PDF文件的路径
            output_path (str, optional): output directory path / 输出目录路径。Default / 默认: None (same as input directory / 与输入文件同目录)
        
        Returns:
            dict: conversion result containing status and message / 包含状态和消息的转换结果
                {
                    'success': bool,
                    'message': str,
                    'output_file': str (if success)
                }
        
        Raises:
            Exception: if conversion fails / 如果转换失败
        
        Examples:
            >>> converter = PDFConverter()
            >>> result = converter.convert('test.pdf', 'output/')
            >>> print(result['success'])
            True
        """
        try:
            # Validate input file exists
            # 验证输入文件存在
            if not os.path.exists(input_file):
                return {
                    'success': False,
                    'message': f'文件不存在: {input_file}'
                }
            
            # Validate file extension
            # 验证文件扩展名
            if not input_file.lower().endswith('.pdf'):
                return {
                    'success': False,
                    'message': f'文件格式错误，仅支持PDF格式'
                }
            
            # Determine output path
            # 确定输出路径
            if output_path is None:
                output_path = os.path.dirname(input_file)
            
            # Create output directory if not exists
            # 如果输出目录不存在则创建
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            
            # Perform conversion using office.pdf.pdf2docx
            # 使用office.pdf.pdf2docx执行转换
            office.pdf.pdf2docx(input_file, output_path)
            
            # Determine output file path
            # 确定输出文件路径
            input_filename = os.path.basename(input_file)
            output_filename = os.path.splitext(input_filename)[0] + '.docx'
            output_file = os.path.join(output_path, output_filename)
            
            # Verify output file was created
            # 验证输出文件已创建
            if os.path.exists(output_file):
                return {
                    'success': True,
                    'message': '转换成功',
                    'output_file': output_file
                }
            else:
                return {
                    'success': False,
                    'message': '转换完成但未找到输出文件'
                }
                
        except PermissionError as e:
            return {
                'success': False,
                'message': f'权限错误: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'转换失败: {str(e)}'
            }
    
    def batch_convert(self, file_list, output_path=None, progress_callback=None):
        """Convert multiple PDF files to Word documents.
        
        将多个PDF文件转换为Word文档。
        
        This method processes a list of PDF files sequentially and converts each
        to Word format. It supports progress callback for UI updates.
        
        该方法按顺序处理PDF文件列表，将每个文件转换为Word格式。支持进度回调以更新UI。
        
        Args:
            file_list (list): list of PDF file paths / PDF文件路径列表
            output_path (str, optional): output directory path / 输出目录路径。Default / 默认: None
            progress_callback (callable, optional): callback function for progress updates / 进度更新回调函数
                Signature: callback(current_index, total_count, current_file, result)
        
        Returns:
            dict: batch conversion summary / 批量转换摘要
                {
                    'total': int,
                    'success': int,
                    'failed': int,
                    'results': list of conversion results
                }
        
        Examples:
            >>> converter = PDFConverter()
            >>> files = ['file1.pdf', 'file2.pdf']
            >>> summary = converter.batch_convert(files, 'output/')
            >>> print(f"成功: {summary['success']}, 失败: {summary['failed']}")
            成功: 2, 失败: 0
        """
        total = len(file_list)
        success_count = 0
        failed_count = 0
        results = []
        
        for index, file_path in enumerate(file_list):
            # Convert single file
            # 转换单个文件
            result = self.convert(file_path, output_path)
            
            # Update counters
            # 更新计数器
            if result['success']:
                success_count += 1
            else:
                failed_count += 1
            
            results.append({
                'file': file_path,
                'result': result
            })
            
            # Call progress callback if provided
            # 如果提供了进度回调则调用
            if progress_callback:
                progress_callback(index + 1, total, file_path, result)
        
        return {
            'total': total,
            'success': success_count,
            'failed': failed_count,
            'results': results
        }
# -*- coding: UTF-8 -*-
"""PDF to Word converter module.

PDF转Word转换器模块。

This module provides the core conversion functionality using office.pdf.pdf2docx API.

该模块使用office.pdf.pdf2docx API提供核心转换功能。
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import office module
# 添加父目录到路径以导入office模块
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

import office


class PDFConverter:
    """PDF to Word converter class.
    
    PDF转Word转换器类。
    
    This class encapsulates the PDF to Word conversion logic and provides methods
    for converting single or multiple PDF files to Word documents.
    
    该类封装了PDF转Word的转换逻辑，提供转换单个或多个PDF文件为Word文档的方法。
    """
    
    def __init__(self):
        """Initialize the PDF converter.
        
        初始化PDF转换器。
        """
        pass
    
    def convert(self, input_file, output_path=None):
        """Convert a PDF file to Word document.
        
        将PDF文件转换为Word文档。
        
        Args:
            input_file (str): path to the input PDF file / 输入PDF文件的路径
            output_path (str, optional): output directory path / 输出目录路径。Default / 默认: None (same as input directory / 与输入文件同目录)
        
        Returns:
            dict: conversion result containing status and message / 包含状态和消息的转换结果
                {
                    'success': bool,
                    'message': str,
                    'output_file': str (if success)
                }
        
        Raises:
            Exception: if conversion fails / 如果转换失败
        
        Examples:
            >>> converter = PDFConverter()
            >>> result = converter.convert('test.pdf', 'output/')
            >>> print(result['success'])
            True
        """
        try:
            # Validate input file exists
            # 验证输入文件存在
            if not os.path.exists(input_file):
                return {
                    'success': False,
                    'message': f'文件不存在: {input_file}'
                }
            
            # Validate file extension
            # 验证文件扩展名
            if not input_file.lower().endswith('.pdf'):
                return {
                    'success': False,
                    'message': f'文件格式错误，仅支持PDF格式'
                }
            
            # Determine output path
            # 确定输出路径
            if output_path is None:
                output_path = os.path.dirname(input_file)
            
            # Create output directory if not exists
            # 如果输出目录不存在则创建
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            
            # Perform conversion using office.pdf.pdf2docx
            # 使用office.pdf.pdf2docx执行转换
            office.pdf.pdf2docx(input_file, output_path)
            
            # Determine output file path
            # 确定输出文件路径
            input_filename = os.path.basename(input_file)
            output_filename = os.path.splitext(input_filename)[0] + '.docx'
            output_file = os.path.join(output_path, output_filename)
            
            # Verify output file was created
            # 验证输出文件已创建
            if os.path.exists(output_file):
                return {
                    'success': True,
                    'message': '转换成功',
                    'output_file': output_file
                }
            else:
                return {
                    'success': False,
                    'message': '转换完成但未找到输出文件'
                }
                
        except PermissionError as e:
            return {
                'success': False,
                'message': f'权限错误: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'转换失败: {str(e)}'
            }
    
    def batch_convert(self, file_list, output_path=None, progress_callback=None):
        """Convert multiple PDF files to Word documents.
        
        将多个PDF文件转换为Word文档。
        
        This method processes a list of PDF files sequentially and converts each
        to Word format. It supports progress callback for UI updates.
        
        该方法按顺序处理PDF文件列表，将每个文件转换为Word格式。支持进度回调以更新UI。
        
        Args:
            file_list (list): list of PDF file paths / PDF文件路径列表
            output_path (str, optional): output directory path / 输出目录路径。Default / 默认: None
            progress_callback (callable, optional): callback function for progress updates / 进度更新回调函数
                Signature: callback(current_index, total_count, current_file, result)
        
        Returns:
            dict: batch conversion summary / 批量转换摘要
                {
                    'total': int,
                    'success': int,
                    'failed': int,
                    'results': list of conversion results
                }
        
        Examples:
            >>> converter = PDFConverter()
            >>> files = ['file1.pdf', 'file2.pdf']
            >>> summary = converter.batch_convert(files, 'output/')
            >>> print(f"成功: {summary['success']}, 失败: {summary['failed']}")
            成功: 2, 失败: 0
        """
        total = len(file_list)
        success_count = 0
        failed_count = 0
        results = []
        
        for index, file_path in enumerate(file_list):
            # Convert single file
            # 转换单个文件
            result = self.convert(file_path, output_path)
            
            # Update counters
            # 更新计数器
            if result['success']:
                success_count += 1
            else:
                failed_count += 1
            
            results.append({
                'file': file_path,
                'result': result
            })
            
            # Call progress callback if provided
            # 如果提供了进度回调则调用
            if progress_callback:
                progress_callback(index + 1, total, file_path, result)
        
        return {
            'total': total,
            'success': success_count,
            'failed': failed_count,
            'results': results
        }
