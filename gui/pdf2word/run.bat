@echo off
REM PDF to Word Converter Launcher
REM PDF转Word转换器启动器

echo ============================================
echo   PDF to Word Converter
echo   PDF转Word转换器
echo ============================================
echo.

REM Check if Python is installed
REM 检查Python是否已安装
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo 错误：Python未安装或不在PATH中
    pause
    exit /b 1
)

echo Starting application...
echo 正在启动应用程序...
echo.

python main.py

pause
@echo off
REM PDF to Word Converter Launcher
REM PDF转Word转换器启动器

echo ============================================
echo   PDF to Word Converter
echo   PDF转Word转换器
echo ============================================
echo.

REM Check if Python is installed
REM 检查Python是否已安装
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo 错误：Python未安装或不在PATH中
    pause
    exit /b 1
)

echo Starting application...
echo 正在启动应用程序...
echo.

python main.py

pause
