from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
url = 'https://www.google.co.kr/?hl=ko'
driver.get(url)

driver.find_element(By.CSS_SELECTOR, '.gLFyf').send_keys("네이버")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.gLFyf').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.LC20lb.MBeuO.DKV0Md').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#query').send_keys("전자신문")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#query').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#main_pack > section.sc_new.sp_nsite._project_site_channel_root._section_nsite_._sp_ntotal._prs_vsd_bas > div > div > div.nsite_desc > div.sublink_wrap > ul > li:nth-child(3)').click()
time.sleep(3)
my_list = ["it", "IT", "AI", "ai"]
'''driver.find_element(By.XPATH, '//section[@class="main_news_wrap"]//*[contains(text()="IT")]').click()
time.sleep(3)'''

count_sum = driver.find_elements(By.CSS_SELECTOR, '.main_art')
for i in range(0,len(count_sum)):
    count = driver.find_elements(By.XPATH, "/html/body/section/section/section/section/article[{}]/p/a".format(i+1))
    for j in range(len(my_list)):
        if my_list[j] in count[i]:
            count[i].click()
            time.sleep(2)