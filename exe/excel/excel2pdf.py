#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Excel转PDF的GUI应用

功能：将Excel文件转换为PDF格式
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                               QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, 
                               QFileDialog, QMessageBox, QGroupBox, QSpinBox)
from PySide6.QtCore import Qt
from office.api.excel import excel2pdf


class Excel2PDFGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Excel转PDF转换器 - Python-Office")
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
        self.excel_input.setPlaceholderText("选择要转换的Excel文件")
        self.excel_button = QPushButton("浏览")
        self.excel_button.clicked.connect(self.browse_excel)
        
        excel_layout.addWidget(excel_label)
        excel_layout.addWidget(self.excel_input)
        excel_layout.addWidget(self.excel_button)
        
        file_layout.addLayout(excel_layout)
        file_group.setLayout(file_layout)
        
        # 转换设置组
        convert_group = QGroupBox("转换设置")
        convert_layout = QVBoxLayout()
        
        # 工作表设置
        sheet_layout = QHBoxLayout()
        sheet_label = QLabel("工作表索引：")
        self.sheet_spinbox = QSpinBox()
        self.sheet_spinbox.setRange(0, 100)
        self.sheet_spinbox.setValue(0)
        self.sheet_spinbox.setToolTip("从0开始计数，0表示第一个工作表")
        
        sheet_layout.addWidget(sheet_label)
        sheet_layout.addWidget(self.sheet_spinbox)
        sheet_layout.addStretch()
        
        convert_layout.addLayout(sheet_layout)
        convert_group.setLayout(convert_layout)
        
        # 输出设置组
        output_group = QGroupBox("输出设置")
        output_layout = QVBoxLayout()
        
        # PDF文件路径
        pdf_layout = QHBoxLayout()
        pdf_label = QLabel("PDF文件：")
        self.pdf_input = QLineEdit()
        self.pdf_input.setPlaceholderText("选择PDF保存路径")
        self.pdf_button = QPushButton("浏览")
        self.pdf_button.clicked.connect(self.browse_pdf)
        
        pdf_layout.addWidget(pdf_label)
        pdf_layout.addWidget(self.pdf_input)
        pdf_layout.addWidget(self.pdf_button)
        
        output_layout.addLayout(pdf_layout)
        output_group.setLayout(output_layout)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        self.convert_btn = QPushButton("转换为PDF")
        self.convert_btn.setStyleSheet("QPushButton { background-color: #F44336; color: white; font-weight: bold; padding: 10px; }")
        self.convert_btn.clicked.connect(self.convert_to_pdf)
        
        self.clear_btn = QPushButton("清空")
        self.clear_btn.clicked.connect(self.clear_inputs)
        
        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.convert_btn)
        
        # 信息提示
        info_label = QLabel("提示：此功能会将指定的Excel工作表转换为PDF格式")
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
        layout.addWidget(convert_group)
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
            # 自动设置PDF文件名
            pdf_path = file_path.replace('.xlsx', '.pdf').replace('.xls', '.pdf')
            self.pdf_input.setText(pdf_path)
            
    def browse_pdf(self):
        """选择PDF文件"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "保存PDF文件", "", "PDF文件 (*.pdf)"
        )
        if file_path:
            self.pdf_input.setText(file_path)
            
    def clear_inputs(self):
        """清空所有输入"""
        self.excel_input.clear()
        self.pdf_input.clear()
        self.sheet_spinbox.setValue(0)
        self.log_text.clear()
        
    def convert_to_pdf(self):
        """转换为PDF"""
        try:
            # 获取输入参数
            excel_path = self.excel_input.text().strip()
            if not excel_path:
                QMessageBox.warning(self, "输入错误", "请选择Excel文件！")
                return
                
            if not os.path.exists(excel_path):
                QMessageBox.warning(self, "文件错误", "选择的Excel文件不存在！")
                return
                
            pdf_path = self.pdf_input.text().strip()
            if not pdf_path:
                QMessageBox.warning(self, "输入错误", "请选择PDF保存路径！")
                return
                
            sheet_id = self.sheet_spinbox.value()
            
            # 记录开始
            self.log_text.append(f"开始转换Excel为PDF...")
            self.log_text.append(f"Excel文件: {excel_path}")
            self.log_text.append(f"PDF文件: {pdf_path}")
            self.log_text.append(f"工作表索引: {sheet_id}")
            
            # 调用API
            excel2pdf(excel_path=excel_path, pdf_path=pdf_path, sheet_id=sheet_id)
            
            # 记录完成
            self.log_text.append("✓ Excel转PDF成功！")
            self.log_text.append("-" * 50)
            
            QMessageBox.information(self, "成功", f"Excel文件已转换为PDF：\n{pdf_path}")
            
        except Exception as e:
            error_msg = f"转换失败：{str(e)}"
            self.log_text.append(f"❌ {error_msg}")
            QMessageBox.critical(self, "错误", error_msg)


def main():
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle('Fusion')
    
    window = Excel2PDFGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()