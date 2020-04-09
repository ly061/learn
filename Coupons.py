# coding=utf-8
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class Coupons_add(unittest.TestCase):
    driver = webdriver.Chrome()
    def test_addCoupons(self, driver=driver):
        driver.get('http://mxdev.storeteam.cn/')
        time.sleep(1)
        driver.maximize_window()
        #登录
        driver.find_element_by_css_selector("#MerchantNo").send_keys("yx")
        driver.find_element_by_css_selector("#UserName").send_keys("admin")
        driver.find_element_by_css_selector("#Password").send_keys("123456")
        driver.find_element_by_css_selector("#btn_login").click()
        time.sleep(5)
        #商品中心--商品管理

        driver.find_element_by_xpath("//a[@href='#/market/coupon/cash'][span[.='营销中心']]").click()
        driver.find_element_by_xpath("//i[@class='anticon anticon-youhuiquan']").click()
        time.sleep(1)
        # #新建门票-----------------------------------------------------------------------------------------------------------------------------------------------
        driver.find_element_by_xpath("//a[@href='#/market/coupon/cash'][span[.='现金/折扣券']]").click()
        # js = 'document.getElementsByClassName("ant-btn ant-btn-primary")[1].click();'
        # driver.execute_script(js)
        # driver.find_element_by_class_name("ant-btn ant-btn-primary").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()

        driver.find_element_by_id("CouponName").send_keys("现金券8.8元")
        time.sleep(1)

        #页面下拉（通过定位元素）到挂牌价
        # MoveElement = driver.find_element_by_id("Amount")
        # ActionChains(driver).move_to_element(MoveElement).perform()
        # MoveElement.clear()
        # time.sleep(3)
        # MoveElement.send_keys('8.8') #用悬停的方法才可以设置挂牌价，否则是0.01元
        driver.find_element_by_id("Amount").clear()
        driver.find_element_by_id("Amount").send_keys('8.8')

        driver.find_element_by_xpath("//span[.='相对时间']").click()
        driver.find_element_by_id("Number").clear()
        driver.find_element_by_id("Number").send_keys('10')
        # driver.find_element_by_xpath("//span[@class='ant-calendar-range-picker-separator']").click()
        # driver.find_element_by_css_selector(".ant-calendar-today > div:nth-child(1)").click()
        # driver.find_element_by_css_selector(".ant-calendar-selected-end-date > div:nth-child(1)").click()
        # js = 'document.getElementsByClassName("ant-calendar-range-picker-separator").removeAttribute("readonly");'
        # driver.execute_script(js)
        # # a=driver.find_element_by_xpath("//span[@class='ant-calendar-range-picker-separator']")
        # # driver.execute_script('arguments[0].removeAttribute(\"readonly\")', a)
        # driver.find_element_by_xpath("//span[@class='ant-calendar-range-picker-separator']").clear()
        # driver.find_element_by_xpath("//span[@class='ant-calendar-range-picker-separator']").send_keys("2020-3-20 ~2021-3-22 23:59")



        # dd = driver.find_element_by_xpath("//td[@class='ant-calendar-cell ant-calendar-today ant-calendar-selected-date']")
        # ActionChains(driver).double_click(dd).perform()
        #
        # driver.find_element_by_xpath("//a[@class='ant-calendar-ok-btn']']").click()
        # driver.find_element_by_xpath("//button[@class='ant-btn btn_form___34Q9c ant-btn-primary']").click()

        driver.find_element_by_css_selector(".ant-calendar-range-picker-input").click()  # 点击日历
        # time.sleep(5)
        input_box1 = driver.find_element_by_css_selector(".ant-calendar-range-part.ant-calendar-range-right > div:nth-child(2) > div.ant-calendar-body > table > tbody > tr:nth-child(3) > td:nth-child(3) > div")
        input_box2 = driver.find_element_by_css_selector(".ant-calendar-range-part.ant-calendar-range-right > div:nth-child(2) > div.ant-calendar-body > table > tbody > tr:nth-child(3) > td:nth-child(5) > div")
        input_box1.click()
        input_box2.click()
        driver.find_element_by_css_selector(".ant-calendar-ok-btn").click()
