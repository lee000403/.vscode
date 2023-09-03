import pandas as pd

df = pd.read_csv("Score.txt", sep="\t", index_col="지원 번호")

# DataFrame 확인
print(df.describe()) # 계산 가능한 데이터 타입을 컬럼 별로 각각 계산을 해준다. 평균, 최대, 최소 등등
print(df.info()) # 데이터 개수 및 타입 확인 용량도 확인 가능
print(df.head()) # 처음 5개의 row를 가져옴

print(df.tail()) # 마지막 5개의 row를 가져옴
print(df.values) # 전체를 리스트 형태로 볼 수 있다.
print(df.index) # 인덱스의 개수 및 종류를 알 수 있다.
print(df.columns) # columns 들을 볼 수 있다.
print(df.shape) # DataFrame 의 형태를 알 수 있다. # row, column 형태로 출력

# Series 확인
print(df["키"].describe())
print(df["키"].min())
print(df["키"].max())
print(df["키"].nlargest(3)) # 키 큰 사람 순서대로 3명 데이터
print(df["키"].mean()) # 평균
print(df["키"].sum()) # 합
print(df["SW특기"].count()) # 유효한 데이터 개수 출력 nan값은 개수 취급 안함
print(df["학교"].unique()) # 유니크한 값만 출력
print(df["학교"].nunique()) # 유니크한 값 개수 출력