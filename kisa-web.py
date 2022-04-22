# kisa-web.py

import re
import urllib.request
from bs4 import BeautifulSoup
hdrstr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for i in range(1,2):
    urlstring = ("https://www.krcert.or.kr/data/secNoticeList.do?page=" + str(i) +"&sort_code=&sort_code_name=&search_sort=title_name&search_word=")
    print(urlstring)

# for i in range(1,10):
#     urlstring = ("https://www.krcert.or.kr/data/secNoticeList.do?page=" + str(i) +"&sort_code=&sort_code_name=&search_sort=title_name&search_word=")
#     print(urlstring)

#     req = urllib.request.Request(urlstring, headers = hdrstr)

#     urlcontents = urllib.request.urlopen(req).read()
#     page = urlcontents.decode('utf-8', 'ignore')
#     soup = BeautifulSoup(page, 'html.parser')

#     list = soup.find_all('a')
#     for item in list:
#         try:
#             title = item
#             print(title)
#         except:
#             pass

#https://www.krcert.or.kr/data/secNoticeList.do?page=1&sort_code=&sort_code_name=&search_sort=title_name&search_word=
#<a href="/data/secNoticeView.do?bulletin_writing_sequence=66664&amp;queryString=cGFnZT0xJnNvcnRfY29kZT0mc29ydF9jb2RlX25hbWU9JnNlYXJjaF9zb3J0PXRpdGxlX25hbWUmc2VhcmNoX3dvcmQ9">Oracle Critical Patch Update 보안 업데이트 권고</a>