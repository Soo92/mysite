from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os, time, numpy as np, pandas as pd
import xlsxwriter
from bs4 import BeautifulSoup    #BeautifulSoup import

def get_pr_detail(path,arr_pro):
    if path=="":
        arr_pro.append([])
        return

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
            main_img="http://signcody.co.kr"+it.find('img')['src']
        elif idx==1:
            sub_img="http://signcody.co.kr"+it.find('img')['src']
        else:
            sub_img=sub_img+","+"http://signcody.co.kr"+it.find('img')['src']

    # print("m_"+main_img)
    # print("s_"+sub_img)

    tmp_detail=soup.select('div[class=goodsDescribe]')[0].contents
    # print(str(detail))
    detail=""
    for it in tmp_detail:
        detail= detail + str(it)
    # print(detail)

    opt_arr=[]
    opt_list=soup.select('div[class=goodsOption]')
    for it in opt_list:
        i_title=""
        i_name=""
        i_price=""
        i_count=""
        opt_p=it.select('div[class=optionFields] > div')
        for tit in opt_p:
            tmp_name=""
            tmp_price=""
            tmp_count=""
            for pr in tit.find_all('li'):
                tmp_s=pr.findAll(text=True)[0].replace("원 )","").replace("*","x").split(" ( ")
                if len(tmp_s)>1:
                    tmp_p=tmp_s[1].replace(",","").replace("+","")
                else:
                    tmp_p="0"
                if tmp_name=="":
                    tmp_name=tmp_s[0]
                    tmp_price=tmp_p
                    tmp_count="9999"
                else:
                    tmp_name=tmp_name+","+tmp_s[0]
                    tmp_price=tmp_price+","+tmp_p
                    tmp_count=tmp_count+",9999"
            i_title=i_title+"\n"+tit.select('div[class=title]')[0].findAll(text=True)[0]
            i_name=i_name+"\n"+tmp_name
            i_price=i_price+"\n"+tmp_price
            i_count=i_count+"\n"+tmp_count
        opt_arr.append([i_title.strip(),i_name.strip(),i_price.strip(),i_count.strip()])
    arr_pro.append([main_img,sub_img,"",detail,opt_arr[0][0],opt_arr[0][1],opt_arr[0][2],opt_arr[0][3],opt_arr[1][0],opt_arr[1][1],opt_arr[1][2],opt_arr[1][3]])

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
g_name=os.path.join(THIS_FOLDER,"chromedriver")
driver = webdriver.Chrome(g_name)

arr_pro=[]

path_list=[
"http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00019853","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015453","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024489","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024488","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0004&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00020075","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024578","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024967","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024625","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024968","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025411","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024769","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025410","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025417","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025416","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025425","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0008&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025361","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025106","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00018183","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025456","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025457","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025455","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025244","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025461","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025568","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025491","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025187","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025186","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025185","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025493","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0008&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025343","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025216","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00018950","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00019856","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024124","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024125","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024126","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025217","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024122","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024334","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025229","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025459","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025220","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025003","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025004","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024892","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00020128","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00018167","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00016029","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00016030","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00016123","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00018179","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025420","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025421","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025412","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00019858","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015603","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025150","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025151","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015604","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015605","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015606","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025215","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025205","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025206","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025468","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0004&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024290","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0004&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024294","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015992","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015996","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00016004","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00016005","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024335","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025431","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025292","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025454","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025534","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024275","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024277","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024276","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024274","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025532","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015476","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00017458","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025352","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025419","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025418","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025414","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0001&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025415","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025362","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025363","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025364","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025365","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025368","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025367","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025369","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025366","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024957","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024904","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025360","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024902","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024903","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00019873","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00019872","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00019874","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0009&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00018270","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0019&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015394","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0003&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00024768","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00025529","http://www.signcody.co.kr/subPages/goods/view.asp?C1=0007&C2=&C3=&sortMethod=&pageNumber=&goodsCode=00015988"
]
for path in path_list:
    get_pr_detail(path,arr_pro)

# os.system("pause")
driver.close()

df = pd.DataFrame(arr_pro)
df.to_excel(THIS_FOLDER+"/exexsc.xlsx")
