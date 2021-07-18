from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os, time, numpy as np, pandas as pd
import xlsxwriter
from bs4 import BeautifulSoup    #BeautifulSoup import

def get_pr_detail(path,arr_pro):
    driver = webdriver.Chrome(g_name)
    driver.get(path)

    time.sleep(1)
    idx=1
    main_img=""
    sub_img=""

    html=driver.find_element_by_xpath("//div[@class='contentWrap']").get_attribute("innerHTML").strip()
    soup = BeautifulSoup(html, 'html.parser')

    img_list=soup.select('div[class=imgList] ul li')
    for idx, it in enumerate(img_list):
        if idx==0:
            main_img="https://www.signcody.com"+it.find('img')['src']
        elif idx==1:
            sub_img="https://www.signcody.com"+it.find('img')['src']
        else:
            sub_img=sub_img+"\n"+"https://www.signcody.com"+it.find('img')['src']

    # print("m_"+main_img)
    # print("s_"+sub_img)

    detail=soup.select('div[class=goodsDescribe]')[0]
    print(detail)

# 필수옵션
    opt_list=soup.select('div[class=optionFields]')

# 다중옵션상품 \n 처리 추가
    opt_sn=opt_list[0].select('div[class=title]')
    if len(opt_sn)>0:
        opt_sn=opt_sn[0].findAll(text=True)[0]
    else:
        opt_sn=""
    title_s=""
    price_s=""
    opt_s=opt_list[0].find_all('li')
    for it in opt_s:
        tmp_s=it.findAll(text=True)[0].replace("원 )","").split(" ( ")
        if len(tmp_s)>1:
            tmp_p=tmp_s[1]
        else:
            tmp_p="0"
        if title_s=="":
            title_s=tmp_s[0]
            price_s=tmp_p
        else:
            title_s=title_s+","+tmp_s[0]
            price_s=price_s+","+tmp_p
    title_s=title_s.strip()
    price_s=price_s.strip()

# 추가옵션
    opt_pn=opt_list[1].select('div[class=title]')
    if len(opt_pn)>0:
        opt_pn=opt_pn[0].findAll(text=True)[0]
    else:
        opt_pn=""
    title_p=""
    price_p=""
    opt_p=opt_list[1].find_all('li')
    for it in opt_p:
        tmp_s=it.findAll(text=True)[0].replace("원 )","").split(" ( ")
        if len(tmp_s)>1:
            tmp_p=tmp_s[1]
        else:
            tmp_p="0"
        if title_p=="":
            title_p=tmp_s[0]
            price_p=tmp_p
        else:
            title_p=title_p+","+tmp_s[0]
            price_p=price_p+","+tmp_p
    title_p=title_p.strip()
    price_p=price_p.strip()

    arr_pro.append([main_img,sub_img,"",detail,opt_sn,title_s,price_s,"9999",opt_pn,title_p,price_p,"9999"])
    driver.close()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
g_name=os.path.join(THIS_FOLDER,"chromedriver")

arr_pro=[]

path="http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025420"
get_pr_detail(path,arr_pro)

df = pd.DataFrame(arr_pro)
df.to_excel(THIS_FOLDER+"/exexsc_"+path.split(".")[1]+".xlsx")
