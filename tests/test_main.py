import unittest

# if __name__ == '__main__':
#     test_dir = './test_unit'
#     suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#     # 创建测试runner，执行测试用例集
#     with open('test_result.txt', 'w+') as f:
#         runner = unittest.TextTestRunner(stream=f, verbosity=2)
#         runner.run(suite)
import pytest

if __name__ == '__main__':
    pytest.main(['./test_unit', '--html=report.html'])
