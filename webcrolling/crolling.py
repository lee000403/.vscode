import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() # 크롬 실행
browser.maximize_window() # 최대화

# 페이지 이동

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url) # url 페이지로 이동

# 조회 항목 초기화 (체크 되어 있는 항목 초기화)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): 
        checkbox.click()

# 조회 항목 설정 (원하는 항목)
items_to_select = ["거래량", "시가총액", "영업이익"]
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') 
    lable = parent.find_element(By.TAG_NAME, 'label')
    #print(lable.text) # 이름 확인
    if lable.text in items_to_select:
        checkbox.click()

btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 100):
    browser.get(url + str(idx))
    
    # 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:
        break
    

    # 파일 저장
    f_name = 'sise.csv'
    if os.path.exists(f_name): # 파일이 있다면? 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else: # 파일이 없다면? 헤더 포함
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    print(f'{idx} 페이지 완료')

browser.quit()
