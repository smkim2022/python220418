# DemoRE.py

import re

#dir(re)
#print(dir(re))

result = re.search("[0-9]*th", "35th")
#매칭 오브젝트
print(result)
print(result.group())
result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

print("--비교--")
result = re.search("[0-9]*th", "  35th")
#매칭 오브젝트
print(result)
print(result.group())
#result = re.match("[0-9]*th", "  35th")
#print(result)
# print(result.group())

print(bool(re.search("apple", "this is apple")))
print(bool(re.match("apple", "this is apple")))

#연도나 우편번호를 검색
year = re.search("\d{4}", "올해는 2022년 2203월입니다.")
print(year.group())
print(year)

postCode = re.search("\d{5}", "우리 동네는 52300")
print(postCode.group())
print(postCode)

