#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
自动创建Excel并模拟数据的GUI应用

功能：通过图形界面创建Excel文件并生成模拟数据
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                               QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, 
                               QSpinBox, QComboBox, QFileDialog, QMessageBox, QGroupBox)
from PySide6.QtCore import Qt
from office.api.excel import fake2excel


class Fake2ExcelGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Excel数据模拟器 - Python-Office")
        self.setGeometry(100, 100, 600, 500)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        layout = QVBoxLayout()
        
        # 列设置组
        column_group = QGroupBox("列设置")
        column_layout = QVBoxLayout()
        
        # 列名输入
        column_label = QLabel("列名（用逗号分隔，如：name,age,email）：")
        self.column_input = QLineEdit()
        self.column_input.setPlaceholderText("例如：name,age,email,city,phone")
        
        # 支持的列类型提示
        column_tip = QLabel("支持模拟的列类型：name, age, email, phone, address, city, company, job, etc.")
        column_tip.setStyleSheet("color: gray; font-size: 10px;")
        
        column_layout.addWidget(column_label)
        column_layout.addWidget(self.column_input)
        column_layout.addWidget(column_tip)
        column_group.setLayout(column_layout)
        
        # 数据设置组
        data_group = QGroupBox("数据设置")
        data_layout = QHBoxLayout()
        
        # 行数设置
        row_label = QLabel("生成行数：")
        self.row_spinbox = QSpinBox()
        self.row_spinbox.setRange(1, 10000)
        self.row_spinbox.setValue(100)
        
        # 语言选择
        lang_label = QLabel("数据语言：")
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["中文 (zh_CN)", "英文 (english)"])
        
        data_layout.addWidget(row_label)
        data_layout.addWidget(self.row_spinbox)
        data_layout.addStretch()
        data_layout.addWidget(lang_label)
        data_layout.addWidget(self.lang_combo)
        data_group.setLayout(data_layout)
        
        # 文件设置组
        file_group = QGroupBox("文件设置")
        file_layout = QVBoxLayout()
        
        # 文件路径选择
        path_layout = QHBoxLayout()
        path_label = QLabel("保存路径：")
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("./fake2excel.xlsx")
        self.path_button = QPushButton("浏览")
        self.path_button.clicked.connect(self.browse_path)
        
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.path_button)
        
        file_layout.addLayout(path_layout)
        file_group.setLayout(file_layout)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        self.generate_btn = QPushButton("生成Excel")
        self.generate_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; padding: 10px; }")
        self.generate_btn.clicked.connect(self.generate_excel)
        
        self.clear_btn = QPushButton("清空")
        self.clear_btn.clicked.connect(self.clear_inputs)
        
        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.generate_btn)
        
        # 日志输出
        log_group = QGroupBox("操作日志")
        log_layout = QVBoxLayout()
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(150)
        log_layout.addWidget(self.log_text)
        log_group.setLayout(log_layout)
        
        # 添加到主布局
        layout.addWidget(column_group)
        layout.addWidget(data_group)
        layout.addWidget(file_group)
        layout.addWidget(QLabel(""))  # 间距
        layout.addLayout(button_layout)
        layout.addWidget(log_group)
        
        central_widget.setLayout(layout)
        
    def browse_path(self):
        """选择保存路径"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "保存Excel文件", "./fake2excel.xlsx", "Excel文件 (*.xlsx)"
        )
        if file_path:
            self.path_input.setText(file_path)
            
    def clear_inputs(self):
        """清空所有输入"""
        self.column_input.clear()
        self.row_spinbox.setValue(100)
        self.path_input.clear()
        self.log_text.clear()
        
    def generate_excel(self):
        """生成Excel文件"""
        try:
            # 获取输入参数
            columns_text = self.column_input.text().strip()
            if not columns_text:
                QMessageBox.warning(self, "输入错误", "请输入列名！")
                return
                
            columns = [col.strip() for col in columns_text.split(',') if col.strip()]
            rows = self.row_spinbox.value()
            path = self.path_input.text().strip() or './fake2excel.xlsx'
            language = 'english' if self.lang_combo.currentText() == '英文 (english)' else 'zh_CN'
            
            # 记录开始
            self.log_text.append(f"开始生成Excel文件...")
            self.log_text.append(f"列名: {', '.join(columns)}")
            self.log_text.append(f"行数: {rows}")
            self.log_text.append(f"语言: {language}")
            self.log_text.append(f"保存路径: {path}")
            
            # 调用API
            fake2excel(columns=columns, rows=rows, path=path, language=language)
            
            # 记录完成
            self.log_text.append("✓ Excel文件生成成功！")
            self.log_text.append("-" * 50)
            
            QMessageBox.information(self, "成功", f"Excel文件已生成：\n{path}")
            
        except Exception as e:
            error_msg = f"生成失败：{str(e)}"
            self.log_text.append(f"❌ {error_msg}")
            QMessageBox.critical(self, "错误", error_msg)


def main():
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle('Fusion')
    
    window = Fake2ExcelGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()