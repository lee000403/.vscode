import numpy as np

# 배열 연산

#broading casting
a1 = np.array([1, 2, 3])
print(a1)
print(a1 + 5)

a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
print(a1 + a2)

b2 = np.array([1, 2, 3]).reshape(3, 1)
print(b2)
print(a1 + b2)

# 산술 연산 다른 차원 배열이랑 연산 가능
a1 = np.arange(1, 10)
print(a1)
print(a1 + 1)
print(np.add(a1, 10)) # 더하기 함수 np.add

print(a1 - 2)
print(np.subtract(a1, 10)) # 빼기 함수 np.subtract

print(-a1)
print(np.negative(a1)) # 모든 인덱스를 -로 바꾼다. np.negative

print(a1 * 2)
print(np.multiply(a1, 2)) # 곱하기 함수 np.multiply

print(a1 / 2)
print(np.divide(a1, 2)) # 나누기 함수 np.divide

print(a1 // 2)
print(np.floor_divide(a1, 2)) # 나눗셈(내림) 함수 np.floor_divide

print(a1 ** 2)
print(np.power(a1, 2)) # 지수 연산 np.power

print(a1 % 2)
print(np.mod(a1, 2)) # 나머지 연산 np.mod

# 절대값 함수
# absolute(), abs() : 내장된 절대값 함수
a1 = np.random.randint(-10, 10, size=5)
print(a1)
print(np.absolute(a1))
print(np.abs(a1))

# 제곱/ 제곱근 함수
# square, sqrt : 제곱, 제곱근 함수
print(a1)
print(np.square(a1))
print(np.sqrt(a1)) # 제곱근 함수

# 지수 함수
a1 = np.random.randint(1, 10, size=5)
print(a1)
print(np.exp(a1)) # 지수 함수 np.exp (수학 : e^a1)
print(np.exp2(a1)) # 2의 제곱 함수 np.exp2 (수학 : 2^a1)
print(np.power(a1, 2)) # 제곱 함수 np.power (a1^2)

# 로그 함수
print(a1)
print(np.log(a1)) # 로그 함수 np.log (수학 : 밑이 e(자연 상수)인 log)
print(np.log2(a1)) # 밑이 2인 log 값
print(np.log10(a1)) # 밑이 10인 log 값

# 삼각함수도 있다.
# 검색을 해서 사용. np.sin(array) 이런 방식으로 사용
t = np.linspace(0, np.pi, 3)
print(t)
print(np.sin(t))
print(np.cos(t))
print(np.tan(t))

# 아크 삼각함수
x = [-1, 0, 1]
print(x)
print(np.arcsin(x))
print(np.arccos(x))
print(np.arctan(x))


# 집계 함수 (NAN 안전 모드 : 숫자가 없더라도 에러를 안띄우고 안전하게 지나간다.)
# sum(): 합 계산
a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)
print(a2.sum(), np.sum(a2)) # 둘다 가능한 사용 방법, 축을 기준으로 연산이 가능하다.
print(a2.sum(axis=0), np.sum(a2, axis=1))

# cumsum(): 누적합 계산
a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)
print(np.cumsum(a2)) # 누적 된 값이 하나하나 나온다.
print(np.cumsum(a2, axis=0))
print(np.cumsum(a2, axis=1))

# diff(): 차분 계산
print(a2)
print(np.diff(a2)) # 두 개의 인덱스 사이의 차분 값을 출력한다.
print(np.diff(a2, axis=0))
print(np.diff(a2, axis=1))

# prod(): 곱 계산
print(a2)
print(np.prod(a2))
print(np.prod(a2, axis=0))
print(np.prod(a2, axis=1))

# cumprod() : 누적 곱 계산
print(a2)
print(np.cumprod(a2))
print(np.cumprod(a2, axis=0))
print(np.cumprod(a2, axis=1))

# dot() / matmul(): 점곱/ 행렬곱 계산
print(a2)
b2 = np.ones_like(a2)
print(b2)
print(np.dot(a2, b2))
print(np.matmul(a2, b2))

# tensordot() : 텐서 곱 계산
# cross(): 백터 곱 계산

# inner() / outer() : 내적 / 외적
print(a2)
print(b2)
print(np.inner(a2, b2))
print(np.outer(a2, b2))

# mean(): 평균 계산
print(a2)
print(np.mean(a2))
print(np.mean(a2, axis=0))
print(np.mean(a2, axis=1))

# std(): 표준 편차 계산
print(a2)
print(np.std(a2))
print(np.std(a2, axis=0))
print(np.std(a2, axis=1))

# var() : 분산 계산
print(a2)
print(np.var(a2))
print(np.var(a2, axis=0))
print(np.var(a2, axis=1))

# min() : 최소값
print(a2)
print(np.min(a2))
print(np.min(a2, axis=0))
print(np.min(a2, axis=1))

# max() : 최대값
print(a2)
print(np.max(a2))
print(np.max(a2, axis=0))
print(np.max(a2, axis=1))

# argmin() : 최소값 인덱스, 위치 값이 인덱스로 나온다.
print(a2)
print(np.argmin(a2))
print(np.argmin(a2, axis=0))
print(np.argmin(a2, axis=1))

# argmax() : 최대값 인덱스, 위치 값이 인덱스로 나온다.
print(a2)
print(np.argmax(a2))
print(np.argmax(a2, axis=0))
print(np.argmax(a2, axis=1))

# mediam() : 중앙값, 실제 중앙값을 출력 mean이랑 다르다.
print(a2)
print(np.median(a2))
print(np.median(a2, axis=0))
print(np.median(a2, axis=1))

# percentile() : 백분위 수
a1 = np.array([0, 1, 2, 3])
print(a1)
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='linear'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='higher'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='lower'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='nearest'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='midpoint'))

# any(): 인덱스 중 하나라도 참이면 참 출력
a2 = np.array([[False, False, False],
               [False, True, True],
               [False, True, True]])
print(a2)
print(np.any(a2))
print(np.any(a2, axis=0))
print(np.any(a2, axis=1))

# all(): 인덱스 중 다 true이어야지 참 출력
a2 = np.array([[False, False, True],
               [True, True, True],
               [False, True, True]])
print(a2)
print(np.all(a2))
print(np.all(a2, axis=0))
print(np.all(a2, axis=1))

# 비교 연산자
# == : np.equal, != : np.not_equal, < : np.less. <= : np.less_equal, > : np.greater, >= np.greater_equal
a1 = np.arange(1, 10)  # True, False 값을 리턴해준다. (bool)
print(a1)
print(a1 == 5) # True, False 값을 리턴해준다.
print(a1 != 5)
print(a1 < 5)
print(a1 <= 5)
print(a1 > 5)
print(a1 >= 5)

a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
print(np.sum(a2))
print(np.count_nonzero(a2 > 5)) # 불리안 형태로 나오니 참인 값을 확인하려고 nonzero 사용
print(np.sum(a2 > 5))
print(np.sum(a2 > 5, axis=0))
print(np.sum(a2 > 5, axis=1))