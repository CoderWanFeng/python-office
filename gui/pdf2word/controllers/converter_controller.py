# -*- coding: UTF-8 -*-
"""Converter controller module for PDF to Word converter.

PDF转Word转换器的转换控制器模块。

This module manages the conversion process and coordinates between
the model and view layers.

该模块管理转换过程并协调模型层和视图层之间的交互。
"""

import os
from PyQt5.QtCore import QThread, pyqtSignal


class ConverterThread(QThread):
    """Worker thread for PDF conversion.
    
    PDF转换的工作线程。
    
    This thread runs the conversion process in the background to avoid
    blocking the main UI thread.
    
    该线程在后台运行转换过程，以避免阻塞主UI线程。
    """
    
    # Signals
    # 信号
    progress_updated = pyqtSignal(int, int, str)  # current, total, filename / 当前进度、总数、文件名
    file_converted = pyqtSignal(int, str, dict)  # file_id, filepath, result / 文件ID、文件路径、结果
    conversion_completed = pyqtSignal(dict)  # summary / 摘要
    
    def __init__(self, converter, file_manager, output_path=None):
        """Initialize the converter thread.
        
        初始化转换线程。
        
        Args:
            converter (PDFConverter): PDF converter instance / PDF转换器实例
            file_manager (FileManager): file manager instance / 文件管理器实例
            output_path (str, optional): output directory path / 输出目录路径。Default / 默认: None
        """
        super().__init__()
        self.converter = converter
        self.file_manager = file_manager
        self.output_path = output_path
        self.is_cancelled = False
    
    def run(self):
        """Run the conversion process.
        
        运行转换过程。
        """
        files = self.file_manager.get_all_files()
        total = len(files)
        success_count = 0
        failed_count = 0
        
        for index, file_info in enumerate(files):
            # Check if cancelled
            # 检查是否已取消
            if self.is_cancelled:
                break
            
            file_id = file_info['id']
            filepath = file_info['filepath']
            
            # Update status to processing
            # 更新状态为转换中
            self.file_manager.update_file_status(file_id, 'processing')
            
            # Emit progress update
            # 发出进度更新信号
            self.progress_updated.emit(index + 1, total, file_info['filename'])
            
            # Determine output path for this file
            # 确定此文件的输出路径
            output_dir = self.output_path if self.output_path else os.path.dirname(filepath)
            
            # Convert file
            # 转换文件
            result = self.converter.convert(filepath, output_dir)
            
            # Update file status based on result
            # 根据结果更新文件状态
            if result['success']:
                self.file_manager.update_file_status(file_id, 'success')
                self.file_manager.update_output_path(file_id, result.get('output_file', ''))
                success_count += 1
            else:
                self.file_manager.update_file_status(file_id, 'failed', result['message'])
                failed_count += 1
            
            # Emit file conversion complete
            # 发出文件转换完成信号
            self.file_converted.emit(file_id, filepath, result)
        
        # Emit conversion completed with summary
        # 发出转换完成信号及摘要
        summary = {
            'total': total,
            'success': success_count,
            'failed': failed_count,
            'cancelled': self.is_cancelled
        }
        self.conversion_completed.emit(summary)
    
    def cancel(self):
        """Cancel the conversion process.
        
        取消转换过程。
        """
        self.is_cancelled = True


class ConverterController:
    """Controller for managing PDF to Word conversion process.
    
    管理PDF转Word转换过程的控制器。
    
    This class coordinates between the view, model, and manages the conversion workflow.
    
    该类协调视图、模型之间的交互，并管理转换工作流程。
    """
    
    def __init__(self, view, converter, file_manager):
        """Initialize the converter controller.
        
        初始化转换控制器。
        
        Args:
            view (MainWindow): main window view / 主窗口视图
            converter (PDFConverter): PDF converter instance / PDF转换器实例
            file_manager (FileManager): file manager instance / 文件管理器实例
        """
        self.view = view
        self.converter = converter
        self.file_manager = file_manager
        self.converter_thread = None
        
        # Connect signals
        # 连接信号
        self.connect_signals()
    
    def connect_signals(self):
        """Connect view signals to controller slots.
        
        连接视图信号到控制器槽函数。
        """
        self.view.file_selected.connect(self.on_files_selected)
        self.view.convert_clicked.connect(self.on_convert_clicked)
        self.view.clear_clicked.connect(self.on_clear_clicked)
        self.view.remove_file_clicked.connect(self.on_remove_file_clicked)
    
    def on_files_selected(self, filepaths):
        """Handle file selection event.
        
        处理文件选择事件。
        
        Args:
            filepaths (list): list of selected file paths / 选择的文件路径列表
        """
        added_count = 0
        for filepath in filepaths:
            file_info = self.file_manager.add_file(filepath)
            if file_info:
                self.view.add_file_to_table(file_info)
                added_count += 1
        
        if added_count > 0:
            self.view.update_status(f'已添加 {added_count} 个文件')
        else:
            self.view.show_info_message('提示', '没有添加新文件，可能文件已存在或格式不正确')
    
    def on_convert_clicked(self):
        """Handle convert button click event.
        
        处理转换按钮点击事件。
        """
        # Check if there are files to convert
        # 检查是否有文件需要转换
        if self.file_manager.get_file_count() == 0:
            self.view.show_info_message('提示', '请先添加PDF文件')
            return
        
        # Get output path
        # 获取输出路径
        output_path = self.view.get_output_path()
        
        # Validate output path if specified
        # 如果指定了输出路径则验证
        if output_path and not os.path.exists(output_path):
            try:
                os.makedirs(output_path)
            except Exception as e:
                self.view.show_error_message('错误', f'无法创建输出目录: {str(e)}')
                return
        
        # Set UI to converting state
        # 设置UI为转换状态
        self.view.set_converting_state(True)
        self.view.update_status('开始转换...')
        self.view.update_progress(0, self.file_manager.get_file_count())
        
        # Create and start converter thread
        # 创建并启动转换线程
        self.converter_thread = ConverterThread(
            self.converter,
            self.file_manager,
            output_path
        )
        
        # Connect thread signals
        # 连接线程信号
        self.converter_thread.progress_updated.connect(self.on_progress_updated)
        self.converter_thread.file_converted.connect(self.on_file_converted)
        self.converter_thread.conversion_completed.connect(self.on_conversion_completed)
        
        # Start conversion
        # 开始转换
        self.converter_thread.start()
    
    def on_progress_updated(self, current, total, filename):
        """Handle progress update from converter thread.
        
        处理来自转换线程的进度更新。
        
        Args:
            current (int): current progress / 当前进度
            total (int): total files / 文件总数
            filename (str): current file being converted / 正在转换的当前文件
        """
        self.view.update_progress(current, total)
        self.view.update_status(f'正在转换 ({current}/{total}): {filename}')
    
    def on_file_converted(self, file_id, filepath, result):
        """Handle file conversion completion.
        
        处理文件转换完成。
        
        Args:
            file_id (int): file ID / 文件ID
            filepath (str): file path / 文件路径
            result (dict): conversion result / 转换结果
        """
        status = 'success' if result['success'] else 'failed'
        error_msg = '' if result['success'] else result['message']
        self.view.update_file_status(file_id, status, error_msg)
    
    def on_conversion_completed(self, summary):
        """Handle conversion completion.
        
        处理转换完成。
        
        Args:
            summary (dict): conversion summary / 转换摘要
        """
        # Set UI back to normal state
        # 将UI恢复为正常状态
        self.view.set_converting_state(False)
        
        # Update status
        # 更新状态
        if summary['cancelled']:
            self.view.update_status('转换已取消')
        else:
            status_text = f'转换完成! 成功: {summary["success"]}, 失败: {summary["failed"]}'
            self.view.update_status(status_text)
            
            # Show completion message
            # 显示完成消息
            message = f'转换完成!\n\n总计: {summary["total"]}\n成功: {summary["success"]}\n失败: {summary["failed"]}'
            self.view.show_info_message('转换完成', message)
    
    def on_clear_clicked(self):
        """Handle clear button click event.
        
        处理清空按钮点击事件。
        """
        self.file_manager.clear_files()
        self.view.clear_table()
        self.view.update_status('已清空文件列表')
        self.view.update_progress(0, 1)
    
    def on_remove_file_clicked(self, file_id):
        """Handle remove file event.
        
        处理删除文件事件。
        
        Args:
            file_id (int): ID of file to remove / 要删除的文件ID
        """
        if self.file_manager.remove_file(file_id):
            # Rebuild table
            # 重建表格
            self.view.clear_table()
            for file_info in self.file_manager.get_all_files():
                self.view.add_file_to_table(file_info)
            
            self.view.update_status('已删除文件')
