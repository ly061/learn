# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from page.page import Page
#
#
# class test_demo1(Page):
#     def __init__(self):
#         self.driver = webdriver.Chrome()  # 第一步打开浏览器
#         super().__init__(self.driver)
#
#     def test_case1(self):
#         self.driver.maximize_window()        # 窗口最大化
#         # self.driver.get("https://sunmaker.medicare.healthinsurance.com/saved-progress/glgr8000")     # 打开网址
#         # self.wait_element_until_visible((By.LINK_TEXT, "2 Prescriptions")).click()
#         # self.wait_element_until_visible((By.LINK_TEXT, "Prescription Drugs")).click()
#         # self.wait_element_until_visible(By.CLASS_NAME, "hZQpTV").click()
#         # input_data = self.driver.find_elements(By.XPATH, "//input[@type='text']")
#         # data = ["A", "C", "A", "M"]
#         # for i,j in enumerate(input_data):
#         #     j.send_keys(data[i])
#         # self.wait_element_until_visible((By.CLASS_NAME, "d8wg8j-1")).click()
#
#         self.driver.get("https://hdguest:MLP@2017@change-your-ride.proferochina.com/en_GB/home")
#         # self.driver.find_element(By.CLASS_NAME, "selectBike__title").screenshot("image1.png")
#         js ="document.documentElement.scrollTop=10000"
#         self.script(js)
#         time.sleep(5)
#         self.driver.find_element(By.TAG_NAME, "body").screenshot("image2.png")
#
# test = test_demo1()
# test.test_case1()

import os

os.environ['env'] = 'dev'
print(os.environ)