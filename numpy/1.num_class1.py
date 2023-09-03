import numpy as np
# 가로줄 axis 1, 세로줄 axis 0
a1 = np.array([1,2,3,4,5]) # 1차원 배열
print(a1)
print(type(a1)) # 넘파이 배열 타입
print(a1.shape) # 5개의 element가 있다. (5,) 쉼표 뒤에 숫자가 없으니 1차원 배열
print(a1[0], a1[1], a1[2], a1[3], a1[4])
a1[0] = 4 # 특정 인덱스에 값을 넣으니 변한다.
a1[1] = 5
a1[2] = 6
print(a1)

a2 = np.array([[1,2,3], [4,5,6], [7,8,9]]) # 2차원 배열
print(a2)
print(a2.shape) # (3,3) 다 나오므로 2차원 배열인 것을 알 수 있다.
print(a2[0,0], a2[1,1], a2[2,2])

a3 = np.array([ [[1,2,3], [4,5,6], [7,8,9]],  # 3차원 배열
                [[1,2,3], [4,5,6], [7,8,9]],
                [[1,2,3], [4,5,6], [7,8,9]] ])
print(a3)
print(a3.shape) # (3,3,3) 이 나오므로 shape 을 통해서 배열이 어떤 모양인지 알 수 있다.

np.zeros(10) # 모든 요소를 0으로 10개 채운다.
np.ones(10) # 모든 요소를 1로 10개 채운다.
np.ones((3,3)) # 2차원 형태의 1이 10개
np.full((3, 3), 1.23) # 1.23 요소로 (3,3) 형태로 채워진다.

# eye() : 단위 행렬 생성. 주대각선의 원소가 모두 1이고 나머지 원소는 모두 0인 정사각 행렬 (정사각형 형태로 나온다.)
print(np.eye(3))

# tri() : 삼각행렬 생성
print(np.tri(3)) # 정사각형 속 삼각형으로 1이 나온다.

# empty() : 초기화되지 않은 배열 생성 (장점 : 배열 생성비용 저렴, 빠름)
print(np.empty(10))

# _like() : 지정된 배열과 shape가 같은 행렬 생성
np.zeros_like(a1) # [0, 0, 0, 0, 0]
np.ones_like(a2) 
print(np.ones_like(a2))
np.full_like(a3, 10) # 인자 값 두개 넣어야한다. 어떤 value로 채워줘야 할지 선언 해야한다. 10으로 3차원 배열을 채워준다.
np.empty_like(a3)
print(np.empty_like(a2))
