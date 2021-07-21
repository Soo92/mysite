import requests
from bs4 import BeautifulSoup    #BeautifulSoup import
import os, time, numpy as np, pandas as pd

from urllib.request import urlopen, Request
from fake_useragent import UserAgent
import json

def get_product(ur,app_pro):
    html1 = urlopen(Request(ur, headers=headers)).read()
    sp = BeautifulSoup(html1, 'html.parser')
    product_list = sp.select('td[width="25%"] div a img')
    for itt in product_list:
        print(str(product_list.index(itt))+"_detail_"+str(len(product_list)))
        itt=itt.parent
        link="https://www.howsign.com/shop"+itt['href'].replace("..","")
        get_detail(link,app_pro)

def get_detail(link,app_pro):
    html1 = urlopen(Request(link, headers=headers)).read()
    sp = BeautifulSoup(html1, 'html.parser')
    main_img = "https://www.howsign.com/shop" + sp.select('div[class="indiv"] span img')[0]['src'] .replace("..","")
    # sub_img = sp.select('div[class="indiv"] span img')
    title = sp.select('b[style="font:bold 12pt 돋움;"]')[0].findAll(text=True)[0].strip()
    # desc = sp.select('div[class="indiv"] span img')
    price = sp.select('span[id="price"]')[0].findAll(text=True)[0].replace(",","")
    detail_img = sp.select('div[id="contents"]')[0]

    detail_img=(str(detail_img).replace('src="/shop/lib/meditor/../..','src="https://www.howsign.com/shop').replace('src="/shop','src="https://www.howsign.com/shop'))
    opt_type = ""
    opt_name = ""
    opt_price = ""
    opt_list = sp.select('select[name="addopt[]"]')
    for ec in opt_list:
        opt_tye = ec['label']
        opt_namle=""
        opt_prile=""
        opt_name_l = ec.select('option')
        for eee in opt_name_l:
            tmpdd=eee.contents[0].replace(",","").split("\n(")
            tmp_n=tmpdd[0].strip()
            if len(tmpdd)==1:
                tmp_p=0
            else:
                tmp_p=tmpdd[1].split("원")[0]
            if eee["value"]!="":
                if opt_namle=="":
                    opt_namle=tmp_n
                    opt_prile=tmp_p
                else:
                    opt_namle=opt_namle + "," + tmp_n
                    opt_prile=str(opt_prile) + "," + str(tmp_p)
        opt_type = str(opt_type) + "\n" + str(opt_tye)
        opt_name = str(opt_name) + "\n" + str(opt_namle)
        opt_price = str(opt_price) + "\n" + str(opt_prile)
    opt_type = str(opt_type).strip()
    opt_name = str(opt_name).strip()
    opt_price = str(opt_price).strip()
    ship = 0
    for item in sp.select("div[style='width:100%;padding:10 10 10 10;overflow:hidden'] table td"):
        if not "(VAT포함)" in item.text:continue
        ship=item.text.split("포함)")[1].split("원")[0]

    app_pro.append([link,main_img,title,price,detail_img,opt_type,opt_name,opt_price,ship])
    # print("app_pro")
    # print(app_pro)

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

url = 'https://www.howsign.com/'
html = urlopen(Request(url, headers=headers)).read()
soup = BeautifulSoup(html, 'html.parser')

app_pro=[]

cate=[]
cate_list=soup.select('td[class=catebar] a')
for it in cate_list:
    cate.append("https://www.howsign.com"+it['href'])
# print(cate)

for it1 in cate:
    print(str(cate.index(it1))+"_cate_"+str(len(cate)))
    url = it1
    html = urlopen(Request(url, headers=headers)).read()
    soup = BeautifulSoup(html, 'html.parser')
    get_product(it1,app_pro)
    page_list = soup.select('a[class=navi]')
    for it in page_list:
        print(str(page_list.index(it))+"_page_"+str(len(page_list)))
        get_product("https://www.howsign.com"+it['href'],app_pro)

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

df = pd.DataFrame(app_pro)
df.columns = ['링크', '메인이미지', '제목', '가격', '상세', '옵션명', '옵션항목', '옵션가', '배송비']
df.rename(columns = {'old_nm' : 'new_nm'}, inplace = True)

df.to_excel(THIS_FOLDER+"/하우사인.xlsx")
