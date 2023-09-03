import numpy as np
a1 = np.array([1,2,3,4,5])
a2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
a3 = np.array([ [[1,2,3], [4,5,6], [7,8,9]],  # 3차원 배열
                [[1,2,3], [4,5,6], [7,8,9]],
                [[1,2,3], [4,5,6], [7,8,9]] ])

# 배열 전치 및 축 변경
print(a2)
print(a2.T) # 대문자 T는 축이 변경이 된다.

# 3차원 배열
print(a3)
print(a3.T) # 3차원 배열도 전치 및 축 변경이 가능하다.

print(a2)
print(a2.swapaxes(1, 0)) # swapaxes는 transpose와 비슷한 개념

print(a3)   
print(a3.swapaxes(0,1))
print(a3.swapaxes(1,2))

# 배열 재구조화
n1 = np.arange(1, 10)
print(n1)
print(n1.reshape(3,3))

# 새로운 축 추가
print(n1)
print(n1[np.newaxis, :5])
print(n1[:5, np.newaxis])

# 배열 크기 변경
n2 = np.random.randint(0, 10, (2, 5))
print(n2)
n2.resize((5, 2)) # resize는 배열 모양만 변경 (5,2) 배열로 변경
print(n2)

# 배열 크기 증가, 남은 공간은 0으로 채워짐
n2.resize((5,5))
print(n2)

# 배열 크기 감소, 포함되지 않은 값은 삭제됨
n2.resize((3,3))
print(n2) # 9개 인덱스만 출력 나머지 5는 삭제

# 배열 추가, append() : 배열의 끝에 값 추가
a2 = np.arange(1, 10).reshape(3,3)
print(a2)
b2 = np.arange(10, 19).reshape(3,3)
print(b2)
# axis 지정이 없으면 1차원 배열 형태로 변형되어 결합
c2 = np.append(a2, b2, axis=1)
print(c2)

# 배열 연결, concatenate() : 튜플이나 배열의 리스트를 인수로 사용해 배열 연결
a1 = np.array([1, 3, 5])
b1 = np.array([2, 4, 6])
np.concatenate([a1, b1])
c1 = np.array([7, 8, 9])
np.concatenate([a1, b1, c1]) # 1차원 형태(x 축 기준) 연결

# 2차원
a2 = np.array([[1, 2, 3],
               [4, 5, 6]])
print(np.concatenate([a2, a2])) # y 축 기준으로 연결

# concatenate 에서 exis 설정
a2 = np.array([[1, 2, 3],
               [4, 5, 6]])
print(np.concatenate([a2, a2], axis=1)) # axis=1(x 축) 기준으로 붙음

# vstack(): 수직 스택(vertical stack), 1차원으로 연결 (y 축)
print(np.vstack([a2, a2]))

# hstack() : 수평 스택(horizontal stack), 2차원으로 연결 (x 축)
print(np.hstack([a2, a2]))

# dstack() : 깊이 스택(depth stack), 3차원으로 연결 (z 축)
print(np.dstack([a2, a2]))

# stack() : 새로운 차원으로 연결 (1차원 -> 2차원, 2차원 -> 3차원 등등등)
print(np.stack([a2, a2]))

# 배열 분할, split(): 배열 분할
a1 = np.arange(0,10)
print(a1)
b1, c1 = np.split(a1, [5])
print(b1, c1)
b1, c1, d1, e1, f1 = np.split(a1, [2, 4, 6, 8])
print(b1, c1, d1, e1, f1)

# vsplit() : 수직 분할, 1차원으로 분할
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2, c2 = np.vsplit(a2, [2]) # (y 축) [1,2,3],[4,5,6], [7,8,9] 로 분할
print(b2, c2)

# hsplit() : 수평 분할, 2차원으로 분할
b2, c2 = np.hsplit(a2, [2]) # (x 축) colunm 기준 분할
print(b2, c2)

# dsplit() : 깊이 분할, 3차원으로 분할
a3 = np.arange(1, 28).reshape(3, 3, 3)
print(a3)
b3, c3 = np.dsplit(a3, [2])
print(b3)
print(c3)