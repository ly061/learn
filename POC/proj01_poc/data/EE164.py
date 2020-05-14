import time
from selenium import webdriver
from proj01_poc.data.locales import v1_locales


def test_ticket_164(locale):
    driver = webdriver.Firefox()
    driver.get(f"https://hdguest:MLP@2017@change-your-ride.proferochina.com/{locale}/home-content")
    time.sleep(5)
    a = driver.find_elements_by_class_name("loadSection__title")[0].text.strip()
    b = driver.find_elements_by_class_name("loadSection__title")[1].text.strip()
    driver.find_element_by_class_name("icon-close").click()     # close cookie
    time.sleep(2)
    driver.find_element_by_class_name("common-cta_btn").click()         # click select bike button
    time.sleep(1)
    driver.find_element_by_class_name("selectBike__decide-box").click()
    time.sleep(3)
    a1 = driver.find_elements_by_class_name("commonLocation__title")[0].text.strip()
    b1 = driver.find_elements_by_class_name("commonLocation__title")[1].text.strip()
    if a != a1 or b != b1:
        print(f"{locale} didn't change the copy")
        print(a, b)
        print(a1, b1)
        with open("test164.txt", "a+") as f:
            f.write(f"{locale}\n")
    driver.close()


for locale in v1_locales:
    test_ticket_164(locale)

li = []
with open("test164.txt") as f:
    for i in f:
        li.append(i.strip())
s = ", ".join(li)
print(s)
