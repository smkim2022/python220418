# web1.py

#bs4 패키지에서 BeautifulSoup 모듈만 사용할 거야
from bs4 import BeautifulSoup

#메서드나 함수를 연속 호출:메서드 체인(인스턴스를 안받고 간결하게)
page = open("c:\\work\\test01.html", "rt", 
    encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#문서의 모든 <p>태그 검색
#print(soup.find_all("p"))

#첫번째 <p>태그 거색
#print(soup.find("p"))

#필터링: <p class="outer-text">컨텐츠</p>
#print(soup.find_all("p", class_="outer-text")) #단어 충돌 때문에 "_"로 붙였다.

#특정 id를 검색
#print(soup.find_all(id="first"))

#태그 안쪽에 문자열 검색
for item in soup.find_all("p"):
    #Tag안쪽의 문자열만 추출(.text)
    title = item.text
    #print(title.strip())
    title = title.replace("\n", "")
    title = title.replace("\t", "")
    print(title.strip())






