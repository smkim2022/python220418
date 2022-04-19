# ifelse.py
# 자둥 라인 주석 치리 : 선택 후 ctrl + / (cmd + /)
# score= int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score <= 90:
#     grade = "B"
# elif 70 <= score <= 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

# 반복구문
value = 5
while value > 0:
    print(value)
    value -= 1

print("전체 실행 종료")

lst = ["문자열",100,3.14]
for item in lst:
    print(item, type(item))

print(len(lst))

lst = [1,2,3,4,5,6,7,8,9]
for i in lst:
    if i > 5:
        break
    print("Itime:{0}".format(i))

lst = [1,2,3,4,5,6,7,8,9]
for i in lst:
    if i % 2 ==0:
        continue
    print("Itime:{0}".format(i))

# 수열함수
print(list(range(10)))
print(list(range(1,11)))

# 매뉴얼하게 루프를 도는 경우
for i in range(5):
    print(i)

print(range(10))

# 리스트 컴프리핸션(리스트 임베딩):한줄로 필터링, 루프, 가공까지 파이썬스럽다.
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])

# 필터함수:filter(), map(), reduce()함수
lst = [20, 25, 30]

iterL = filter(None, lst)
for i in iterL:
    print("Item:{0}".format(i))

print("---필터링---")

# 필터링 함수 정의(논리식에서 True면 포함)
def getBiggerThan20(i):
    # 수정(논리식)
    return i > 20

# 파이썬은 무조건 참조가 복사가 됨(레퍼런스가 넘어감, 포인터(?)가 아님)
iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print("Item:{0}".format(i))

# 람다함수로 정의
print("---람다함수---")
iterL = filter(lambda x:x>20, lst)
for i in iterL:
    print("Item:{0}".format(i)) ## 관용적 표현????
    # print("Item:$i") ## 