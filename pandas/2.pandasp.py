import pandas as pd
import numpy as np

# data = {
#     "2015": [9904312, 3448737, 2890451, 2466052],
#     "2010": [9631482, 3393191, 2632035, 2431774],
#     "2005": [9762546, 3512547, 2517680, 2456016],
#     "2000": [9853972, 3655437, 2466338, 2473990],
#     "지역": ["수도권", "경상권", "수도권", "경상권"],
#     "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
# }
# columns = ["지역", "2000", "2005", "2010", "2015", "2010-2015 증가율"]
# index = ["서울", "부산", "인천", "대구"]
# df = pd.DataFrame(data, index=index, columns=columns)
# print(df)
# print(df.values)
# df.index.name = "도시"
# df.columns.name = "특성"
# print(df)

data_1 = {
    "name" : ["lee", "kim", "jang", "kang", "oh"],
    "age" : [12, 14, 51, 24, 21],
    "height" : [123.1, 162.2, 190.8, 152.5, 124.4],
    "1" : [1, 2, 3, 4, 5],
    "3" : [1000, 1001, 1002, 1003, 1004]
}
col = ["name", "height", "1", "age", "3"]
idx = ["학생 1", "학생 2", "학생 3", "학생 4", "학생 5"]
df = pd.DataFrame(data_1, index=idx, columns=col)
# print(df)
# print(df.T)
# df["height"] = df["height"] * 100
# print(df)
# df["weight"] = (df["height"] / 3).round(2)
# print(df)
# del df["weight"]
# print(df)
print(df[["name", "age"]])
print(df["age"])
print(df[["age"]])
print(df["age"]["학생 2"])

df2 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df2)

data = {
    "국어": [80, 90, 70, 30],
    "영어": [90, 70, 60, 40],
    "수학": [90, 60, 80, 70],
}
columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]
df = pd.DataFrame(data, index=index, columns=columns)
print(df)
print(df["수학"])
print(df[["국어","영어"]])
df["평균"] = (df["국어"] + df["영어"] + df["수학"]) / 3
print(df)
df["영어"]["방자"] = 80
df["평균"] = (df["국어"] + df["영어"] + df["수학"]) / 3
print(df)
print(df[:1])
print(df.T["향단"])