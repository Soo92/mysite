import numpy as np
import time
import csv
from selenium import webdriver

import hashlib, hmac, base64, requests, time, os
import pandas as pd

import urllib.request, json

from datetime import datetime
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

f_name=os.path.join(THIS_FOLDER,"keyw.csv")
m_name=os.path.join(THIS_FOLDER,"my.csv")
d_name=os.path.join(THIS_FOLDER,"del.csv")
r_name=os.path.join(THIS_FOLDER,"rel.csv")
c_name=os.path.join(THIS_FOLDER,"keyc.csv")
today=datetime.today().strftime("%y%m%d")

g_name=os.path.join(THIS_FOLDER,"chromedriver")

# 검색 API 계정
client_id = "IEu9KZec1kqGvGkpeZg8"
client_secret = "ynbWZ12hy6"

def cnt_check(type,idx,max):
    print(type+":"+str(idx)+"/"+str(max))
    a=1

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
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            j_data = json.loads(response_body)
            return_D=""
            # print(response_body.decode('utf-8'))
            max_prd=len(j_data['items'])
            if len(j_data['items'])>3:
                max_prd=3
            for cc in range(0,max_prd):
                return_D=return_D+"val!"+j_data['items'][cc]['title'].replace("<b>","").replace("</b>","").replace(","," ")+"lnk!"+j_data['items'][cc]['link'].split("?id=")[1]
            if return_D=="":
                return_D="상품없음"
            return(str(j_data['total'])+","+return_D)
        else:
            # print("Error Code:" + rescode)
            return("Err:" + rescode)
    except Exception as e:
        # print("Error Code2:" + str(e))
        time.sleep(1)
        return sel_api(keyw)

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

def reload():
    for it in (f_name,m_name,d_name,r_name,c_name):
        if (not os.path.isfile(it)):
            f = open(it, "w", encoding='euc-kr')
            if it==m_name:
                f.write("지정\n")
            elif it==d_name:
                f.write("제외\n")
            f.close()

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
        driver = webdriver.Chrome(g_name)
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
                keyword_path = '//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{}]/a'.format(i)
                key_num=driver.find_element_by_xpath(keyword_path).text.split("\n")[0]
                key_word=driver.find_element_by_xpath(keyword_path).text.split("\n")[1]
                while(int(key_num)!=p*20+i):
                    time.sleep(0.1)
                    keyword_path = '//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{}]/a'.format(i)
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
    row_count_p = sum(1 for row in rdr)-1
    f.close()
    f = open(f_name,'r')
    rdr = csv.reader(f)
    i=0
    for line in rdr:
        if i!=0:
            cnt_check("기존검색",i,row_count_p)
            line_exist=line[1].lower() in keyword_list_lower
            if (not line_exist):
                if not "기존" in line[0]:
                    line[0]="기존"+line[0]
                if today_file and len(line)>10 and line[10]!="":
                    row_list.append(",".join(line))
                else:
                    row_list.append(",".join(line[:10]))
                keyword_list.append(line[1])
                keyword_list_lower.append(line[1].lower())
        i+=1
    f.close()

    # 내가 지정한 키워드
    arr=np.array(keyword_list_lower)
    m = open(m_name,'r')
    rdr = csv.reader(m)
    row_count_m = sum(1 for row in rdr)-1
    m.close()
    m = open(m_name,'r')
    rdr = csv.reader(m)
    i=0
    for line in rdr:
        if i!=0:
            # 지정 키워드 추가
            cnt_check("지정검색",i,row_count_m)
            result = np.where(arr == line[0].lower())
            if (len(result[0])==0 and line[0]!=""):
                row_list.insert(1,"지정,"+line[0])
                keyword_list.insert(1,line[0])
                keyword_list_lower.insert(1,line[0].lower())
                arr=np.array(keyword_list_lower)
            elif (len(result[0])!=0 and result[0][0]>-1):
                cur_row=row_list[result[0][0]].split(",")
                if not "지정" in cur_row[0]:
                    cur_row[0]="지정"+cur_row[0]
                row_list[result[0][0]]=",".join(cur_row)
        i+=1
    m.close()
    # 내가 제외한 키워드
    arr=np.array(keyword_list_lower)
    d = open(d_name,'r')
    rdr = csv.reader(d)
    row_count_m = sum(1 for row in rdr)
    d.close()
    d = open(d_name,'r')
    rdr = csv.reader(d)
    i=0
    for line in rdr:
        if i!=0:
            # 제외 키워드 삭제
            cnt_check("제외검색",i,row_count_m)
            result2 = np.where(arr == line[0].lower())
            if (line[0]!="" and len(result2[0])!=0 and result2[0][0]>-1):
                row_list.pop(result2[0][0])
                keyword_list.pop(result2[0][0])
                keyword_list_lower.pop(result2[0][0])
                arr=np.array(keyword_list_lower)
        i+=1
    d.close()


    i=1
    maxi=120
    maxcc=3000
    for i in range(1,maxcc+1):
        key_tmp=[]
        while len(key_tmp)<5:
            if i==maxcc or i==len(keyword_list):
                print(key_tmp)
                break
            elif keyword_list[i]!="" and len(row_list[i].split(","))<3:
                key_tmp.append(keyword_list[i])
            i=i+1
        cnt_check("연관검색",i,maxcc)
        if len(key_tmp)==0:
            break
        kwds_string = ','.join(key_tmp)
        returnData = None
        while returnData is None:
            try:
                returnData = call_RelKwdStat(kwds_string)
                df = pd.DataFrame(returnData['keywordList'])
            except:
                print("efrrr")
                time.sleep(0.5)
                returnData = call_RelKwdStat(kwds_string)
                df = pd.DataFrame(returnData['keywordList'])
                pass
        df.rename({'compIdx':'경쟁도',
           'monthlyAveMobileClkCnt':'평균클릭(폰)',
           'monthlyAveMobileCtr':'평균클릭률(폰)',
           'monthlyAvePcClkCnt':'평균클릭(PC)',
           'monthlyAvePcCtr':'평클릭률(PC)',
           'monthlyMobileQcCnt':'검색(폰)',
           'monthlyPcQcCnt': '검색(PC)',
           'plAvgDepth':'노출광고수',
           'relKeyword':'키워드'},axis=1,inplace=True)
        df.to_csv(r_name,encoding='euc-kr')
        r = open(r_name,'r')
        rdr = csv.reader(r)
        r_i=0
        for line in rdr:
            if r_i!=0:
                result = np.where(arr == line[1].lower())
                if (len(result[0])!=0 and result[0][0]>-1):
                    cur_row=row_list[result[0][0]].split(",")
                    row_list[result[0][0]]=cur_row[0]+","+",".join(line[1:])
                    if len(cur_row)>10:
                        row_list[result[0][0]]=row_list[result[0][0]]+","+",".join(cur_row[10:])
                else:
                    if(len(keyword_list)>maxcc):
                        break
                    row_list.append("연관"+",".join(line))
                    keyword_list.append(line[1])
                    keyword_list_lower.append(line[1].lower())
                    arr=np.array(keyword_list_lower)
            r_i=r_i+1
        r.close()
    r = open(r_name,'r')
    rdr = csv.reader(r)
    for line in rdr:
        row_list[0]=today+","+",".join(line[1:])
        break
    r.close()

    # csv 파일 생성
    # 상품수 검색 제한 : 최대 25000제한이라;;
    # maxs=500+row_count_m
    # maxs=2
    maxs=maxcc
    f = open(f_name, "w",encoding='euc-kr')
    for i in range(len(row_list)):
        row_si=row_list[i].split(",")
        if i==0:
            if len(row_si)==10 or "" in row_si[10:]:
                row_list[i]=row_list[i]+",총조회,총클릭,상품수,top3,비율(조회),비율 (클릭)"
        else:
            cnt_check("상품수검색",i,len(row_list)-1)
            if len(row_si)==10 or "" in row_si[10:]:
                if "" in row_si[10:]:
                    row_si=row_si[:10]
                row_si[2]=(row_si[2].replace("< 10","5"))
                row_si[3]=(row_si[3].replace("< 10","5"))
                row_si.append(str(int(row_si[2])+int(row_si[3])))
                row_si.append(str(int(float(row_si[4])+float(row_si[5]))))
                if i<=maxs:
                    cnt_lnk=str(sel_api(keyword_list[i]))
                    if cnt_lnk.find("Err")<0 and float(cnt_lnk.split(",")[0]):
                        row_si.append(cnt_lnk)
                        row_si.append(str(int(float(cnt_lnk.split(",")[0])/(int(row_si[2])+int(row_si[3])+1))))
                        row_si.append(str(int(float(cnt_lnk.split(",")[0])/(float(row_si[4])+float(row_si[5])+1))))
                    else:
                        # print("-----------")
                        # print(cnt_lnk.split(","))
                        # print(float(cnt_lnk.split(",")[0]))
                        # print(cnt_lnk.find("Err")<0)
                        # print(cnt_lnk.find("Err")<0 and float(cnt_lnk.split(",")[0]))
                        # print("-----------")
                        row_si.append("0,?,?,?")
                else:
                    row_si.append("연관검색어,미확인,-,-")
                if "" in row_si[10:]:
                    print("" in row_si[10:])
                    print(row_si)
            row_list[i]=",".join(row_si)
        try:
            f.write(row_list[i]+"\n")
        except Exception as e:
            print(str(e))
            # print(row_list[i])
            # os.system("pause")
    f.close()
