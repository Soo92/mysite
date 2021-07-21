import requests
from bs4 import BeautifulSoup    #BeautifulSoup import

from urllib.request import urlopen, Request
from fake_useragent import UserAgent
import json

# fake_useragent 모듈을 통한 User-Agent 정보 생성
useragent = UserAgent()
# print(useragent.chrome)
# print(useragent.ie)
# print(useragent.safari)
# print(useragent.random)

# 헤더 선언 및 referer, User-Agent 전송
headers = {
    'User-Agent' : useragent.chrome
}

# 주식 데이터 요청 URL
url = 'https://www.samhwasnd.com/goods/view?no=1944'

# 주식 데이터 요청
html = urlopen(Request(url, headers=headers)).read().decode('utf-8')

# print(html)
soup = BeautifulSoup(html, 'html.parser')

img_list=soup.select('ul[class=pagination] li a img')
for idx, it in enumerate(img_list):
    if idx==0:
        main_img="https://www.samhwasnd.com"+it['src']
    elif idx==1:
        sub_img="https://www.samhwasnd.com"+it['src']
    else:
        sub_img=sub_img+","+"https://www.samhwasnd.com"+it['src']
print(main_img)
print(sub_img)

# detail=soup.select('div[class=goods_information_contents]')
# print(detail)

# sprice_type=soup.select('ul[class=ul_ship] li[1]')
# print(sprice)
# sprice=soup.select('ul[class=ul_ship] li[1] div table tbody tr td[2]')
# sprice_deal=soup.select('ul[class=ul_ship] li[1] div table tbody tr td[2]')
# sprice_free=soup.select('ul[class=ul_ship] li[1] div table tbody tr td[1]')
# sprice_each=soup.select('ul[class=ul_ship] li[1] div table tbody tr td[2]')
# sprice_ba=""
# sprice_re=""

# opt=soup.select('div[class=goods_option_area]')
# print(opt)
