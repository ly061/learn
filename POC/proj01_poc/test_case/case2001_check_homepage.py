import time
import unittest
import pytest
from parameterized import parameterized
import allure
from driver.browser import firefox_browser
from proj01_poc.page.home_page import HomePage


class Test_POC(unittest.TestCase):
    """
    Test POC homepage
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = firefox_browser()
        cls.homepage = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @allure.severity("critical")
    @allure.feature("check home page")
    @allure.story('visit home page')
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_poc_homepage(self):
        """
        this is the testcase 001 description
        """
        # self.homepage.url = "home"
        self.homepage.open_url()
        self.homepage.logger.info("open url successfully")
        time.sleep(5)

    @allure.severity("normal")
    @allure.feature("check home page")
    @allure.story('check home button is clickable')
    @pytest.mark.run(order=2)
    def test_navigation_is_clickable(self):
        """
        this is the testcase 002 description
        """
        self.res = 0
        try:
            self.homepage.element_is_clickable(self.homepage.element.hompage_navigation)
            self.homepage.logger.info("home button is clickable")
        except:
            self.res += 1
            self.homepage.logger.warning("this button is not clickable")
        assert self.res == 0
if __name__ == '__main__':
    pytest.main(["-s", "POC/proj01_poc/test_case/case2001_check_homepage.py", "-n 1"])
