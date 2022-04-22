# DB3.py

import sqlite3

#연결객체를 만들기(먼저 메모리에서 연습)
#con = sqlite3.connect(":memory:")   ## 파일에 기록하지 말고 메모리에서만 작업
con = sqlite3.connect("c:\\work\\commit.db")   ## 파일에 기록
#구문을 수행할 커서 객체
cur = con.cursor()
#테이블 구조(테이블 스키마):SQL구문은 대소문자 구분안함
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick','010');")

#입력 파라미터 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#N건을 입력(2차원 2행2열, tuple 안에 tuple 존재)
datalist = (("tom","010-123"), ("dsp","010-333")) 
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
#작업을 완료하고 종료
con.commit()


