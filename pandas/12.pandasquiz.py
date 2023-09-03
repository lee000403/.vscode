import pandas as pd
import numpy as np

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)
# print(df["영화"])
# print(df[["영화", "평점"]])
# df_sel = df["개봉 연도"] >= 2015
# print(df.loc[df_sel, ["영화", "개봉 연도"]])
# print(df)
# df["추천 점수"] = (df["관객 수"] * df["평점"]) // 100
# print(df)
df.sort_values("개봉 연도", ascending=False, inplace=True)
print(df)