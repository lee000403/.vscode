import pandas as pd

df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")

# print(df.columns)
# print(df.columns[0])
# print(df.columns[2])
# print(df[df.columns[0]])
# print(df["영어"][0:5])
# print(df[["이름", "키"]][:3])

# print(df.loc["1번"])
# print(df.iloc[1])
# print(df.loc[(df["키"] >= 185) & (df["학교"] == "북산고")])
# print(df.loc[df["키"] >185, ["이름", "수학", "과학"]])
# print(df.loc[(df["키"] < 170) | (df["키"] > 200)]) # 키가 170 미만이거나 200 초과인 데이터를 가져옴

# str 함수
filt = df["이름"].str.startswith("송") # "송" 씨 성을 가진 사람 데이터 가져옴
print(df[filt])
filt = df["이름"].str.contains("태") # "태" 가 들어가는 사람 데이터
print(df[filt])
print(df[~filt]) # "태" 가 들어가는 사람을 제외

langs = ["Python", "Java"]
filt = df["SW특기"].isin(langs) # SW특기가 Pyhon 이거나 Java 인 사람
print(df[filt])
langs = ["python", "java"]
filt = df["SW특기"].str.lower().isin(langs)
print(df[filt])
filt = df["SW특기"].str.contains("Java", na=False) # NaN 데이텅 대해서 False 로 설정 na 속성 잘 알고 있기
print(df[filt])