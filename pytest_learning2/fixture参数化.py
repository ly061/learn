"""
测试参数化
执行命令 pytest --setup-show pytest_learning2/fixture参数化.py
"""


def test_data1(data1):
    print('test data')
    assert data1['age'] == 26
