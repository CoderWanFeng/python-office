#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
按指定列拆分Excel的GUI应用

功能：根据指定列的内容将Excel文件拆分为多个文件
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                               QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, 
                               QFileDialog, QMessageBox, QGroupBox, QSpinBox)
from PySide6.QtCore import Qt
from office.api.excel import split_excel_by_column


class SplitExcelByColumnGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Excel按列拆分器 - Python-Office")
        self.setGeometry(100, 100, 600, 500)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        layout = QVBoxLayout()
        
        # 文件选择组
        file_group = QGroupBox("文件选择")
        file_layout = QVBoxLayout()
        
        # Excel文件选择
        excel_layout = QHBoxLayout()
        excel_label = QLabel("Excel文件：")
        self.excel_input = QLineEdit()
        self.excel_input.setPlaceholderText("选择要拆分的Excel文件")
        self.excel_button = QPushButton("浏览")
        self.excel_button.clicked.connect(self.browse_excel)
        
        excel_layout.addWidget(excel_label)
        excel_layout.addWidget(self.excel_input)
        excel_layout.addWidget(self.excel_button)
        
        file_layout.addLayout(excel_layout)
        file_group.setLayout(file_layout)
        
        # 拆分设置组
        split_group = QGroupBox("拆分设置")
        split_layout = QVBoxLayout()
        
        # 列号设置
        column_layout = QHBoxLayout()
        column_label = QLabel("拆分列号：")
        self.column_spinbox = QSpinBox()
        self.column_spinbox.setRange(0, 100)
        self.column_spinbox.setValue(0)
        self.column_spinbox.setToolTip("从0开始计数，0表示第一列，1表示第二列，以此类推")
        
        column_layout.addWidget(column_label)
        column_layout.addWidget(self.column_spinbox)
        column_layout.addStretch()
        
        # 工作表名称
        sheet_layout = QHBoxLayout()
        sheet_label = QLabel("工作表名称：")
        self.sheet_input = QLineEdit()
        self.sheet_input.setPlaceholderText("留空表示第一个工作表")
        
        sheet_layout.addWidget(sheet_label)
        sheet_layout.addWidget(self.sheet_input)
        sheet_layout.addStretch()
        
        split_layout.addLayout(column_layout)
        split_layout.addLayout(sheet_layout)
        split_group.setLayout(split_layout)
        
        # 输出设置组
        output_group = QGroupBox("输出设置")
        output_layout = QVBoxLayout()
        
        # 输出目录
        output_dir_layout = QHBoxLayout()
        output_label = QLabel("输出目录：")
        self.output_input = QLineEdit()
        self.output_input.setPlaceholderText("./拆分结果/")
        self.output_button = QPushButton("浏览")
        self.output_button.clicked.connect(self.browse_output)
        
        output_dir_layout.addWidget(output_label)
        output_dir_layout.addWidget(self.output_input)
        output_dir_layout.addWidget(self.output_button)
        
        output_layout.addLayout(output_dir_layout)
        output_group.setLayout(output_layout)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        self.split_btn = QPushButton("按列拆分")
        self.split_btn.setStyleSheet("QPushButton { background-color: #3F51B5; color: white; font-weight: bold; padding: 10px; }")
        self.split_btn.clicked.connect(self.split_by_column)
        
        self.clear_btn = QPushButton("清空")
        self.clear_btn.clicked.connect(self.clear_inputs)
        
        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.split_btn)
        
        # 信息提示
        info_label = QLabel("提示：此功能会根据指定列的不同内容将Excel文件拆分为多个文件")
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
        layout.addWidget(split_group)
        layout.addWidget(output_group)
        layout.addWidget(info_label)
        layout.addWidget(QLabel(""))  # 间距
        layout.addLayout(button_layout)
        layout.addWidget(log_group)
        
        central_widget.setLayout(layout)
        
    def browse_excel(self):
        """选择Excel文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择Excel文件", "", "Excel文件 (*.xlsx *.xls)"
        )
        if file_path:
            self.excel_input.setText(file_path)
            
    def browse_output(self):
        """选择输出目录"""
        directory = QFileDialog.getExistingDirectory(self, "选择输出目录")
        if directory:
            self.output_input.setText(directory)
            
    def clear_inputs(self):
        """清空所有输入"""
        self.excel_input.clear()
        self.output_input.clear()
        self.column_spinbox.setValue(0)
        self.sheet_input.clear()
        self.log_text.clear()
        
    def split_by_column(self):
        """按列拆分"""
        try:
            # 获取输入参数
            filepath = self.excel_input.text().strip()
            if not filepath:
                QMessageBox.warning(self, "输入错误", "请选择Excel文件！")
                return
                
            if not os.path.exists(filepath):
                QMessageBox.warning(self, "文件错误", "选择的Excel文件不存在！")
                return
                
            column = self.column_spinbox.value()
            worksheet_name = self.sheet_input.text().strip() or None
            
            # 记录开始
            self.log_text.append(f"开始按列拆分Excel文件...")
            self.log_text.append(f"源文件: {filepath}")
            self.log_text.append(f"拆分列号: {column}")
            if worksheet_name:
                self.log_text.append(f"工作表名称: {worksheet_name}")
            
            # 调用API
            split_excel_by_column(
                filepath=filepath, 
                column=column, 
                worksheet_name=worksheet_name
            )
            
            # 记录完成
            self.log_text.append("✓ Excel文件按列拆分成功！")
            self.log_text.append("根据列内容已拆分为多个文件")
            self.log_text.append("-" * 50)
            
            QMessageBox.information(self, "成功", f"Excel文件已按列拆分完成！")
            
        except Exception as e:
            error_msg = f"拆分失败：{str(e)}"
            self.log_text.append(f"❌ {error_msg}")
            QMessageBox.critical(self, "错误", error_msg)


def main():
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle('Fusion')
    
    window = SplitExcelByColumnGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()