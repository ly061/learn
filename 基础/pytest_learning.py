import pytest

@pytest.fixture()
def some_data():
    print("1111111")
    yield
    print("2222222")

def test_some_data(some_data):
    print("test")