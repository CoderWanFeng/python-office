# -*- coding: UTF-8 -*-
"""Main window view for PDF to Word converter.

PDF转Word转换器的主窗口视图。

This module defines the main window UI components and layout.

该模块定义主窗口UI组件和布局。
"""

import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTableWidget,
                             QTableWidgetItem, QProgressBar, QFileDialog,
                             QMessageBox, QHeaderView, QAbstractItemView)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QFont


class MainWindow(QMainWindow):
    """Main window class for PDF to Word converter application.
    
    PDF转Word转换器应用程序的主窗口类。
    
    This class creates and manages the main window UI, including file selection,
    conversion controls, and progress display.
    
    该类创建和管理主窗口UI，包括文件选择、转换控制和进度显示。
    """
    
    # Signals
    # 信号
    file_selected = pyqtSignal(list)  # Emitted when files are selected / 当文件被选择时触发
    convert_clicked = pyqtSignal()  # Emitted when convert button is clicked / 当转换按钮被点击时触发
    clear_clicked = pyqtSignal()  # Emitted when clear button is clicked / 当清空按钮被点击时触发
    remove_file_clicked = pyqtSignal(int)  # Emitted when remove file is clicked / 当删除文件被点击时触发
    
    def __init__(self):
        """Initialize the main window.
        
        初始化主窗口。
        """
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface components.
        
        初始化用户界面组件。
        """
        # Set window properties
        # 设置窗口属性
        self.setWindowTitle('PDF转Word工具')
        self.setGeometry(100, 100, 900, 650)
        
        # Create central widget
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        # 创建主布局
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Add title
        # 添加标题
        title_label = QLabel('PDF转Word转换工具')
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Add toolbar
        # 添加工具栏
        toolbar_layout = self.create_toolbar()
        main_layout.addLayout(toolbar_layout)
        
        # Add file table
        # 添加文件表格
        self.file_table = self.create_file_table()
        main_layout.addWidget(self.file_table)
        
        # Add output settings
        # 添加输出设置
        output_layout = self.create_output_settings()
        main_layout.addLayout(output_layout)
        
        # Add progress bar
        # 添加进度条
        progress_layout = self.create_progress_bar()
        main_layout.addLayout(progress_layout)
        
        # Add control buttons
        # 添加控制按钮
        button_layout = self.create_control_buttons()
        main_layout.addLayout(button_layout)
        
        # Enable drag and drop
        # 启用拖放功能
        self.setAcceptDrops(True)
    
    def create_toolbar(self):
        """Create the toolbar with quick action buttons.
        
        创建包含快捷操作按钮的工具栏。
        
        Returns:
            QHBoxLayout: toolbar layout / 工具栏布局
        """
        toolbar_layout = QHBoxLayout()
        
        # Add single file button
        # 添加单文件按钮
        self.add_file_btn = QPushButton('选择PDF文件')
        self.add_file_btn.clicked.connect(self.on_add_file_clicked)
        toolbar_layout.addWidget(self.add_file_btn)
        
        # Add batch files button
        # 添加批量文件按钮
        self.add_files_btn = QPushButton('批量选择')
        self.add_files_btn.clicked.connect(self.on_add_files_clicked)
        toolbar_layout.addWidget(self.add_files_btn)
        
        # Add clear button
        # 添加清空按钮
        self.clear_btn = QPushButton('清空列表')
        self.clear_btn.clicked.connect(self.on_clear_clicked)
        toolbar_layout.addWidget(self.clear_btn)
        
        toolbar_layout.addStretch()
        
        return toolbar_layout
    
    def create_file_table(self):
        """Create the file list table.
        
        创建文件列表表格。
        
        Returns:
            QTableWidget: file table widget / 文件表格部件
        """
        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(['序号', '文件名', '文件路径', '状态'])
        
        # Set column widths
        # 设置列宽
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
        # Set table properties
        # 设置表格属性
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setAlternatingRowColors(True)
        
        # Enable context menu
        # 启用上下文菜单
        table.setContextMenuPolicy(Qt.CustomContextMenu)
        table.customContextMenuRequested.connect(self.show_context_menu)
        
        return table
    
    def create_output_settings(self):
        """Create the output settings panel.
        
        创建输出设置面板。
        
        Returns:
            QHBoxLayout: output settings layout / 输出设置布局
        """
        output_layout = QHBoxLayout()
        
        # Output path label
        # 输出路径标签
        output_label = QLabel('输出路径:')
        output_layout.addWidget(output_label)
        
        # Output path input
        # 输出路径输入框
        self.output_path_input = QLineEdit()
        self.output_path_input.setPlaceholderText('默认为源文件所在目录')
        output_layout.addWidget(self.output_path_input)
        
        # Browse button
        # 浏览按钮
        self.browse_output_btn = QPushButton('浏览...')
        self.browse_output_btn.clicked.connect(self.on_browse_output_clicked)
        output_layout.addWidget(self.browse_output_btn)
        
        return output_layout
    
    def create_progress_bar(self):
        """Create the progress bar layout.
        
        创建进度条布局。
        
        Returns:
            QVBoxLayout: progress bar layout / 进度条布局
        """
        progress_layout = QVBoxLayout()
        
        # Status label
        # 状态标签
        self.status_label = QLabel('就绪')
        progress_layout.addWidget(self.status_label)
        
        # Progress bar
        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        progress_layout.addWidget(self.progress_bar)
        
        return progress_layout
    
    def create_control_buttons(self):
        """Create the control buttons layout.
        
        创建控制按钮布局。
        
        Returns:
            QHBoxLayout: control buttons layout / 控制按钮布局
        """
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        # Convert button
        # 转换按钮
        self.convert_btn = QPushButton('开始转换')
        self.convert_btn.setMinimumWidth(120)
        self.convert_btn.setMinimumHeight(35)
        self.convert_btn.clicked.connect(self.on_convert_clicked)
        button_layout.addWidget(self.convert_btn)
        
        button_layout.addStretch()
        
        return button_layout
    
    def on_add_file_clicked(self):
        """Handle single file selection.
        
        处理单文件选择。
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            '选择PDF文件',
            '',
            'PDF文件 (*.pdf)'
        )
        
        if file_path:
            self.file_selected.emit([file_path])
    
    def on_add_files_clicked(self):
        """Handle multiple files selection.
        
        处理多文件选择。
        """
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            '批量选择PDF文件',
            '',
            'PDF文件 (*.pdf)'
        )
        
        if file_paths:
            self.file_selected.emit(file_paths)
    
    def on_browse_output_clicked(self):
        """Handle output directory selection.
        
        处理输出目录选择。
        """
        directory = QFileDialog.getExistingDirectory(
            self,
            '选择输出目录',
            ''
        )
        
        if directory:
            self.output_path_input.setText(directory)
    
    def on_convert_clicked(self):
        """Handle convert button click.
        
        处理转换按钮点击。
        """
        self.convert_clicked.emit()
    
    def on_clear_clicked(self):
        """Handle clear button click.
        
        处理清空按钮点击。
        """
        self.clear_clicked.emit()
    
    def show_context_menu(self, position):
        """Show context menu for file table.
        
        显示文件表格的上下文菜单。
        
        Args:
            position (QPoint): menu position / 菜单位置
        """
        from PyQt5.QtWidgets import QMenu
        
        menu = QMenu()
        remove_action = menu.addAction('删除')
        
        action = menu.exec_(self.file_table.mapToGlobal(position))
        
        if action == remove_action:
            current_row = self.file_table.currentRow()
            if current_row >= 0:
                file_id_item = self.file_table.item(current_row, 0)
                if file_id_item:
                    file_id = int(file_id_item.text())
                    self.remove_file_clicked.emit(file_id)
    
    def add_file_to_table(self, file_info):
        """Add a file to the table.
        
        将文件添加到表格。
        
        Args:
            file_info (dict): file information / 文件信息
        """
        row = self.file_table.rowCount()
        self.file_table.insertRow(row)
        
        # ID
        id_item = QTableWidgetItem(str(file_info['id']))
        id_item.setTextAlignment(Qt.AlignCenter)
        self.file_table.setItem(row, 0, id_item)
        
        # Filename
        # 文件名
        filename_item = QTableWidgetItem(file_info['filename'])
        self.file_table.setItem(row, 1, filename_item)
        
        # Filepath
        # 文件路径
        filepath_item = QTableWidgetItem(file_info['filepath'])
        self.file_table.setItem(row, 2, filepath_item)
        
        # Status
        # 状态
        status_item = QTableWidgetItem(self.get_status_text(file_info['status']))
        status_item.setTextAlignment(Qt.AlignCenter)
        self.set_status_color(status_item, file_info['status'])
        self.file_table.setItem(row, 3, status_item)
    
    def update_file_status(self, file_id, status, error_msg=''):
        """Update file status in the table.
        
        更新表格中的文件状态。
        
        Args:
            file_id (int): file ID / 文件ID
            status (str): new status / 新状态
            error_msg (str, optional): error message / 错误消息。Default / 默认: ''
        """
        # Find the row with the given file_id
        # 查找具有给定file_id的行
        for row in range(self.file_table.rowCount()):
            id_item = self.file_table.item(row, 0)
            if id_item and int(id_item.text()) == file_id:
                status_item = self.file_table.item(row, 3)
                if status_item:
                    status_text = self.get_status_text(status)
                    if error_msg:
                        status_text += f' ({error_msg})'
                    status_item.setText(status_text)
                    self.set_status_color(status_item, status)
                break
    
    def clear_table(self):
        """Clear all files from the table.
        
        清除表格中的所有文件。
        """
        self.file_table.setRowCount(0)
    
    def get_status_text(self, status):
        """Get status display text.
        
        获取状态显示文本。
        
        Args:
            status (str): status code / 状态代码
        
        Returns:
            str: display text / 显示文本
        """
        status_map = {
            'waiting': '等待',
            'processing': '转换中',
            'success': '成功',
            'failed': '失败'
        }
        return status_map.get(status, status)
    
    def set_status_color(self, item, status):
        """Set status item color based on status.
        
        根据状态设置状态项颜色。
        
        Args:
            item (QTableWidgetItem): table item / 表格项
            status (str): status code / 状态代码
        """
        color_map = {
            'waiting': QColor(128, 128, 128),  # Gray / 灰色
            'processing': QColor(0, 122, 204),  # Blue / 蓝色
            'success': QColor(0, 128, 0),  # Green / 绿色
            'failed': QColor(255, 0, 0)  # Red / 红色
        }
        
        color = color_map.get(status, QColor(0, 0, 0))
        item.setForeground(color)
    
    def update_progress(self, current, total):
        """Update progress bar.
        
        更新进度条。
        
        Args:
            current (int): current progress / 当前进度
            total (int): total items / 总数
        """
        if total > 0:
            percentage = int((current / total) * 100)
            self.progress_bar.setValue(percentage)
    
    def update_status(self, message):
        """Update status label.
        
        更新状态标签。
        
        Args:
            message (str): status message / 状态消息
        """
        self.status_label.setText(message)
    
    def set_converting_state(self, is_converting):
        """Set UI state for converting.
        
        设置转换时的UI状态。
        
        Args:
            is_converting (bool): whether conversion is in progress / 是否正在转换
        """
        self.add_file_btn.setEnabled(not is_converting)
        self.add_files_btn.setEnabled(not is_converting)
        self.clear_btn.setEnabled(not is_converting)
        self.convert_btn.setEnabled(not is_converting)
        self.browse_output_btn.setEnabled(not is_converting)
    
    def get_output_path(self):
        """Get the output path from input field.
        
        从输入框获取输出路径。
        
        Returns:
            str: output path or None if empty / 输出路径，如果为空则返回None
        """
        path = self.output_path_input.text().strip()
        return path if path else None
    
    def show_info_message(self, title, message):
        """Show information message box.
        
        显示信息消息框。
        
        Args:
            title (str): message box title / 消息框标题
            message (str): message content / 消息内容
        """
        QMessageBox.information(self, title, message)
    
    def show_error_message(self, title, message):
        """Show error message box.
        
        显示错误消息框。
        
        Args:
            title (str): message box title / 消息框标题
            message (str): error message / 错误消息
        """
        QMessageBox.critical(self, title, message)
    
    def dragEnterEvent(self, event):
        """Handle drag enter event.
        
        处理拖拽进入事件。
        
        Args:
            event (QDragEnterEvent): drag enter event / 拖拽进入事件
        """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        """Handle drop event.
        
        处理拖放事件。
        
        Args:
            event (QDropEvent): drop event / 拖放事件
        """
        files = []
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith('.pdf'):
                files.append(file_path)
        
        if files:
            self.file_selected.emit(files)
# -*- coding: UTF-8 -*-
"""Main window view for PDF to Word converter.

PDF转Word转换器的主窗口视图。

This module defines the main window UI components and layout.

该模块定义主窗口UI组件和布局。
"""

import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTableWidget,
                             QTableWidgetItem, QProgressBar, QFileDialog,
                             QMessageBox, QHeaderView, QAbstractItemView)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QFont


class MainWindow(QMainWindow):
    """Main window class for PDF to Word converter application.
    
    PDF转Word转换器应用程序的主窗口类。
    
    This class creates and manages the main window UI, including file selection,
    conversion controls, and progress display.
    
    该类创建和管理主窗口UI，包括文件选择、转换控制和进度显示。
    """
    
    # Signals
    # 信号
    file_selected = pyqtSignal(list)  # Emitted when files are selected / 当文件被选择时触发
    convert_clicked = pyqtSignal()  # Emitted when convert button is clicked / 当转换按钮被点击时触发
    clear_clicked = pyqtSignal()  # Emitted when clear button is clicked / 当清空按钮被点击时触发
    remove_file_clicked = pyqtSignal(int)  # Emitted when remove file is clicked / 当删除文件被点击时触发
    
    def __init__(self):
        """Initialize the main window.
        
        初始化主窗口。
        """
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface components.
        
        初始化用户界面组件。
        """
        # Set window properties
        # 设置窗口属性
        self.setWindowTitle('PDF转Word工具')
        self.setGeometry(100, 100, 900, 650)
        
        # Create central widget
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        # 创建主布局
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Add title
        # 添加标题
        title_label = QLabel('PDF转Word转换工具')
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Add toolbar
        # 添加工具栏
        toolbar_layout = self.create_toolbar()
        main_layout.addLayout(toolbar_layout)
        
        # Add file table
        # 添加文件表格
        self.file_table = self.create_file_table()
        main_layout.addWidget(self.file_table)
        
        # Add output settings
        # 添加输出设置
        output_layout = self.create_output_settings()
        main_layout.addLayout(output_layout)
        
        # Add progress bar
        # 添加进度条
        progress_layout = self.create_progress_bar()
        main_layout.addLayout(progress_layout)
        
        # Add control buttons
        # 添加控制按钮
        button_layout = self.create_control_buttons()
        main_layout.addLayout(button_layout)
        
        # Enable drag and drop
        # 启用拖放功能
        self.setAcceptDrops(True)
    
    def create_toolbar(self):
        """Create the toolbar with quick action buttons.
        
        创建包含快捷操作按钮的工具栏。
        
        Returns:
            QHBoxLayout: toolbar layout / 工具栏布局
        """
        toolbar_layout = QHBoxLayout()
        
        # Add single file button
        # 添加单文件按钮
        self.add_file_btn = QPushButton('选择PDF文件')
        self.add_file_btn.clicked.connect(self.on_add_file_clicked)
        toolbar_layout.addWidget(self.add_file_btn)
        
        # Add batch files button
        # 添加批量文件按钮
        self.add_files_btn = QPushButton('批量选择')
        self.add_files_btn.clicked.connect(self.on_add_files_clicked)
        toolbar_layout.addWidget(self.add_files_btn)
        
        # Add clear button
        # 添加清空按钮
        self.clear_btn = QPushButton('清空列表')
        self.clear_btn.clicked.connect(self.on_clear_clicked)
        toolbar_layout.addWidget(self.clear_btn)
        
        toolbar_layout.addStretch()
        
        return toolbar_layout
    
    def create_file_table(self):
        """Create the file list table.
        
        创建文件列表表格。
        
        Returns:
            QTableWidget: file table widget / 文件表格部件
        """
        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(['序号', '文件名', '文件路径', '状态'])
        
        # Set column widths
        # 设置列宽
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
        # Set table properties
        # 设置表格属性
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setAlternatingRowColors(True)
        
        # Enable context menu
        # 启用上下文菜单
        table.setContextMenuPolicy(Qt.CustomContextMenu)
        table.customContextMenuRequested.connect(self.show_context_menu)
        
        return table
    
    def create_output_settings(self):
        """Create the output settings panel.
        
        创建输出设置面板。
        
        Returns:
            QHBoxLayout: output settings layout / 输出设置布局
        """
        output_layout = QHBoxLayout()
        
        # Output path label
        # 输出路径标签
        output_label = QLabel('输出路径:')
        output_layout.addWidget(output_label)
        
        # Output path input
        # 输出路径输入框
        self.output_path_input = QLineEdit()
        self.output_path_input.setPlaceholderText('默认为源文件所在目录')
        output_layout.addWidget(self.output_path_input)
        
        # Browse button
        # 浏览按钮
        self.browse_output_btn = QPushButton('浏览...')
        self.browse_output_btn.clicked.connect(self.on_browse_output_clicked)
        output_layout.addWidget(self.browse_output_btn)
        
        return output_layout
    
    def create_progress_bar(self):
        """Create the progress bar layout.
        
        创建进度条布局。
        
        Returns:
            QVBoxLayout: progress bar layout / 进度条布局
        """
        progress_layout = QVBoxLayout()
        
        # Status label
        # 状态标签
        self.status_label = QLabel('就绪')
        progress_layout.addWidget(self.status_label)
        
        # Progress bar
        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        progress_layout.addWidget(self.progress_bar)
        
        return progress_layout
    
    def create_control_buttons(self):
        """Create the control buttons layout.
        
        创建控制按钮布局。
        
        Returns:
            QHBoxLayout: control buttons layout / 控制按钮布局
        """
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        # Convert button
        # 转换按钮
        self.convert_btn = QPushButton('开始转换')
        self.convert_btn.setMinimumWidth(120)
        self.convert_btn.setMinimumHeight(35)
        self.convert_btn.clicked.connect(self.on_convert_clicked)
        button_layout.addWidget(self.convert_btn)
        
        button_layout.addStretch()
        
        return button_layout
    
    def on_add_file_clicked(self):
        """Handle single file selection.
        
        处理单文件选择。
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            '选择PDF文件',
            '',
            'PDF文件 (*.pdf)'
        )
        
        if file_path:
            self.file_selected.emit([file_path])
    
    def on_add_files_clicked(self):
        """Handle multiple files selection.
        
        处理多文件选择。
        """
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            '批量选择PDF文件',
            '',
            'PDF文件 (*.pdf)'
        )
        
        if file_paths:
            self.file_selected.emit(file_paths)
    
    def on_browse_output_clicked(self):
        """Handle output directory selection.
        
        处理输出目录选择。
        """
        directory = QFileDialog.getExistingDirectory(
            self,
            '选择输出目录',
            ''
        )
        
        if directory:
            self.output_path_input.setText(directory)
    
    def on_convert_clicked(self):
        """Handle convert button click.
        
        处理转换按钮点击。
        """
        self.convert_clicked.emit()
    
    def on_clear_clicked(self):
        """Handle clear button click.
        
        处理清空按钮点击。
        """
        self.clear_clicked.emit()
    
    def show_context_menu(self, position):
        """Show context menu for file table.
        
        显示文件表格的上下文菜单。
        
        Args:
            position (QPoint): menu position / 菜单位置
        """
        from PyQt5.QtWidgets import QMenu
        
        menu = QMenu()
        remove_action = menu.addAction('删除')
        
        action = menu.exec_(self.file_table.mapToGlobal(position))
        
        if action == remove_action:
            current_row = self.file_table.currentRow()
            if current_row >= 0:
                file_id_item = self.file_table.item(current_row, 0)
                if file_id_item:
                    file_id = int(file_id_item.text())
                    self.remove_file_clicked.emit(file_id)
    
    def add_file_to_table(self, file_info):
        """Add a file to the table.
        
        将文件添加到表格。
        
        Args:
            file_info (dict): file information / 文件信息
        """
        row = self.file_table.rowCount()
        self.file_table.insertRow(row)
        
        # ID
        id_item = QTableWidgetItem(str(file_info['id']))
        id_item.setTextAlignment(Qt.AlignCenter)
        self.file_table.setItem(row, 0, id_item)
        
        # Filename
        # 文件名
        filename_item = QTableWidgetItem(file_info['filename'])
        self.file_table.setItem(row, 1, filename_item)
        
        # Filepath
        # 文件路径
        filepath_item = QTableWidgetItem(file_info['filepath'])
        self.file_table.setItem(row, 2, filepath_item)
        
        # Status
        # 状态
        status_item = QTableWidgetItem(self.get_status_text(file_info['status']))
        status_item.setTextAlignment(Qt.AlignCenter)
        self.set_status_color(status_item, file_info['status'])
        self.file_table.setItem(row, 3, status_item)
    
    def update_file_status(self, file_id, status, error_msg=''):
        """Update file status in the table.
        
        更新表格中的文件状态。
        
        Args:
            file_id (int): file ID / 文件ID
            status (str): new status / 新状态
            error_msg (str, optional): error message / 错误消息。Default / 默认: ''
        """
        # Find the row with the given file_id
        # 查找具有给定file_id的行
        for row in range(self.file_table.rowCount()):
            id_item = self.file_table.item(row, 0)
            if id_item and int(id_item.text()) == file_id:
                status_item = self.file_table.item(row, 3)
                if status_item:
                    status_text = self.get_status_text(status)
                    if error_msg:
                        status_text += f' ({error_msg})'
                    status_item.setText(status_text)
                    self.set_status_color(status_item, status)
                break
    
    def clear_table(self):
        """Clear all files from the table.
        
        清除表格中的所有文件。
        """
        self.file_table.setRowCount(0)
    
    def get_status_text(self, status):
        """Get status display text.
        
        获取状态显示文本。
        
        Args:
            status (str): status code / 状态代码
        
        Returns:
            str: display text / 显示文本
        """
        status_map = {
            'waiting': '等待',
            'processing': '转换中',
            'success': '成功',
            'failed': '失败'
        }
        return status_map.get(status, status)
    
    def set_status_color(self, item, status):
        """Set status item color based on status.
        
        根据状态设置状态项颜色。
        
        Args:
            item (QTableWidgetItem): table item / 表格项
            status (str): status code / 状态代码
        """
        color_map = {
            'waiting': QColor(128, 128, 128),  # Gray / 灰色
            'processing': QColor(0, 122, 204),  # Blue / 蓝色
            'success': QColor(0, 128, 0),  # Green / 绿色
            'failed': QColor(255, 0, 0)  # Red / 红色
        }
        
        color = color_map.get(status, QColor(0, 0, 0))
        item.setForeground(color)
    
    def update_progress(self, current, total):
        """Update progress bar.
        
        更新进度条。
        
        Args:
            current (int): current progress / 当前进度
            total (int): total items / 总数
        """
        if total > 0:
            percentage = int((current / total) * 100)
            self.progress_bar.setValue(percentage)
    
    def update_status(self, message):
        """Update status label.
        
        更新状态标签。
        
        Args:
            message (str): status message / 状态消息
        """
        self.status_label.setText(message)
    
    def set_converting_state(self, is_converting):
        """Set UI state for converting.
        
        设置转换时的UI状态。
        
        Args:
            is_converting (bool): whether conversion is in progress / 是否正在转换
        """
        self.add_file_btn.setEnabled(not is_converting)
        self.add_files_btn.setEnabled(not is_converting)
        self.clear_btn.setEnabled(not is_converting)
        self.convert_btn.setEnabled(not is_converting)
        self.browse_output_btn.setEnabled(not is_converting)
    
    def get_output_path(self):
        """Get the output path from input field.
        
        从输入框获取输出路径。
        
        Returns:
            str: output path or None if empty / 输出路径，如果为空则返回None
        """
        path = self.output_path_input.text().strip()
        return path if path else None
    
    def show_info_message(self, title, message):
        """Show information message box.
        
        显示信息消息框。
        
        Args:
            title (str): message box title / 消息框标题
            message (str): message content / 消息内容
        """
        QMessageBox.information(self, title, message)
    
    def show_error_message(self, title, message):
        """Show error message box.
        
        显示错误消息框。
        
        Args:
            title (str): message box title / 消息框标题
            message (str): error message / 错误消息
        """
        QMessageBox.critical(self, title, message)
    
    def dragEnterEvent(self, event):
        """Handle drag enter event.
        
        处理拖拽进入事件。
        
        Args:
            event (QDragEnterEvent): drag enter event / 拖拽进入事件
        """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        """Handle drop event.
        
        处理拖放事件。
        
        Args:
            event (QDropEvent): drop event / 拖放事件
        """
        files = []
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith('.pdf'):
                files.append(file_path)
        
        if files:
            self.file_selected.emit(files)
