# DemoTupleDict.py

# Tuple

tp = (1,2,3)
print(type(tp))
print(tp)
print(len(tp))
print(tp[0])

# 주로 데이터를 담아서 전달
def calc(a,b):
    return a+b, a*b

result = calc(3,4)
print(result)

args = (5,6)
# *는 튜플에 담아서 입력
print(calc(*args))


# 세트는 집합연산
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))

#다른 형식으로 변환:tuple ==> list로(타입캐스팅)
a = {1,2,3}
b = list(a)
print(b)
print(type(b))
b.append(4)
print(b)

###

#for k,v in device.items():
#    print(k,v)
