import numpy as np

a1 = np.array([1,2,3,4,5])
a2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
a3 = np.array([ [[1,2,3], [4,5,6], [7,8,9]],  # 3차원 배열
                [[1,2,3], [4,5,6], [7,8,9]],
                [[1,2,3], [4,5,6], [7,8,9]] ])

# insert
print(a1)
b1 = np.insert(a1, 0, 10) # 배열, 위치, 값, axis 순서로 넣어야 한다. 위치에 추가로 넣는 것이다. 기존 인덱스는 사라지지 않는다.
print(b1)
print(a1) # b1의 insert를 했기 때문에 a1의 값은 바뀌지 않는다.
c1 = np.insert(a1, 2, 10)
print(c1)

print(a2)
b2 = np.insert(a2, 1, 10, axis=0) # axis = 0 은 row이기 때문에 (2,) 에 10으로 다 채워진다.
print(b2)
c2 = np.insert(a2, 1, 10, axis=1) # axis = 1 은 colunm이기 때문에 (1,1), (2,1), (3,1) 부분에 10으로 다 채운다.
print(c2)

# 배열 값 수정
print(a1)
a1[0] = 2
a1[1] = 3
a1[2] = 4
print(a1)
a1[:1] = 9 # n번째 인덱스까지 9로 수정
print(a1)
i = np.array([1, 3, 4])
a1[i] = 0 # 1, 3, 4번째 인덱스를 0으로 값을 수정
print(a1)
a1[i] += 4
print(a1) # a1[i] 부분을 +4 인 상태로 값 수정

print(a2)
a2[0, 0] = 2
a2[1, 1] = 3
a2[2, 2] = 4
a2[0] = 1 # 전체 해당하는 row가 1로 바뀐다.
print(a2)
a2[1:, 2] = 9
print(a2)
row = np.array([0, 1])
col = np.array([1, 2])
a2[row, col] = 0
print(a2)

# 배열 값 삭제
# 특정 위치에 값 삭제, axis 지정 안할 시 1차원 배열로 변환, 삭제할 방향은 axis로 지정, 원본 배열 변경없이 새로운 배열 반환
print(a1)
b1 = np.delete(a1, 1)
print(b1)
print(a1) # a1의 배열 값은 바뀌지 않았다.

# 2차 배열
print(a2)
b2 = np.delete(a2, 1, axis=0)
print(b2)
c2 = np.delete(a2, 1, axis=1)

# 배열 복사
# 리스트 자료형과 달리 배열의 슬라이스는 복사본이 아님
print(a2)
print(a2[:2, :2])
a2_sub = a2[:2, :2]
print(a2_sub)
a2_sub[:, 1] = 0
print(a2_sub) # 원본 배열에 영향을 주는 변수이다.
print(a2)

# copy
print(a2)
a2_sub_copy = a2[:2, :2].copy() # copy() 라는 함수를 사용하면 원본 배열에 영향을 주지 않는다.
print(a2_sub_copy)
a2_sub_copy[:, 1] = 1
print(a2_sub_copy)
print(a2)
