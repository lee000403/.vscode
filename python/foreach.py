import pandas as pd
import pymysql
import csv

df = pd.read_csv("score.csv")
file = open("score.csv", encoding="utf-8-sig")
data = []
read_csv = csv.reader(file)
for i, line in enumerate(list(read_csv)[1:], start=1):
    tmp = []
    tmp.append(str(i))
    tmp = tmp+line
    data.append(tmp)


print(data)