import numpy as np

a1 = np.array([1,2,3,4,5])
a2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
a3 = np.array([ [[1,2,3], [4,5,6], [7,8,9]],  # 3차원 배열
                [[1,2,3], [4,5,6], [7,8,9]],
                [[1,2,3], [4,5,6], [7,8,9]] ])

print(a1)
print(a1[0]) # 인덱스는 0부터 시작
print(a1[2])
print(a1[-1]) # -1 번째 인덱스는 맨뒤에서 첫번째 인덱스이다 (5)
print(a1[-2])

print(a2)
print(a2[0, 0]) # 인덱스는 0부터 시작
print(a2[0, 2])
print(a2[1, 1]) # -1 번째 인덱스는 맨뒤에서 첫번째 인덱스이다 (5)
print(a2[2, -1])

print(a3)
print(a3[0, 0, 0])
print(a3[1, 1, 1])
print(a3[2, 2, 2])
print(a3[2, -1, -1])

# 슬라이싱 a[start : stop : step] 기본값: start = 0, stop=ndim, step=1
# 1차원 슬라이싱
print(a1)
print(a1[0:2]) # 두번째 칸에 들어가는 2는 0 ~ 1까지 인덱스 출력
print(a1[0:])
print(a1[:1])
print(a1[::2]) # 세번째 칸에 들어가는 수는 간격을 나타낸다. (0번쨰, 2번째, 4번째 인덱스 출력)
print(a1[::-1]) # -1은 거꾸로 출력의미

# 2차원 슬라이싱
print(a2)
print(a2[1])
print(a2[1, :])
print(a2[:2, :2])
print(a2[1:, ::-1])
print(a2[::-1, ::-1])

# 불리언 인덱싱 (True 값인 인덱스의 값만 조회)
# 1차원
print(a1)
bi = [False, True, True, False, True]
print(a1[bi])
bi = [True, False, True, True, False]
print(a1[bi])

# 2차원 배열
print(a2)
bi = np.random.randint(0,2, (3,3), dtype=bool) # 랜덤 인트에 0 ~ 1 사이에 숫자를 랜덤 부여하고 (3,3) 모양의 배열, 타입을 bool로 바꾼다.
print(bi)
print(a2[bi])

# 팬시 인덱싱
print(a1)
print([a1[0], a1[2]]) # a1의 요소를 뽑아 배열에 다시 넣어서 출력
ind = [0, 2]
print(a1[ind]) # 결과를 한번에 출력
ind = np.array([[0, 1],
                [2, 0]])
print(a1[ind]) # 2차원 배열로 a1의 숫자가 나온다.

# 2차원 배열
print(a2)
row = np.array([0, 2]) 
col = np.array([1, 2]) 
print(a2[row, col]) # row 에서 0번째 인덱스, col 1번째 인덱스 출력 (2 출력) # row 에서 2번째 인덱스 출력, col 2번째 인덱스 출력 (9 출력)
print(a2[row, :]) # 0번째 row와 2번째 row만 출력
print(a2[:, col]) # 1번째 col과 2번째 col만 출력
print(a2[row, 1])
print(a2[2, col])
print(a2[row, 1:])
print(a2[1: , col])
