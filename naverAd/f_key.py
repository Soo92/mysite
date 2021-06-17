import numpy as np
import time
import csv
from selenium import webdriver

import hashlib, hmac, base64, requests, time
import pandas as pd

from datetime import datetime

f_name='keyw.csv'
r_name="rel.csv"
today=datetime.today().strftime("%y%m%d")

# 네이버 강고 API 키
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

f = open(f_name,'r')
rdr = csv.reader(f)
row_list = []
keyword_list = []

for line in rdr:
    # print(line)
    # print(line[0]+"/"+today)
    # print(line[0]==today)
    if False and line[0]!=today:
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
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[1]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000004'])").click()
        time.sleep(0.2)
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[2]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000108'])").click()
        time.sleep(0.2)
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[3]").click()
        driver.find_element_by_xpath("(//a[@data-cid='50000964'])").click()
        # 조회하기 클릭
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/a').click()
        time.sleep(1)
        row_list = [today+",키워드"]
        keyword_list = ["연관키워드"]
        for p in range(0, 25):
            # 인기검색어 가져오기
            for i in range(1, 21):
                keyword_path = f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/a'
                key_num=driver.find_element_by_xpath(keyword_path).text.split("\n")[0]
                key_word=driver.find_element_by_xpath(keyword_path).text.split("\n")[1]
                while(key_num==p*20+i):
                    time.sleep(0.1)
                    keyword_path = f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/a'
                    key_num=driver.find_element_by_xpath(keyword_path).text.split("\n")[0]
                    key_word=driver.find_element_by_xpath(keyword_path).text.split("\n")[1]
                row_list.append(key_num+","+key_word)
                keyword_list.append(key_word)
            # 다음 페이지 넘기기
            driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
            # print(keyword_list)
        driver.close()
    break

keyword_list_lower=list(map(lambda x: x.lower(), keyword_list))
arr=np.array(keyword_list_lower)
maxc=600
i=0
for line in rdr:
    if i==maxc:
        break
    result = np.where(arr == line[1].lower())
    # print("dd")
    # print(len(result[0]))
    # print(result)
    # print(line[1].lower())
    if (len(result[0])==0 and line[1]!=""):
        print(line[1].lower()+"/")
        row_list.append("기존"+",".join(line))
        keyword_list.append(line[1])
    i=i+1
f.close()

# https://hanshuginn.blogspot.com/2020/02/?m=0
# return된 결과 길이 확인
# print(len(call_RelKwdStat('원피스')['keywordList']))
arr=np.array(keyword_list_lower)
# 최대 5개의 키워드 입력 가능
i=0
while i < maxc/5:
    if "" in keyword_list[i*5+1:(i*5+6)]:
        break
    kwds_string = ','.join(keyword_list[i*5+1:(i*5+6)])
    try:
        returnData = call_RelKwdStat(kwds_string)
        df = pd.DataFrame(returnData['keywordList'])
    except:
        time.sleep(0.1)
        returnData = call_RelKwdStat(kwds_string)
        df = pd.DataFrame(returnData['keywordList'])
    print(str(i)+"/"+kwds_string)
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
    r_i=0
    r = open(r_name,'r')
    rdr2 = csv.reader(r)
    for line in rdr2:
        if r_i==0:
            r_i=r_i+1
            row_list[0]=",".join(line)
        result = np.where(arr == line[1].lower())
        if (len(result[0])!=0 and result[0][0]>-1):
            row_list[result[0][0]]=row_list[result[0][0]].split(",")[0]+",".join(line[1:])
        else:
            row_list.append("연관"+",".join(line))
            keyword_list.append(line[1])
            keyword_list_lower=list(map(lambda x: x.lower(), keyword_list))
            arr=np.array(keyword_list_lower)
    r.close()
    i=i+1

# csv 파일 생성
f = open(f_name, "w")
for i in range(len(row_list)):
    f.write(row_list[i]+"\n")

f.close()
