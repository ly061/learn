"""
这儿的data是在conftest文件里的fixture,作用域是module，所以执行的时候能看到只调用的一次fixture
执行命令    pytest --setup-show pytest_learning2/fixture_1.py
"""


def test_data1(data):
    assert data == 42


def test_data2(data):
    assert data == 23
