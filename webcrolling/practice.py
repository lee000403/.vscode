import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import clipboard
from selenium.webdriver.common.action_chains import ActionChains

a = []
b = []
browser = webdriver.Chrome()
browser.get("https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/searchHomeHF.do?menu_grp=MENU_NEW01&menu_no=2823#")
time.sleep(2)
click_ti = browser.find_element(By.XPATH, ('//*[@id="search_word"]'))
click_ti.send_keys("다이어트")
time.sleep(2)
click_ti.send_keys(Keys.ENTER)
time.sleep(2)
# browser.find_element(By.ID, "show_cnt").click()
# time.sleep(2)
# browser.find_element(By.XPATH, '//*[@id="show_cnt"]/option[3]').click()
# time.sleep(2)
# browser.find_element(By.ID, "show_cnt-btn").click()
# time.sleep(2)
for i in range(0,len(browser.find_elements(By.CLASS_NAME, "table_txt"))):
    try:
        title = browser.find_elements(By.CLASS_NAME, "table_txt")[i]
        a.append(title.get_attribute("innerText"))
        title.click()
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "url").click()
        time.sleep(1)
        alert = Alert(browser)
        alert.send_keys(Keys.CONTROL)
        alert.send_keys("c")
        time.sleep(1)
        alert.accept()
        time.sleep(1)
        result = clipboard.paste()
        b.append(result)
        browser.back()
        time.sleep(1)
    except:
        break
print(a)
print(b)
browser.quit()