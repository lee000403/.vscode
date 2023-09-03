import numpy as np

# 비교 연산자

# np.isclose : 배열 두개가 가까우면 True, 아니면 False
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
b1 = np.array([1, 2, 3, 3, 4])
print(b1)
print(np.isclose(a1, b1))

a1 = np.array([np.nan, 2, np.inf, 4, np.NINF]) # nan : 없다, inf : 무한대
print(a1)
print(np.isnan(a1)) 
print(np.isinf(a1))
print(np.isfinite(a1)) # 무한대가 아닌 것만 True, 나머지는 False

# 불리언 연산자(Boolean Operators)
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
print((a2 > 5) & (a2 < 8))
print(a2[(a2 > 5) & (a2 < 8)]) # a2로 인하면 True 인 6,7 값 출력

print((a2 > 5) | (a2 < 8))
print(a2[(a2 > 5) | (a2 < 8)])

print((a2 > 5) ^ (a2 < 8)) # 인덱스 6,7(True인 부분) 을 빼고 난 나머지가 다 True 이다 (^ : &의 차집합)
print(a2[(a2 > 5) ^ (a2 < 8)])

print(~(a2 > 5)) # ~ : not 의미, 5초과인 것은 False라는 의미
print(a2[~(a2 > 5)])
