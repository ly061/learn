"""
The Browser Object
"""
import os
from selenium import webdriver

headless = eval(os.environ["headless"]) if "headless" in os.environ else None

#iPhone X
WIDTH = 375
HEIGHT = 812
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

def chrome_browser(headless = headless):
    option = webdriver.ChromeOptions()
    option.headless = headless
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    return driver

def firefox_browser(headless = headless, mobile = False):
    option = webdriver.FirefoxOptions()
    if mobile:
        option.add_argument(f'--user-agent={UA}')
    option.headless = headless
    driver = webdriver.Firefox(options=option)
    if mobile:
        driver.set_window_size(WIDTH, HEIGHT)
    driver.maximize_window()
    return driver
