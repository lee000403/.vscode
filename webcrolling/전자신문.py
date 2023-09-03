import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pymysql

driver = webdriver.Chrome()

next_url = 'https://www.etnews.com/news/section.html?id1=04&page='
page = driver.find_elements(By.XPATH, '//a[@href="/news/section.html?id1=04&amp;page="]')
name = []
my_list = ["ai", "AI", "it", "IT"]


for next_page in range(1, 5):
    driver.get(next_url + str(next_page))
    time.sleep(2)
    list_search = driver.find_elements(By.XPATH, '/html/body/section/section/section/section/article')
    for i in list_search:
        index = i.find_elements(By.TAG_NAME, 'a')
        for last_index in index:
            for my_list_for in my_list:
                if my_list_for in last_index.get_attribute('innerText'):
                    name.append([last_index.get_attribute('innerText'), last_index.get_attribute('href')])

data = []
for i, line in enumerate(name, start=1):
    tmp=[]
    tmp.append(str(i))
    tmp += line
    data.append(tmp)

conn = pymysql.connect(host="localhost", user="root", password="1234",  charset="utf8", db="electricnewsdb")

curs = conn.cursor()
sql = """insert into news(id, title, url)
        values (%s, %s, %s)"""
curs.executemany(sql, data)
conn.commit()

conn.close()