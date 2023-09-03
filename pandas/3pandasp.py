import pandas as pd
import numpy as np

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data, index=["1번", "2번", "3번", "4번", "5번", "6번", "7번", "8번"])
print(df.index)
df.index.name = '지원 번호'
print(df)
print(df.reset_index())
df.reset_index(drop=True)
print(df)
df.reset_index(drop=True, inplace=True)
print(df)

print(df.set_index("이름", inplace=True))

df.sort_index(inplace=True)
print(df)
df.sort_index(ascending=False, inplace=True)
print(df)
