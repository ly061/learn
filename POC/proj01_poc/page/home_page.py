"""
Escape Home Page
"""
import time
import datetime
import os
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
import requests
import json

import selenium.webdriver.support.expected_conditions as EC

from page.page import Page
from proj01_poc.data.marketmatrix_utils import get_social_matrix
from proj01_poc.data.urls import current_url
from proj01_poc.element.elements_define import ElementsDefine


class HomePage(Page):
    """
    Escape Home Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = ""
        super(HomePage, self).__init__(driver, current_url())
        self.element = ElementsDefine()
        self.screenshot_path = f"report/screenshot/proj21-{datetime.datetime.now():%Y%m%d}"
        if not os.path.exists(self.screenshot_path):
            os.mkdir(self.screenshot_path)

