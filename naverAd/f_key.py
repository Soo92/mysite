import numpy as np
import time
import csv
from selenium import webdriver

import hashlib, hmac, base64, requests, time, os
import pandas as pd

import urllib.request

from datetime import datetime

f_name='keyw.csv'
m_name="my.csv"
r_name="rel.csv"
today=datetime.today().strftime("%y%m%d")

# 검색 API 계정
client_id = "IEu9KZec1kqGvGkpeZg8"
client_secret = "ynbWZ12hy6"

def type_check(type,idx,max):
    print(type+":"+str(idx)+"/"+str(max))

def test_print(txt):
    time.sleep(2)
    print(txt)

def sel_api(keyw):
    encText = urllib.parse.quote(keyw)
    url = "https://openapi.naver.com/v1/search/shop?query="+encText+"&display=10&start=1&sort=sim"
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

# 네이버 광고 API 키
BASE_URL = 'https://api.naver.com'
CUSTOMER_ID = '392590'
API_KEY = '01000000008fa2a584355277148cf5b1792f0a1650becf66b049812186ce69dbfb7cbf4ec3'
SECRET_KEY = 'AQAAAACPoqWENVJ3FIz1sXkvChZQySFY24NP0GvvyT3R14cXaQ=='

def generate(timestamp, method, uri, secret_key):
    message = "{}.{}.{}".format(timestamp, method, uri)
#     hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
    hash = hmac.new(secret_key.encode("utf-8"), message.encode("utf-8"), hashlib.sha256)
    hash.hexdigest()
    return base64.b64encode(hash.digest())

def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(int(time.time() * 1000))
    signature = generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}


# 네이버 광고 API
def call_RelKwdStat(_kwds_string):
    dic_return_kwd = {}
    uri = '/keywordstool'
    method = 'GET'
    prm = {'hintKeywords' : _kwds_string , 'showDetail':1}
    # ManageCustomerLink Usage Sample
    r = requests.get(BASE_URL + uri, params=prm, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))
    r_data = r.json()
    return r_data

for it in (f_name,m_name,r_name):
    if (not os.path.isfile(it)):
        f = open(it, "w")
        f.close

row_list = [today+",키워드"]
keyword_list = ["연관키워드"]
keyword_list_lower = ["연관키워드"]

today_file=True
if os.stat(f_name).st_size == 0:
    today_file=False
else:
    f = open(f_name,'r')
    rdr = csv.reader(f)
    for line in rdr:
        if len(line)==0 or line[0]!=today:
            today_file=False
        break
    f.close()

if not today_file:
    driver = webdriver.Chrome('./chromedriver')
    # 쇼핑인사이트 이동
    path = 'https://datalab.naver.com/shoppingInsight/sCategory.naver'
    driver.get(path)
    # 기기별 전체 선택
    driver.find_element_by_xpath('//*[@id="18_device_0"]').click()
    # 성별 전체 선택
    driver.find_element_by_xpath('//*[@id="19_gender_0"]').click()
    # 연령별 전체 선택
    driver.find_element_by_xpath('//*[@id="20_age_0"]').click()
    # 분류 & 기간 선택
    try:
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[1]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000004'])").click()
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[2]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000108'])").click()
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[3]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000964'])").click()
    except:
        time.sleep(0.1)
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[1]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000004'])").click()
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[2]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000108'])").click()
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[3]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000964'])").click()
    # 조회하기 클릭
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/a').click()
    time.sleep(1)
    for p in range(0, 25):
        # 인기검색어 가져오기
        for i in range(1, 21):
            keyword_path = f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/a'
            key_num=driver.find_element_by_xpath(keyword_path).text.split("\n")[0]
            key_word=driver.find_element_by_xpath(keyword_path).text.split("\n")[1]
            while(int(key_num)!=p*20+i):
                time.sleep(0.1)
                keyword_path = f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/a'
                key_num=driver.find_element_by_xpath(keyword_path).text.split("\n")[0]
                key_word=driver.find_element_by_xpath(keyword_path).text.split("\n")[1]
            row_list.append(key_num+","+key_word)
            keyword_list.append(key_word)
            keyword_list_lower.append(key_word.lower())
        # 다음 페이지 넘기기
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
    driver.close()


# 기존 키워드
f = open(f_name,'r')
rdr = csv.reader(f)
row_count = sum(1 for row in rdr)
i=0
for line in rdr:
    i+=1
    type_check("기존검색",i,row_count)
    line_exist=line[1].lower() in keyword_list_lower
    if (not line_exist):
        line[0]="기존"
        if today_file and len(line)>10:
            row_list.append(",".join(line))
        else:
            row_list.append(",".join(line[:9]))
        keyword_list.append(line[1])
        keyword_list_lower.append(line[1].lower())
f.close()

# 내가 지정한 키워드
arr=np.array(keyword_list_lower)
m = open(m_name,'r')
rdr = csv.reader(m)
row_count = sum(1 for row in rdr)
i=0
for line in rdr:
    i+=1
    type_check("지정검색",i,row_count)
    result = np.where(arr == line[0].lower())
    if (len(result[0])==0 and line[0]!=""):
        row_list.append("지정,"+line[0])
        keyword_list.append(line[0])
        keyword_list_lower.append(line[0].lower())
        arr=np.array(keyword_list_lower)
    elif (len(result[0])!=0 and result[0][0]>-1):
        cur_row=row_list[result[0][0]].split(",")
        if not "지정" in cur_row[0]:
            cur_row[0]="지정"+cur_row[0]
        row_list[result[0][0]]=",".join(cur_row)
m.close()

i=0
maxi=120
while i < maxi:
    type_check("연관검색",i,maxi)
    if len(keyword_list[(i*5):(i*5+5)])==0:
        break
    kwds_string = ','.join(keyword_list[i*5+1:(i*5+6)])
    try:
        returnData = call_RelKwdStat(kwds_string)
        df = pd.DataFrame(returnData['keywordList'])
    except:
        time.sleep(0.1)
        returnData = call_RelKwdStat(kwds_string)
        df = pd.DataFrame(returnData['keywordList'])
    df = pd.DataFrame(returnData['keywordList'])
    df.rename({'compIdx':'경쟁정도',
       'monthlyAveMobileClkCnt':'월평균클릭수_모바일',
       'monthlyAveMobileCtr':'월평균클릭률_모바일',
       'monthlyAvePcClkCnt':'월평균클릭수_PC',
       'monthlyAvePcCtr':'월평균클릭률_PC',
       'monthlyMobileQcCnt':'월간검색수_모바일',
       'monthlyPcQcCnt': '월간검색수_PC',
       'plAvgDepth':'월평균노출광고수',
       'relKeyword':'연관키워드'},axis=1,inplace=True)
    df.to_csv(r_name,encoding='euc-kr')
    r = open(r_name,'r')
    rdr = csv.reader(r)
    r_i=0
    for line in rdr:
        if r_i==0:
            r_i=r_i+1
            row_list[0]=today+","+",".join(line[1:])
        else:
            result = np.where(arr == line[1].lower())
            if (len(result[0])!=0 and result[0][0]>-1):
                cur_row=row_list[result[0][0]].split(",")
                row_list[result[0][0]]=cur_row[0]+","+",".join(line[1:])
                if len(cur_row)>10:
                    row_list[result[0][0]]=row_list[result[0][0]]+","+",".join(cur_row[10:])
            else:
                if(len(keyword_list)>25000):
                    break
                row_list.append("연관"+",".join(line))
                keyword_list.append(line[1])
                keyword_list_lower.append(line[1].lower())
                arr=np.array(keyword_list_lower)
    r.close()
    if(len(keyword_list)>25000):
        break
    i=i+1

# csv 파일 생성
f = open(f_name, "w")
for i in range(len(row_list)):
    if i!=0:
        type_check("상품수검색",i,len(row_list))
        # sel_api(keyword_list[i])
    f.write(row_list[i]+"\n")
f.close()
