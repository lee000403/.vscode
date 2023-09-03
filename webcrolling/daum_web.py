import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://finance.daum.net/domestic/market_cap')

while browser.find_elements(By.CLASS_NAME, 'btnNext'):
    for i in range(0, len(browser.find_elements(By.CLASS_NAME, 'btnMove'))):
        df = pd.read_html(browser.page_source)[1]
        df.dropna(axis='index', how='all', inplace=True)
        df.dropna(axis='columns', how='all', inplace=True)

        f_name = '다음_주식.csv'
        if os.path.exists(f_name):
            df.to_csv(f_name, encoding='utf-8', index=False, mode='a', header=False)
        else:
            df.to_csv(f_name, encoding='utf-8', index=False)
        
        button_next = browser.find_elements(By.CLASS_NAME, 'btnMove')[i]
        button_next.click()
        time.sleep(3)
    browser.find_element(By.CLASS_NAME, 'btnNext').click()
    time.sleep(3)

browser.quit()
    