import numpy as np

# arange() : 정수 범위로 배열 생성
print(np.arange(0, 30, 2)) # array 로 만들어짐. 0 ~ 30까지 0, 2, 4, 6, ..., 28까지 만들어진다.

# linspace() : 범위 내에서 균등 간격의 배열 생성
print(np.linspace(0, 1, 5)) # 0, 0.25, 0.5, 0.75, 1 생성 array 형태로

# logspace() : 범위 내에서 균등간격으로 로그 스케일로 배열 생성
print(np.logspace(0.1, 1, 20))

# 랜덤 함수
# random.random() : 랜덤한 수의 배열 생성
print(np.random.random((3,3))) # 2차원 배열 랜덤도 가능하다.

# random.randint() : 랜덤 정수 배열
print(np.random.randint(0, 10, (3, 3))) # 2차원 배열 정수 랜덤은 (사이 숫자, (배열 차원))

# random.normal() : 정규분포 랜덤 배열
print(np.random.normal(0, 1, (3,3)))

# random.rand() : 균등분포 랜덤 배열
print(np.random.rand(3, 3)) # 차원에 따른 배열 입력

# random.randn() : 표준 정규 분포 랜덤 배열
print(np.random.randn(3,3)) # 차원에 따른 배열 입력

# 표준 데이터 타입 확인해보기
print(np.zeros(20, dtype=int)) # dtype을 통해 데이터 타입을 넣는다.
print(np.ones((3,3), dtype=bool)) # 1 = True 이므로 True로 배열 생성
print(np.full((3,3), 1.0, dtype=float)) # 1.0 으로 생성된 2차원 배열 생성