import pandas as pd
import numpy as np

df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")
print(df)

# 데이터에 함수 적용 (apply)
# 키 뒤에 cm를 붙이는 역할
def add_cm(height):
    return str(height) + "cm"

df["키"] = df["키"].apply(add_cm) # 키 데이터에 대해서 add_cm 함수를 호출한 결과 데이터를 반영
print(df)

def capitalize(lang):
    if pd.notnull(lang): # NaN 이 아닌지
        return lang.capitalize() # 첫 글자는 대문자로, 나머지는 소문자로
    return lang
df["SW특기"] = df["SW특기"].apply(capitalize)
print(df)

df["SW특기"].str.capitalize()