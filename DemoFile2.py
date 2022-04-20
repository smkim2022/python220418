# DemoFile2.py

#파일을 생성하기(유니코드로 저장)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
#f = open("c:/work/demo.txt", "wt", encoding="utf-8")
f.write("하나\n두번째\n세번째\n")
f.close()

#파일을 읽기
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
#전체 파일을 하나의 문자열 변수로 받기
result = f.read()
print(result)

#현재 파일포인터의 위치(책갈비)
print(f.tell())
#처음으로 리셋
f.seek(0)
#예를 들면 파일이 1GB, 2GB(로그파일)
print(f.readline(), end="")
print(f.readline(), end="")
#파일 전체를 리스트로 받기
f.seek(0)
lst = f.readlines() ## 복수인 경우 배열..
print(lst)
#print(f.tell())
f.close()

#기존 파일에 첨부하는 경우
f = open("c:\\work\\demo.txt", "a+", encoding="utf-8")
f.write("새루운 데이터\n")
print(result)

