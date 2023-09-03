import requests
import re

p = re.compile("ca.e") 
# . : 하나의 문자를 의미 > care, cafe, csae (O)| caffe (X)
# ^ (^de): 문자열의 시작 > desk, desti (O)| fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

# m = p.match("case")
# print(m.group()) # 매치되지 않으면 에러가 발생
# m = p.match("caffe") # print(m.group()) # 에러 발생 예제

def print_match(m):
    if m :
        print(m.group())
    else :
        print("매칭되지 않음")

m = p.match("careless") # amtch : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
