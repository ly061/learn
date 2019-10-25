import pytest


@pytest.fixture(name='ly')
def test_1():
    print('this is fixture')


def test_2(test_1):
    print('this is test 2')
