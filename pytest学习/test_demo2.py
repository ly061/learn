import unittest
from selenium import webdriver
from time import sleep


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        self.driver.close()

    def test_1(self):
        print('test1')
        sleep(2)

    def test_2(self):
        print('test2')
        sleep(2)

    def test_3(self):
        print('test3')
        sleep(2)

    def test_4(self):
        print('test4')
        sleep(2)
        assert 1 == 4


