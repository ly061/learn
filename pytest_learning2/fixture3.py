import time
import unittest
import pytest
from parameterized import parameterized


class TestEsacpeProcess(unittest.TestCase):
    """
    Test Esacpe Tooter bike Social
    """

    def test_fixture3(self,driver):
        self.driver = driver
        print(self.driver)

if __name__ == '__main__':
    pytest.main("pytest_learning2/fixture3.py -n 1")

