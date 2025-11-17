"""PDF to Word Converter - GUI Application using PySide6"""
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QPushButton, QLabel, QFileDialog, QTextEdit, QProgressBar)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QIcon, QCursor
import popdf
import os
import sys


class ConvertThread(QThread):
    """Background thread for PDF conversion"""
    finished = Signal(str)
    error = Signal(str)
    
    def __init__(self, pdf_path, output_path):
        super().__init__()
        self.pdf_path = pdf_path
        self.output_path = output_path
    
    def run(self):
        try:
            popdf.pdf2docx(self.pdf_path, self.output_path)
            self.finished.emit(self.output_path)
        except Exception as e:
            self.error.emit(str(e))


class PDFConverterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pdf_path = None
        self.convert_thread = None  # Type: ConvertThread | None
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("程序员晚枫的软件 - PDF转Word工具")
        self.setGeometry(100, 100, 700, 550)
        
        # Set modern dark theme stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a2e, stop:1 #16213e);
            }
            QWidget {
                background: transparent;
                color: #ffffff;
                font-family: 'Microsoft YaHei', Arial;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0f4c75, stop:1 #1b6ca8);
                color: white;
                border: 2px solid #3282b8;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1b6ca8, stop:1 #3282b8);
                border: 2px solid #00d9ff;
            }
            QPushButton:pressed {
                background: #0f4c75;
            }
            QPushButton:disabled {
                background: #2c3e50;
                border: 2px solid #34495e;
                color: #7f8c8d;
            }
            QLabel {
                color: #ffffff;
            }
            QTextEdit {
                background-color: rgba(30, 30, 46, 0.8);
                border: 2px solid #3282b8;
                border-radius: 8px;
                color: #00ff88;
                padding: 10px;
                font-family: 'Consolas', monospace;
                font-size: 12px;
            }
            QProgressBar {
                border: 2px solid #3282b8;
                border-radius: 8px;
                background-color: rgba(30, 30, 46, 0.6);
                text-align: center;
                height: 25px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00d9ff, stop:1 #0f4c75);
                border-radius: 6px;
            }
        """)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title with glow effect
        title = QLabel("⚡ PDF 转 Word 转换器 ⚡")
        title.setFont(QFont("Microsoft YaHei", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            color: #00d9ff;
            padding: 20px;
            font-weight: bold;
            text-shadow: 0 0 10px #00d9ff;
        """)
        layout.addWidget(title)
        
        # File info card
        self.file_label = QLabel("📄 未选择文件")
        self.file_label.setFont(QFont("Microsoft YaHei", 12))
        self.file_label.setStyleSheet("""
            padding: 20px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 rgba(50, 130, 184, 0.3), stop:1 rgba(0, 217, 255, 0.3));
            border: 2px solid #3282b8;
            border-radius: 12px;
            color: #ffffff;
        """)
        self.file_label.setWordWrap(True)
        self.file_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.file_label)
        
        # Buttons container
        btn_layout = QVBoxLayout()
        btn_layout.setSpacing(15)
        
        # Select PDF button
        self.select_btn = QPushButton("📂 选择 PDF 文件")
        self.select_btn.setMinimumHeight(50)
        self.select_btn.setFont(QFont("Microsoft YaHei", 13, QFont.Weight.Bold))
        self.select_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.select_btn.clicked.connect(self.select_pdf)
        btn_layout.addWidget(self.select_btn)
        
        # Convert button
        self.convert_btn = QPushButton("🚀 开始转换")
        self.convert_btn.setMinimumHeight(50)
        self.convert_btn.setFont(QFont("Microsoft YaHei", 13, QFont.Weight.Bold))
        self.convert_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.convert_btn.setEnabled(False)
        self.convert_btn.clicked.connect(self.convert_pdf)
        btn_layout.addWidget(self.convert_btn)
        
        layout.addLayout(btn_layout)
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        self.progress.setTextVisible(True)
        self.progress.setFormat("转换中... %p%")
        layout.addWidget(self.progress)
        
        # Log text area
        log_label = QLabel("📋 操作日志")
        log_label.setFont(QFont("Microsoft YaHei", 11, QFont.Weight.Bold))
        log_label.setStyleSheet("color: #00d9ff; padding: 5px;")
        layout.addWidget(log_label)
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMinimumHeight(120)
        layout.addWidget(self.log_text)
        
        # Footer
        footer = QLabel("Powered by 程序员晚枫 | Python Office")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setStyleSheet("""
            color: #7f8c8d;
            font-size: 10px;
            padding: 10px;
        """)
        layout.addWidget(footer)
        
        self.log("✨ 欢迎使用 PDF 转 Word 转换工具！")
    
    def log(self, message):
        """Add message to log"""
        self.log_text.append(f"• {message}")
    
    def select_pdf(self):
        """Select PDF file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择 PDF 文件", "", "PDF Files (*.pdf)"
        )
        
        if file_path:
            self.pdf_path = file_path
            self.file_label.setText(f"已选择: {os.path.basename(file_path)}")
            self.convert_btn.setEnabled(True)
            self.log(f"已选择文件: {file_path}")
    
    def convert_pdf(self):
        """Convert PDF to Word"""
        if not self.pdf_path:
            return
        
        # Generate output path
        output_path = self.pdf_path.rsplit('.', 1)[0] + '.docx'
        
        # Disable buttons
        self.select_btn.setEnabled(False)
        self.convert_btn.setEnabled(False)
        self.progress.setVisible(True)
        self.progress.setRange(0, 0)  # Indeterminate progress
        
        self.log(f"开始转换: {os.path.basename(self.pdf_path)}")
        
        # Start conversion in background thread
        self.convert_thread = ConvertThread(self.pdf_path, output_path)
        self.convert_thread.finished.connect(self.on_convert_success)
        self.convert_thread.error.connect(self.on_convert_error)
        self.convert_thread.start()
    
    def on_convert_success(self, output_path):
        """Handle successful conversion"""
        self.progress.setVisible(False)
        self.select_btn.setEnabled(True)
        self.convert_btn.setEnabled(True)
        
        self.log(f"✓ 转换成功！")
        self.log(f"输出文件: {output_path}")
        
        # Open output folder
        folder_path = os.path.dirname(output_path)
        os.startfile(folder_path)
    
    def on_convert_error(self, error_msg):
        """Handle conversion error"""
        self.progress.setVisible(False)
        self.select_btn.setEnabled(True)
        self.convert_btn.setEnabled(True)
        
        self.log(f"✗ 转换失败: {error_msg}")


def main():
    app = QApplication(sys.argv)
    window = PDFConverterGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
