import pandas as pd
import numpy as np

df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")
print(df)

# 데이터 수정
# Column 수정
df["학교"].replace({"북산고" : "상북고", "능남고" : "무슨고"}) # 딕셔너리 형태로 변화해줘야함.
print(df)
df["SW특기"].str.lower()
df["SW특기"] = df["SW특기"].str.lower()
print(df)

df["SW특기"] = df["SW특기"].str.upper()
print(df)

df["학교"] = df["학교"] + "등학교" # 학교 데이터 + 등학교
print(df)

# Column 추가
df["총합"] = df["국어"] + df["수학"] + df["과학"] + df["사회"] + df["영어"]
print(df)
df["결과"] = "Fail" # 결과 Column 을 추가하고 전체 데이터는 Fail 로 초기화
print(df)
df.loc[df["총합"] > 400, "결과"] = "Pass" # 총합이 400보다 큰 데이터에 대해서 결과를 Pass로 업데이트
print(df)

# Column 삭제
df.drop(columns=["총합"]) # 총합 Column 을 삭젠
df.drop(columns=["국어", "영어", "수학"]) # 국어, 영어, 수학 column 을 삭제

# Row 삭제
df.drop(index="4번") # 4번 학생 데이터 row 를 삭제
filt = df["수학"] < 80 # 수학 점수 80점 미만 학생 필터링
print(df[filt])
df[filt].index
print(df.drop(index=df[filt].index))

# Row 추가
df.loc["9번"] = ["이정환", "해남고등학교", 184, 90, 90, 90, 90, 90, "Kotlin", 450, "Pass"] # 새로운 Row 추가
print(df)

# Cell 수정
df.loc["4번", "SW특기"] = "Python" # 4번 학생의 SW특기 데이터를 Python으로 변경
print(df)
df.loc["5번", ["학교", "SW특기"]] = ["능남고등학교", "C"] # 5번 학생의 학교는 능남고등학교로, SW특기는 C로 변경
print(df)

# Column 순서 변경
cols = list(df.columns)
print(cols)
df = df[[cols[-1]] + cols[0:-1]] # 맨 뒤에 있는 결과 Column 을 앞으로 가져오고, 나머지 Column 들과 합쳐서 순서 변경
print(df)

# Column 이름 변경
df.columns = ["Result"] # column 을 지정해주고 이름을 column 수의 맞게 넣어준다.
print(df)