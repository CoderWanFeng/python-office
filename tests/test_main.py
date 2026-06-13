"""测试主入口模块。

该模块提供测试运行的主入口点，支持使用pytest运行测试套件并生成HTML报告。
"""

# if __name__ == '__main__':
#     test_dir = './test_code'
#     suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#     # 创建测试runner，执行测试用例集
#     with open('test_result.txt', 'w+') as f:
#         runner = unittest.TextTestRunner(stream=f, verbosity=2)
#         runner.run(suite)
import pytest


if __name__ == '__main__':
    """运行测试套件的主函数。
    
    Args:
        无参数，使用默认配置运行测试。
        
    Returns:
        None: 无返回值。
    """
    pytest.main(['./test_code', '--html=report.html'])
