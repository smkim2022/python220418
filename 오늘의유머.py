# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#우리 웹싸이트는 웹봇은 금지(크롤링)
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,11):
        #오늘의 유머 웹 싸이트
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

#<a href="/board/view.php?table=bestofbest&amp;no=454253&amp;s_no=454253&amp;page=1" target="_top">윤석열 유퀴즈 출연  쉽게 비유하겠습니다</a>

        #<span>태그의 attributes속성들
        list = soup.find_all('td', attrs={'class':'subject'})
        for item in list:
                try:
                        title = item.find("a").text.strip()
                        #print(title.strip())
                        #if (re.search('아이패드', title)):
                        print(title)
                        # print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
