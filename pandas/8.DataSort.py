import pandas as pd
import numpy as np

df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")
print(df)

df.sort_values("키", inplace=True) # 키 기준으로 오름차순 정렬
print(df)
df.sort_values("키", ascending=False, inplace=True)
print(df)
df.sort_values(["수학", "영어"], ascending=False) # 수학, 영어 점수 기준으로 내림 차순 수학 점수가 같으면 영어 점수 기준
df.sort_values(["수학", "영어"]) # 수학, 영어 점수 기준으로 오름 차순

df.sort_values(["수학", "영어"], ascending=[True, False]) # 수학 점수는 오름 차순, 영어 점수는 내림차순으로 정렬하고 싶을땐 ascending에 리스트 형태로 넣어서 순서대로 값을 넣어준다.
print(df["키"].sort_values()) # 시리즈 형태로 출력
print(df["키"].sort_values(ascending=False))
df.sort_index() # 인덱스 번호 오름 차순 정렬