import requests
res = requests.get("https://www.google.com/")
# print("응답 코드 : ", res.status_code) # 200이면 정상, 403은 접근 할 수 없는 것

# if res.status_code == requests.codes.ok:
#     print("1, 정상")
# else:
#     print(res.status_code, "문제 발생")

res.raise_for_status() # 문제시 종료 하는 문법
# print("웹 스크래핑을 진행합니다.")

with open("google.html", "w", encoding="utf-8") as f:
    f.write(res.text)