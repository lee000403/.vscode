import pandas as pd
import numpy as np

df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")
print(df)
# df.groupby("학교") # 동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균 등의 값을 계산해서 사용
# df.groupby("학교").get_group("북산고") # 북산고 데이터 
# df.groupby("학교").get_group("능남고") # 능남고 데이터 
# df.groupby("학교").mean() # 계산 가능한 데이터들의 평균값
# df.groupby("학교").size() # 각 그룹의 크기 정보
# df.groupby("학교").size()["능남고"] # 학교로 그룹화를 한 뒤에 능남고에 해당하는 데이터 수

# df.groupby("학교")["키"].mean() # 학교로 그룹화를 한 뒤에 키의 평균 데이터
# df.groupby("학교")[["국어", "영어", "수학"]].mean() # 학교로 그룹화를 한 뒤에 국어, 영어, 수학 평균 값 데이터

df["학년"] = [3,3,2,1,1,3,2,2] # 학년 Column 추가
print(df)
df.groupby(["힉교", "학년"]).mean() # 학교별, 학년별 평균 데이터
df.groupby("학년").mean() # 학년 별 평균 데이터
df.groupby("학년").mean().sort_values("키", ascending=False)
df.groupby("학교")["SW특기"].count() # 학교로 그룹화를 한 뒤에 각 학교별 SW특기 데이터의 수를 가져옴

school = df.groupby("학교")
school["학년"].value_counts() # 학교로 그룹화를 한 뒤에 학년별 학생 수를 가져옴

school["학년"].value_counts.loc["북산고"] # 학교로 그룹화를 한 뒤에 북산고에 대해서 학년별 학생 수를 가져옴
school["학년"].value_counts.loc["능남고"] # 학교로 그룹화를 한 뒤에 능남고에 대해서 학년별 학생 수를 가져옴
school["학년"].value_counts(normalize=True).loc["북산고"] # 학생들의 수 데이터를 퍼센트로 비교하여 가져옴