import requests
from bs4 import BeautifulSoup    #BeautifulSoup import

from urllib.request import urlopen, Request
from fake_useragent import UserAgent
import json

# fake_useragent 모듈을 통한 User-Agent 정보 생성
useragent = UserAgent()
print(useragent.chrome)
print(useragent.ie)
print(useragent.safari)
print(useragent.random)

# 헤더 선언 및 referer, User-Agent 전송
headers = {
    'User-Agent' : useragent.chrome
}

# 주식 데이터 요청 URL
url = 'http://www.signcody.co.kr/subPages/goods/view.asp?C1=0008&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025343'

# 주식 데이터 요청
html = urlopen(Request(url, headers=headers)).read().decode('utf-8')

print(html)
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select('div[class=goodsOption]'):
    print(tag)
    print(tag.text.strip())
