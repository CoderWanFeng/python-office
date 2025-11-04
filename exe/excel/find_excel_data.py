#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
搜索Excel中指定内容的GUI应用

功能：在多个Excel文件中搜索指定的关键词
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                               QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, 
                               QFileDialog, QMessageBox, QGroupBox, QListWidget)
from PySide6.QtCore import Qt
from office.api.excel import find_excel_data


class FindExcelDataGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Excel内容搜索器 - Python-Office")
        self.setGeometry(100, 100, 700, 600)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        layout = QVBoxLayout()
        
        # 搜索设置组
        search_group = QGroupBox("搜索设置")
        search_layout = QVBoxLayout()
        
        # 搜索关键词
        keyword_layout = QHBoxLayout()
        keyword_label = QLabel("搜索关键词：")
        self.keyword_input = QLineEdit()
        self.keyword_input.setPlaceholderText("输入要搜索的内容")
        
        keyword_layout.addWidget(keyword_label)
        keyword_layout.addWidget(self.keyword_input)
        
        search_layout.addLayout(keyword_layout)
        search_group.setLayout(search_layout)
        
        # 文件选择组
        file_group = QGroupBox("文件选择")
        file_layout = QVBoxLayout()
        
        # 目录选择
        dir_layout = QHBoxLayout()
        dir_label = QLabel("搜索目录：")
        self.dir_input = QLineEdit()
        self.dir_input.setPlaceholderText("选择包含Excel文件的文件夹")
        self.dir_button = QPushButton("浏览")
        self.dir_button.clicked.connect(self.browse_directory)
        
        dir_layout.addWidget(dir_label)
        dir_layout.addWidget(self.dir_input)
        dir_layout.addWidget(self.dir_button)
        
        # 文件列表
        file_list_label = QLabel("检测到的Excel文件：")
        self.file_list = QListWidget()
        self.file_list.setMaximumHeight(100)
        
        file_layout.addLayout(dir_layout)
        file_layout.addWidget(file_list_label)
        file_layout.addWidget(self.file_list)
        file_group.setLayout(file_layout)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        self.search_btn = QPushButton("搜索内容")
        self.search_btn.setStyleSheet("QPushButton { background-color: #E91E63; color: white; font-weight: bold; padding: 10px; }")
        self.search_btn.clicked.connect(self.search_data)
        
        self.clear_btn = QPushButton("清空")
        self.clear_btn.clicked.connect(self.clear_inputs)
        
        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.search_btn)
        
        # 搜索结果组
        result_group = QGroupBox("搜索结果")
        result_layout = QVBoxLayout()
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        result_layout.addWidget(self.result_text)
        result_group.setLayout(result_layout)
        
        # 添加到主布局
        layout.addWidget(search_group)
        layout.addWidget(file_group)
        layout.addWidget(QLabel(""))  # 间距
        layout.addLayout(button_layout)
        layout.addWidget(result_group)
        
        central_widget.setLayout(layout)
        
    def browse_directory(self):
        """选择目录"""
        directory = QFileDialog.getExistingDirectory(self, "选择Excel文件目录")
        if directory:
            self.dir_input.setText(directory)
            self.scan_excel_files(directory)
            
    def scan_excel_files(self, directory):
        """扫描目录中的Excel文件"""
        self.file_list.clear()
        try:
            excel_files = []
            for file in os.listdir(directory):
                if file.lower().endswith(('.xlsx', '.xls')):
                    excel_files.append(file)
                    
            if excel_files:
                for file in sorted(excel_files):
                    self.file_list.addItem(file)
                self.result_text.append(f"在目录中发现 {len(excel_files)} 个Excel文件")
            else:
                self.result_text.append("❌ 目录中没有找到Excel文件")
                
        except Exception as e:
            self.result_text.append(f"❌ 扫描文件时出错：{str(e)}")
            
    def clear_inputs(self):
        """清空所有输入"""
        self.keyword_input.clear()
        self.dir_input.clear()
        self.file_list.clear()
        self.result_text.clear()
        
    def search_data(self):
        """搜索数据"""
        try:
            # 获取输入参数
            search_key = self.keyword_input.text().strip()
            if not search_key:
                QMessageBox.warning(self, "输入错误", "请输入搜索关键词！")
                return
                
            target_dir = self.dir_input.text().strip()
            if not target_dir:
                QMessageBox.warning(self, "输入错误", "请选择搜索目录！")
                return
                
            if not os.path.exists(target_dir):
                QMessageBox.warning(self, "路径错误", "选择的目录不存在！")
                return
            
            # 检查是否有Excel文件
            excel_files = []
            for file in os.listdir(target_dir):
                if file.lower().endswith(('.xlsx', '.xls')):
                    excel_files.append(file)
                    
            if not excel_files:
                QMessageBox.warning(self, "文件错误", "目录中没有找到Excel文件！")
                return
            
            # 记录开始
            self.result_text.append(f"开始搜索Excel内容...")
            self.result_text.append(f"搜索关键词: {search_key}")
            self.result_text.append(f"搜索目录: {target_dir}")
            self.result_text.append(f"发现 {len(excel_files)} 个Excel文件")
            self.result_text.append("-" * 50)
            
            # 调用API
            find_excel_data(search_key=search_key, target_dir=target_dir)
            
            # 记录完成
            self.result_text.append("✓ 搜索完成！")
            self.result_text.append("搜索结果已显示在控制台")
            self.result_text.append("请查看命令行窗口获取详细的搜索结果")
            self.result_text.append("-" * 50)
            
            QMessageBox.information(self, "成功", f"搜索完成！\n请查看命令行窗口获取详细的搜索结果")
            
        except Exception as e:
            error_msg = f"搜索失败：{str(e)}"
            self.result_text.append(f"❌ {error_msg}")
            QMessageBox.critical(self, "错误", error_msg)


def main():
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle('Fusion')
    
    window = FindExcelDataGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()