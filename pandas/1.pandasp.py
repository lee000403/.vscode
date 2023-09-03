import pandas as pd

# s = pd.Series([9904312, 3448737, 2890451, 2466052],
#               index=["서울", "부산", "인천", "대구"])
# # print(s)
# # print(s.index)
# # print(s.values)
# # s.index.name = "도시"
# # print(s / 1000)

# # s1 = pd.Series(range(10, 14))
# # print(s1)
# print(s)
# print(s[1], s["대구"])
# print(s[[0,3,1]])
# print(s[["서울", "대구", "부산"]])
# print(s.items)

# s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158},
#                index=["부산", "서울", "인천", "대전"])
# print(s2)

# rs = (s - s2) / s2 * 100
# rs = rs[rs.notnull()]
# print(rs)
# rs["부산"] = 1.3
# print(rs)

# a = pd.Series([1, 2, 3, 5, 7],
#               index=["A", "a", "b", "c", "d"])

# a1 = pd.Series([11, 22, 33, 55, 77],
#                index=["a", "b", "c", "d", "E"])
# sum = a - a1
# sum = sum[sum.notnull()]
# print(a)
# print(a1)
# print(sum)

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
print(data)
df = pd.DataFrame(data, columns=["이름", "학교", "키"])
print(df)