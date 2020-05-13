
import unittest

from BeautifulReport import BeautifulReport

# 用例存放位置

test_case_path = "C:\Users\coco.chen\PycharmProjects\untitled"

# 测试报告存放位置

log_path = 'C:\Users\coco.chen\PycharmProjects\untitled'

# 测试报告名称

filename = 'Report'

# 用例名称

description = '2.py'

# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"

pattern = "2.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)

    result = BeautifulReport(test_suite)

    result.report(filename=filename, description=description, log_path=log_path)
