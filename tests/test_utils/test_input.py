import unittest
import io
import sys


def stub_stdin(testcase_inst, inputs):
    '''
    输入内容
    :param testcase_inst:
    :param inputs:
    :return:
    '''
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = io.StringIO(inputs)


def stub_stdout(testcase_inst):
    '''
    输出内容
    :param testcase_inst:
    :return:
    '''
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()

# 用法举例
# def test_fun():
#     x = int(input())
#     print(x + 5)
#
#
# class UnitTest():
#     def test_fun(self):
#         print('请输入数字')
#         stub_stdin(self, '2\n4\n')  # 依次输入2,4
#
#         stub_stdout(self)
#         test_fun()
#         self.assertEqual(str(sys.stdout.getvalue()), '7\n')
#
#         stub_stdout(self)  # 重置输出
#         test_fun()
#         self.assertEqual(str(sys.stdout.getvalue()), '9\n')
#
#
# if __name__ == '__main__':
#     unittest.main()
