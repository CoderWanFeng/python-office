#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
多个Excel的多个sheet自动合并的GUI应用

功能：将多个Excel文件的所有工作表合并到一个Excel文件的指定工作表中
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                               QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, 
                               QFileDialog, QMessageBox, QGroupBox, QListWidget)
from PySide6.QtCore import Qt
from office.api.excel import merge2sheet


class Merge2SheetGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Excel工作表合并器 - Python-Office")
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
        self.file_list.setMaximumHeight(100)
        
        file_layout.addLayout(dir_layout)
        file_layout.addWidget(file_list_label)
        file_layout.addWidget(self.file_list)
        file_group.setLayout(file_layout)
        
        # 合并设置组
        merge_group = QGroupBox("合并设置")
        merge_layout = QVBoxLayout()
        
        # 工作表名称
        sheet_layout = QHBoxLayout()
        sheet_label = QLabel("工作表名称：")
        self.sheet_input = QLineEdit()
        self.sheet_input.setPlaceholderText("Sheet1")
        self.sheet_input.setText("Sheet1")
        
        sheet_layout.addWidget(sheet_label)
        sheet_layout.addWidget(self.sheet_input)
        sheet_layout.addStretch()
        
        # 输出文件名
        output_name_layout = QHBoxLayout()
        output_name_label = QLabel("输出文件名：")
        self.output_name_input = QLineEdit()
        self.output_name_input.setPlaceholderText("merge2sheet")
        self.output_name_input.setText("merge2sheet")
        
        output_name_layout.addWidget(output_name_label)
        output_name_layout.addWidget(self.output_name_input)
        output_name_layout.addStretch()
        
        merge_layout.addLayout(sheet_layout)
        merge_layout.addLayout(output_name_layout)
        merge_group.setLayout(merge_layout)
        
        # 输出设置组
        output_group = QGroupBox("输出设置")
        output_layout = QVBoxLayout()
        
        # 输出目录
        output_dir_layout = QHBoxLayout()
        output_label = QLabel("输出目录：")
        self.output_input = QLineEdit()
        self.output_input.setPlaceholderText("./合并结果/")
        self.output_button = QPushButton("浏览")
        self.output_button.clicked.connect(self.browse_output)
        
        output_dir_layout.addWidget(output_label)
        output_dir_layout.addWidget(self.output_input)
        output_dir_layout.addWidget(self.output_button)
        
        output_layout.addLayout(output_dir_layout)
        output_group.setLayout(output_layout)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        self.merge_btn = QPushButton("合并工作表")
        self.merge_btn.setStyleSheet("QPushButton { background-color: #9C27B0; color: white; font-weight: bold; padding: 10px; }")
        self.merge_btn.clicked.connect(self.merge_sheets)
        
        self.clear_btn = QPushButton("清空")
        self.clear_btn.clicked.connect(self.clear_inputs)
        
        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.merge_btn)
        
        # 信息提示
        info_label = QLabel("提示：此功能会将多个Excel文件的所有工作表合并到一个Excel文件的指定工作表中")
        info_label.setStyleSheet("color: #666; font-size: 12px; padding: 10px; background-color: #f5f5f5; border-radius: 5px;")
        
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
        layout.addWidget(merge_group)
        layout.addWidget(output_group)
        layout.addWidget(info_label)
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
        """选择输出目录"""
        directory = QFileDialog.getExistingDirectory(self, "选择输出目录")
        if directory:
            self.output_input.setText(directory)
            
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
        self.sheet_input.clear()
        self.output_name_input.clear()
        self.file_list.clear()
        self.log_text.clear()
        
    def merge_sheets(self):
        """合并工作表"""
        try:
            # 获取输入参数
            dir_path = self.dir_input.text().strip()
            if not dir_path:
                QMessageBox.warning(self, "输入错误", "请选择Excel文件目录！")
                return
                
            if not os.path.exists(dir_path):
                QMessageBox.warning(self, "路径错误", "选择的目录不存在！")
                return
                
            output_sheet_name = self.sheet_input.text().strip() or 'Sheet1'
            output_excel_name = self.output_name_input.text().strip() or 'merge2sheet'
            output_path = self.output_input.text().strip() or './'
            
            # 检查是否有Excel文件
            excel_files = []
            for file in os.listdir(dir_path):
                if file.lower().endswith(('.xlsx', '.xls')):
                    excel_files.append(file)
                    
            if not excel_files:
                QMessageBox.warning(self, "文件错误", "目录中没有找到Excel文件！")
                return
            
            # 记录开始
            self.log_text.append(f"开始合并Excel工作表...")
            self.log_text.append(f"源目录: {dir_path}")
            self.log_text.append(f"工作表名称: {output_sheet_name}")
            self.log_text.append(f"输出文件名: {output_excel_name}")
            self.log_text.append(f"输出目录: {output_path}")
            self.log_text.append(f"发现 {len(excel_files)} 个Excel文件")
            
            # 调用API
            merge2sheet(
                dir_path=dir_path, 
                output_sheet_name=output_sheet_name, 
                output_excel_name=output_excel_name
            )
            
            # 记录完成
            self.log_text.append("✓ Excel工作表合并成功！")
            self.log_text.append("所有工作表已合并到指定文件中")
            self.log_text.append("-" * 50)
            
            QMessageBox.information(self, "成功", f"Excel工作表已合并：\n{output_path}/{output_excel_name}.xlsx")
            
        except Exception as e:
            error_msg = f"合并失败：{str(e)}"
            self.log_text.append(f"❌ {error_msg}")
            QMessageBox.critical(self, "错误", error_msg)


def main():
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle('Fusion')
    
    window = Merge2SheetGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()