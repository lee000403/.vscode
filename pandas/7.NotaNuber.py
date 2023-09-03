import pandas as pd
import numpy as np

df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")
print(df)

# 데이터 채우기 fillna
df.fillna("") # NaN 데이터를 빈 칸으로 채움
print(df.fillna(""))
print(df.fillna("없음"))

df["학교"] = np.nan # 학교 데이터 전체를 NaN 으로 채움
print(df)
df.fillna("모름", inplace=True)
print(df)

df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")
print(df)
df["SW특기"].fillna("확인 중", inplace=True)
print(df)

# 데이터 제외하기 dropna
df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")
print(df)
df.dropna(inplace=True) # 전체 데이터 중에서 NaN 을 포함하는 데이터 삭제
print(df)
df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")
print(df)
# axis : index or columns
# how : any or all
df.dropna(axis="index", how="any") # NaN 가 하나라도 있는 row 삭제
df.dropna(axis="columns", how="any") # NaN 이 하나라도 있는 colunm 삭제
df["학교"] = np.nan
print(df)
df.dropna(axis='columns', how='all') # 데이터 전체가 NaN 인 경우에만 column 삭제