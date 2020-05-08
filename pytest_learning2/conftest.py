import pytest
import json
from selenium import webdriver


@pytest.fixture(name='data', scope='module')
def some_data():
    return 42


get_data1 = json.loads(open(r'C:\Users\Administrator\Desktop\Learn\learn\pytest_learning2\data.json').read())


@pytest.fixture(params=get_data1, name='data1', scope='session')
def give_data(request):
    return request.param


@pytest.fixture(name='driver')
def driver():
    return 5
