import numpy as np
# 날짜 datetime 인식 방법
date = np.array("2020-01-01", dtype=np.datetime64)
print(date)

# date 타입 연산
print(date + np.arange(12)) # 각각의 숫자를 dated에 추가로 더해서 배열 완성

# datetime 속 시간설정 방법
datetime = np.datetime64('2020-06-01 12:00') # 출력물 T는 시간
print(datetime)

datetime = np.datetime64('2020-06-01 12:00:12.34', 'ns') # 나노초 같은 경우 뒤에 ns를 붙여줘야한다.
print(datetime)