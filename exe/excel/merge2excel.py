#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
多个Excel合并到一个文件的不同sheet中的GUI应用

功能：将多个Excel文件合并到一个Excel文件的不同工作表中
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                               QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, 
                               QFileDialog, QMessageBox, QGroupBox, QListWidget)
from PySide6.QtCore import Qt
from office.api.excel import merge2excel


class Merge2ExcelGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Excel文件合并器 - Python-Office")
        self.setGeometry(100, 100, 700, 600)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        layout = QVBoxLayout()
        
        # 文件选择组
        file_group = QGroupBox("文件选择")
        file_layout = QVBoxLayout()
        
        # 目录选择
        dir_layout = QHBoxLayout()
        dir_label = QLabel("Excel文件目录：")
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
        self.file_list.setMaximumHeight(150)
        
        file_layout.addLayout(dir_layout)
        file_layout.addWidget(file_list_label)
        file_layout.addWidget(self.file_list)
        file_group.setLayout(file_layout)
        
        # 输出设置组
        output_group = QGroupBox("输出设置")
        output_layout = QVBoxLayout()
        
        # 输出文件路径
        output_path_layout = QHBoxLayout()
        output_label = QLabel("合并后文件：")
        self.output_input = QLineEdit()
        self.output_input.setPlaceholderText("./merge2excel.xlsx")
        self.output_button = QPushButton("浏览")
        self.output_button.clicked.connect(self.browse_output)
        
        output_path_layout.addWidget(output_label)
        output_path_layout.addWidget(self.output_input)
        output_path_layout.addWidget(self.output_button)
        
        output_layout.addLayout(output_path_layout)
        output_group.setLayout(output_layout)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        self.merge_btn = QPushButton("合并Excel文件")
        self.merge_btn.setStyleSheet("QPushButton { background-color: #2196F3; color: white; font-weight: bold; padding: 10px; }")
        self.merge_btn.clicked.connect(self.merge_excel)
        
        self.clear_btn = QPushButton("清空")
        self.clear_btn.clicked.connect(self.clear_inputs)
        
        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.merge_btn)
        
        # 日志输出
        log_group = QGroupBox("操作日志")
        log_layout = QVBoxLayout()
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(150)
        log_layout.addWidget(self.log_text)
        log_group.setLayout(log_layout)
        
        # 添加到主布局
        layout.addWidget(file_group)
        layout.addWidget(output_group)
        layout.addWidget(QLabel(""))  # 间距
        layout.addLayout(button_layout)
        layout.addWidget(log_group)
        
        central_widget.setLayout(layout)
        
    def browse_directory(self):
        """选择目录"""
        directory = QFileDialog.getExistingDirectory(self, "选择Excel文件目录")
        if directory:
            self.dir_input.setText(directory)
            self.scan_excel_files(directory)
            
    def browse_output(self):
        """选择输出文件"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "保存合并后的Excel文件", "./merge2excel.xlsx", "Excel文件 (*.xlsx)"
        )
        if file_path:
            self.output_input.setText(file_path)
            
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
                self.log_text.append(f"在目录中发现 {len(excel_files)} 个Excel文件")
            else:
                self.log_text.append("❌ 目录中没有找到Excel文件")
                
        except Exception as e:
            self.log_text.append(f"❌ 扫描文件时出错：{str(e)}")
            
    def clear_inputs(self):
        """清空所有输入"""
        self.dir_input.clear()
        self.output_input.clear()
        self.file_list.clear()
        self.log_text.clear()
        
    def merge_excel(self):
        """合并Excel文件"""
        try:
            # 获取输入参数
            dir_path = self.dir_input.text().strip()
            if not dir_path:
                QMessageBox.warning(self, "输入错误", "请选择Excel文件目录！")
                return
                
            if not os.path.exists(dir_path):
                QMessageBox.warning(self, "路径错误", "选择的目录不存在！")
                return
                
            output_file = self.output_input.text().strip() or './merge2excel.xlsx'
            
            # 检查是否有Excel文件
            excel_files = []
            for file in os.listdir(dir_path):
                if file.lower().endswith(('.xlsx', '.xls')):
                    excel_files.append(file)
                    
            if not excel_files:
                QMessageBox.warning(self, "文件错误", "目录中没有找到Excel文件！")
                return
            
            # 记录开始
            self.log_text.append(f"开始合并Excel文件...")
            self.log_text.append(f"源目录: {dir_path}")
            self.log_text.append(f"输出文件: {output_file}")
            self.log_text.append(f"发现 {len(excel_files)} 个Excel文件")
            
            # 调用API
            merge2excel(dir_path=dir_path, output_file=output_file)
            
            # 记录完成
            self.log_text.append("✓ Excel文件合并成功！")
            self.log_text.append("每个Excel文件已合并为单独的工作表")
            self.log_text.append("-" * 50)
            
            QMessageBox.information(self, "成功", f"Excel文件已合并：\n{output_file}")
            
        except Exception as e:
            error_msg = f"合并失败：{str(e)}"
            self.log_text.append(f"❌ {error_msg}")
            QMessageBox.critical(self, "错误", error_msg)


def main():
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle('Fusion')
    
    window = Merge2ExcelGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()