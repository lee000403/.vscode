import pymysql
import pandas as pd
from sqlalchemy import create_engine
import csv

df = pd.read_csv("score.csv")
file = open("score.csv", encoding="utf-8-sig")
data = []
read_csv = csv.reader(file)
for i in list(read_csv)[1:]:
    data.append(i)

# pymysql.install_as_MySQLdb()
# engine = create_engine("mysql+mysqldb://root:1234@localhost:3306/school")
# conn = engine.connect()
# df.to_sql("student_info", con=conn, if_exists="append")

conn = pymysql.connect(host="localhost", user="root", password="1234",  charset="utf8", db="school")

curs = conn.cursor()
sql = """insert into student_info(id, name, school, height, korean, english, meth, science, sa, sw)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
curs.executemany(sql, data)
conn.commit()
# df.to_sql(name="student_info")

conn.close