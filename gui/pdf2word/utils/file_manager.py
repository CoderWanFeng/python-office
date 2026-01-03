# -*- coding: UTF-8 -*-
"""File manager module for handling PDF files.

用于处理PDF文件的文件管理器模块。

This module provides file management functionality including validation,
listing, and metadata extraction.

该模块提供文件管理功能，包括验证、列表和元数据提取。
"""

import os
from typing import List, Dict


class FileManager:
    """File manager class for PDF files.
    
    PDF文件的文件管理器类。
    
    This class handles file operations such as validation, adding files to the list,
    removing files, and managing file metadata.
    
    该类处理文件操作，如验证、添加文件到列表、删除文件和管理文件元数据。
    """
    
    def __init__(self):
        """Initialize the file manager.
        
        初始化文件管理器。
        """
        self.file_list = []
        self.next_id = 1
    
    def add_file(self, filepath):
        """Add a PDF file to the managed list.
        
        将PDF文件添加到管理列表。
        
        Args:
            filepath (str): path to the PDF file / PDF文件路径
        
        Returns:
            dict: file information object or None if invalid / 文件信息对象，如果无效则返回None
                {
                    'id': int,
                    'filename': str,
                    'filepath': str,
                    'status': str,
                    'output_path': str,
                    'error_msg': str
                }
        
        Examples:
            >>> manager = FileManager()
            >>> file_info = manager.add_file('test.pdf')
            >>> print(file_info['filename'])
            test.pdf
        """
        # Validate file
        # 验证文件
        if not self.validate_file(filepath):
            return None
        
        # Check if file already exists in list
        # 检查文件是否已在列表中
        if self.is_file_in_list(filepath):
            return None
        
        # Create file info object
        # 创建文件信息对象
        file_info = {
            'id': self.next_id,
            'filename': os.path.basename(filepath),
            'filepath': filepath,
            'status': 'waiting',
            'output_path': '',
            'error_msg': ''
        }
        
        self.file_list.append(file_info)
        self.next_id += 1
        
        return file_info
    
    def add_files(self, filepaths):
        """Add multiple PDF files to the managed list.
        
        将多个PDF文件添加到管理列表。
        
        Args:
            filepaths (list): list of PDF file paths / PDF文件路径列表
        
        Returns:
            list: list of successfully added file information objects / 成功添加的文件信息对象列表
        
        Examples:
            >>> manager = FileManager()
            >>> files = manager.add_files(['file1.pdf', 'file2.pdf'])
            >>> print(len(files))
            2
        """
        added_files = []
        for filepath in filepaths:
            file_info = self.add_file(filepath)
            if file_info:
                added_files.append(file_info)
        return added_files
    
    def remove_file(self, file_id):
        """Remove a file from the managed list by ID.
        
        根据ID从管理列表中删除文件。
        
        Args:
            file_id (int): ID of the file to remove / 要删除的文件ID
        
        Returns:
            bool: True if file was removed, False otherwise / 如果文件被删除则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> success = manager.remove_file(1)
            >>> print(success)
            True
        """
        for i, file_info in enumerate(self.file_list):
            if file_info['id'] == file_id:
                self.file_list.pop(i)
                return True
        return False
    
    def clear_files(self):
        """Clear all files from the managed list.
        
        清除管理列表中的所有文件。
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> manager.clear_files()
            >>> print(len(manager.get_all_files()))
            0
        """
        self.file_list.clear()
        self.next_id = 1
    
    def get_file_by_id(self, file_id):
        """Get file information by ID.
        
        根据ID获取文件信息。
        
        Args:
            file_id (int): ID of the file / 文件ID
        
        Returns:
            dict: file information object or None if not found / 文件信息对象，如果未找到则返回None
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> file_info = manager.get_file_by_id(1)
            >>> print(file_info['filename'])
            test.pdf
        """
        for file_info in self.file_list:
            if file_info['id'] == file_id:
                return file_info
        return None
    
    def get_all_files(self):
        """Get all files in the managed list.
        
        获取管理列表中的所有文件。
        
        Returns:
            list: list of all file information objects / 所有文件信息对象的列表
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> files = manager.get_all_files()
            >>> print(len(files))
            1
        """
        return self.file_list
    
    def update_file_status(self, file_id, status, error_msg=''):
        """Update the status of a file.
        
        更新文件的状态。
        
        Args:
            file_id (int): ID of the file / 文件ID
            status (str): new status (waiting/processing/success/failed) / 新状态
            error_msg (str, optional): error message if status is failed / 如果状态为失败则提供错误消息。Default / 默认: ''
        
        Returns:
            bool: True if status was updated, False otherwise / 如果状态已更新则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> success = manager.update_file_status(1, 'processing')
            >>> print(success)
            True
        """
        file_info = self.get_file_by_id(file_id)
        if file_info:
            file_info['status'] = status
            file_info['error_msg'] = error_msg
            return True
        return False
    
    def update_output_path(self, file_id, output_path):
        """Update the output path of a file.
        
        更新文件的输出路径。
        
        Args:
            file_id (int): ID of the file / 文件ID
            output_path (str): output file path / 输出文件路径
        
        Returns:
            bool: True if output path was updated, False otherwise / 如果输出路径已更新则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> success = manager.update_output_path(1, 'output/test.docx')
            >>> print(success)
            True
        """
        file_info = self.get_file_by_id(file_id)
        if file_info:
            file_info['output_path'] = output_path
            return True
        return False
    
    def validate_file(self, filepath):
        """Validate if a file is a valid PDF file.
        
        验证文件是否为有效的PDF文件。
        
        Args:
            filepath (str): path to the file / 文件路径
        
        Returns:
            bool: True if file is valid, False otherwise / 如果文件有效则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> is_valid = manager.validate_file('test.pdf')
            >>> print(is_valid)
            True
        """
        # Check if file exists
        # 检查文件是否存在
        if not os.path.exists(filepath):
            return False
        
        # Check if it's a file (not a directory)
        # 检查是否为文件（不是目录）
        if not os.path.isfile(filepath):
            return False
        
        # Check file extension
        # 检查文件扩展名
        if not filepath.lower().endswith('.pdf'):
            return False
        
        return True
    
    def is_file_in_list(self, filepath):
        """Check if a file is already in the managed list.
        
        检查文件是否已在管理列表中。
        
        Args:
            filepath (str): path to the file / 文件路径
        
        Returns:
            bool: True if file is in list, False otherwise / 如果文件在列表中则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> exists = manager.is_file_in_list('test.pdf')
            >>> print(exists)
            True
        """
        for file_info in self.file_list:
            if file_info['filepath'] == filepath:
                return True
        return False
    
    def get_file_count(self):
        """Get the total number of files in the list.
        
        获取列表中文件的总数。
        
        Returns:
            int: number of files / 文件数量
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> count = manager.get_file_count()
            >>> print(count)
            1
        """
        return len(self.file_list)
    
    def get_status_count(self):
        """Get the count of files by status.
        
        按状态获取文件数量。
        
        Returns:
            dict: dictionary with status as key and count as value / 以状态为键、计数为值的字典
                {
                    'waiting': int,
                    'processing': int,
                    'success': int,
                    'failed': int
                }
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> counts = manager.get_status_count()
            >>> print(counts['waiting'])
            1
        """
        counts = {
            'waiting': 0,
            'processing': 0,
            'success': 0,
            'failed': 0
        }
        
        for file_info in self.file_list:
            status = file_info['status']
            if status in counts:
                counts[status] += 1
        
        return counts
# -*- coding: UTF-8 -*-
"""File manager module for handling PDF files.

用于处理PDF文件的文件管理器模块。

This module provides file management functionality including validation,
listing, and metadata extraction.

该模块提供文件管理功能，包括验证、列表和元数据提取。
"""

import os
from typing import List, Dict


class FileManager:
    """File manager class for PDF files.
    
    PDF文件的文件管理器类。
    
    This class handles file operations such as validation, adding files to the list,
    removing files, and managing file metadata.
    
    该类处理文件操作，如验证、添加文件到列表、删除文件和管理文件元数据。
    """
    
    def __init__(self):
        """Initialize the file manager.
        
        初始化文件管理器。
        """
        self.file_list = []
        self.next_id = 1
    
    def add_file(self, filepath):
        """Add a PDF file to the managed list.
        
        将PDF文件添加到管理列表。
        
        Args:
            filepath (str): path to the PDF file / PDF文件路径
        
        Returns:
            dict: file information object or None if invalid / 文件信息对象，如果无效则返回None
                {
                    'id': int,
                    'filename': str,
                    'filepath': str,
                    'status': str,
                    'output_path': str,
                    'error_msg': str
                }
        
        Examples:
            >>> manager = FileManager()
            >>> file_info = manager.add_file('test.pdf')
            >>> print(file_info['filename'])
            test.pdf
        """
        # Validate file
        # 验证文件
        if not self.validate_file(filepath):
            return None
        
        # Check if file already exists in list
        # 检查文件是否已在列表中
        if self.is_file_in_list(filepath):
            return None
        
        # Create file info object
        # 创建文件信息对象
        file_info = {
            'id': self.next_id,
            'filename': os.path.basename(filepath),
            'filepath': filepath,
            'status': 'waiting',
            'output_path': '',
            'error_msg': ''
        }
        
        self.file_list.append(file_info)
        self.next_id += 1
        
        return file_info
    
    def add_files(self, filepaths):
        """Add multiple PDF files to the managed list.
        
        将多个PDF文件添加到管理列表。
        
        Args:
            filepaths (list): list of PDF file paths / PDF文件路径列表
        
        Returns:
            list: list of successfully added file information objects / 成功添加的文件信息对象列表
        
        Examples:
            >>> manager = FileManager()
            >>> files = manager.add_files(['file1.pdf', 'file2.pdf'])
            >>> print(len(files))
            2
        """
        added_files = []
        for filepath in filepaths:
            file_info = self.add_file(filepath)
            if file_info:
                added_files.append(file_info)
        return added_files
    
    def remove_file(self, file_id):
        """Remove a file from the managed list by ID.
        
        根据ID从管理列表中删除文件。
        
        Args:
            file_id (int): ID of the file to remove / 要删除的文件ID
        
        Returns:
            bool: True if file was removed, False otherwise / 如果文件被删除则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> success = manager.remove_file(1)
            >>> print(success)
            True
        """
        for i, file_info in enumerate(self.file_list):
            if file_info['id'] == file_id:
                self.file_list.pop(i)
                return True
        return False
    
    def clear_files(self):
        """Clear all files from the managed list.
        
        清除管理列表中的所有文件。
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> manager.clear_files()
            >>> print(len(manager.get_all_files()))
            0
        """
        self.file_list.clear()
        self.next_id = 1
    
    def get_file_by_id(self, file_id):
        """Get file information by ID.
        
        根据ID获取文件信息。
        
        Args:
            file_id (int): ID of the file / 文件ID
        
        Returns:
            dict: file information object or None if not found / 文件信息对象，如果未找到则返回None
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> file_info = manager.get_file_by_id(1)
            >>> print(file_info['filename'])
            test.pdf
        """
        for file_info in self.file_list:
            if file_info['id'] == file_id:
                return file_info
        return None
    
    def get_all_files(self):
        """Get all files in the managed list.
        
        获取管理列表中的所有文件。
        
        Returns:
            list: list of all file information objects / 所有文件信息对象的列表
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> files = manager.get_all_files()
            >>> print(len(files))
            1
        """
        return self.file_list
    
    def update_file_status(self, file_id, status, error_msg=''):
        """Update the status of a file.
        
        更新文件的状态。
        
        Args:
            file_id (int): ID of the file / 文件ID
            status (str): new status (waiting/processing/success/failed) / 新状态
            error_msg (str, optional): error message if status is failed / 如果状态为失败则提供错误消息。Default / 默认: ''
        
        Returns:
            bool: True if status was updated, False otherwise / 如果状态已更新则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> success = manager.update_file_status(1, 'processing')
            >>> print(success)
            True
        """
        file_info = self.get_file_by_id(file_id)
        if file_info:
            file_info['status'] = status
            file_info['error_msg'] = error_msg
            return True
        return False
    
    def update_output_path(self, file_id, output_path):
        """Update the output path of a file.
        
        更新文件的输出路径。
        
        Args:
            file_id (int): ID of the file / 文件ID
            output_path (str): output file path / 输出文件路径
        
        Returns:
            bool: True if output path was updated, False otherwise / 如果输出路径已更新则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> success = manager.update_output_path(1, 'output/test.docx')
            >>> print(success)
            True
        """
        file_info = self.get_file_by_id(file_id)
        if file_info:
            file_info['output_path'] = output_path
            return True
        return False
    
    def validate_file(self, filepath):
        """Validate if a file is a valid PDF file.
        
        验证文件是否为有效的PDF文件。
        
        Args:
            filepath (str): path to the file / 文件路径
        
        Returns:
            bool: True if file is valid, False otherwise / 如果文件有效则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> is_valid = manager.validate_file('test.pdf')
            >>> print(is_valid)
            True
        """
        # Check if file exists
        # 检查文件是否存在
        if not os.path.exists(filepath):
            return False
        
        # Check if it's a file (not a directory)
        # 检查是否为文件（不是目录）
        if not os.path.isfile(filepath):
            return False
        
        # Check file extension
        # 检查文件扩展名
        if not filepath.lower().endswith('.pdf'):
            return False
        
        return True
    
    def is_file_in_list(self, filepath):
        """Check if a file is already in the managed list.
        
        检查文件是否已在管理列表中。
        
        Args:
            filepath (str): path to the file / 文件路径
        
        Returns:
            bool: True if file is in list, False otherwise / 如果文件在列表中则返回True，否则返回False
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> exists = manager.is_file_in_list('test.pdf')
            >>> print(exists)
            True
        """
        for file_info in self.file_list:
            if file_info['filepath'] == filepath:
                return True
        return False
    
    def get_file_count(self):
        """Get the total number of files in the list.
        
        获取列表中文件的总数。
        
        Returns:
            int: number of files / 文件数量
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> count = manager.get_file_count()
            >>> print(count)
            1
        """
        return len(self.file_list)
    
    def get_status_count(self):
        """Get the count of files by status.
        
        按状态获取文件数量。
        
        Returns:
            dict: dictionary with status as key and count as value / 以状态为键、计数为值的字典
                {
                    'waiting': int,
                    'processing': int,
                    'success': int,
                    'failed': int
                }
        
        Examples:
            >>> manager = FileManager()
            >>> manager.add_file('test.pdf')
            >>> counts = manager.get_status_count()
            >>> print(counts['waiting'])
            1
        """
        counts = {
            'waiting': 0,
            'processing': 0,
            'success': 0,
            'failed': 0
        }
        
        for file_info in self.file_list:
            status = file_info['status']
            if status in counts:
                counts[status] += 1
        
        return counts
