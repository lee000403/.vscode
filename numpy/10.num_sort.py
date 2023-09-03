import numpy as np

# 배열 정렬
# 원본을 그대로 유지한다.
a1 = np.random.randint(1, 10, size=10)
print(a1)
print(np.sort(a1))
print(a1)
print(np.argsort(a1)) # 정렬되는 인덱스 위치 값 리턴
print(a1)

# 정렬 저장
print(a1.sort())
print(a1)

# 2차원
a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)
print(np.sort(a2, axis=0))
print(np.sort(a2, axis=1))

# 부분 정렬
# partition(): 배열에서 k개의 작은 값을 반환
a1 = np.random.randint(1, 10, size=10)
print(a1)
print(np.partition(a1, 3))

# 2차원
a2 = np.random.randint(1, 10, size=(5, 5))
print(a2)
print(np.partition(a2, 3))
print(np.partition(a2, 3, axis=0))
print(np.partition(a2, 3, axis=1))