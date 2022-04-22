# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#우리 웹싸이트는 웹봇은 금지(크롤링)
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        # <span class="subject_fixed" data-role="list-title-text" title="레오폴드 FC660M PD 저소음 적축 화이트 핑크">
        #                 레오폴드 FC660M PD 저소음 적축 화이트 핑크
        # </span>
        #<span>태그의 attributes속성들
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        # title = span2.text 
                        title = item.text
                        #print(title.strip())
                        if (re.search('아이패드', title)):
                                print(title.strip())
                                # print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
