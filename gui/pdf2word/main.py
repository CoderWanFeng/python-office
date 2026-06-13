# -*- coding: UTF-8 -*-
"""Main entry point for PDF to Word converter application.

PDF转Word转换器应用程序的主入口点。

This is the main entry point for the PDF to Word GUI application.
It initializes the application and shows the main window.

这是PDF转Word GUI应用程序的主入口点。
它初始化应用程序并显示主窗口。
"""

import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
from models.converter import PDFConverter
from utils.file_manager import FileManager
from controllers.converter_controller import ConverterController


def main():
    """Main function to start the application.
    
    启动应用程序的主函数。
    
    This function creates the application instance, initializes all components,
    and starts the event loop.
    
    该函数创建应用程序实例，初始化所有组件，并启动事件循环。
    """
    # Create application instance
    # 创建应用程序实例
    app = QApplication(sys.argv)
    app.setApplicationName('PDF转Word工具')
    
    # Create model instances
    # 创建模型实例
    converter = PDFConverter()
    file_manager = FileManager()
    
    # Create view
    # 创建视图
    main_window = MainWindow()
    
    # Create controller
    # 创建控制器
    controller = ConverterController(main_window, converter, file_manager)
    
    # Show main window
    # 显示主窗口
    main_window.show()
    
    # Start event loop
    # 启动事件循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
# -*- coding: UTF-8 -*-
"""Main entry point for PDF to Word converter application.

PDF转Word转换器应用程序的主入口点。

This is the main entry point for the PDF to Word GUI application.
It initializes the application and shows the main window.

这是PDF转Word GUI应用程序的主入口点。
它初始化应用程序并显示主窗口。
"""

import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
from models.converter import PDFConverter
from utils.file_manager import FileManager
from controllers.converter_controller import ConverterController


def main():
    """Main function to start the application.
    
    启动应用程序的主函数。
    
    This function creates the application instance, initializes all components,
    and starts the event loop.
    
    该函数创建应用程序实例，初始化所有组件，并启动事件循环。
    """
    # Create application instance
    # 创建应用程序实例
    app = QApplication(sys.argv)
    app.setApplicationName('PDF转Word工具')
    
    # Create model instances
    # 创建模型实例
    converter = PDFConverter()
    file_manager = FileManager()
    
    # Create view
    # 创建视图
    main_window = MainWindow()
    
    # Create controller
    # 创建控制器
    controller = ConverterController(main_window, converter, file_manager)
    
    # Show main window
    # 显示主窗口
    main_window.show()
    
    # Start event loop
    # 启动事件循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
