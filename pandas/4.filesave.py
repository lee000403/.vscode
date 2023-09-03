import pandas as pd

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
df.index.name = "지원 번호"
print(df)

# 저장하기

# df.to_csv("score.csv", encoding="utf-8-sig", index=False)

# df.to_csv("Score.txt", sep="\t") # 탭칸을 띄워서 저장

# 열기
df = pd.read_csv("score.csv", skiprows=1) # 지정된 개수 만큼의 row 를 건너 뜀
print(df)
df = pd.read_csv("score.csv", skiprows=[1,3,5]) # 1, 3, 5 row 건너뜀(row는 0부터 시작)
df = pd.read_csv("score.csv", nrows=4) # 지정된 개수 만큼 가져옴
df = pd.read_csv("score.csv", skiprows=2, nrows=4)
df = pd.read_csv("score.txt", sep="\t", index_col="지원 번호")
print(df)
df = pd.read_csv("score.txt", sep="\t")
df.set_index("지원 번호", inplace=True)