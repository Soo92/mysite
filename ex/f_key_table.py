from io import BytesIO
from PIL import Image
import csv
import datetime
import openpyxl
import clipboard
import requests
import hashlib, hmac, base64, requests, time, os
import urllib.request, json
from urllib.request import urlopen, Request
import random
import shutil
from openpyxl import load_workbook
from openpyxl.chart import BarChart, LineChart, Reference, Series
from openpyxl.styles import Border, Alignment, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
import PIL
import io
import urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import zipfile
import os, time, numpy as np, pandas as pd
import xlsxwriter
from bs4 import BeautifulSoup    #BeautifulSoup import
import time

def set_df_to_sht(df,sht,y,x):
    dfy=y
    dfx=x
    for col in df.columns:
        sht.cell(dfy,dfx).value=col
        dfx=dfx+1
    for dfy in range(0,len(df)):
        dfx=x
        for col in df.columns:
            sht.cell(dfy+y+1,dfx).value=df.iloc[dfy][col]
            dfx=dfx+1
    return dfy+y+1

def set_chg_report():
# 엑셀데이터 가져오기
    in_keyword_per_cut=df_admin_dict["키워드 상위(%)"]
    in_keyword_cnt_cut=df_admin_dict["키워드 최대갯수"]
    ws_chg.cell(5,12).value=in_keyword_per_cut
    ws_chg.cell(6,12).value=in_keyword_cnt_cut
# 인기키워드 top 25개중 10개 추출
    arr_key_rank=[25]
    arr_key_cnt=[10]
# 유입 csv 데이터 추출
    df=df_web_dict["검색어-보고서"][["검색어","노출수","클릭수","전환수"]]
    df=df[1:]
    columnNames = df.columns
    for i in range(1,4):
        col=columnNames[i]
        df[col] = df[col].astype(str).str.replace(',', '')
        df=df.astype({col: int})
        df=df.sort_values(by=col, ascending=False)
        df2=df[df[col] > df[col].quantile((100-in_keyword_per_cut)/100)]
        df2=df2.head(in_keyword_cnt_cut)
        ws_chg.cell(6+i,11).value=col
        for j in range(0,df2.value_counts().size):
            ws_chg.cell(6+i,12+j).value=(df2.iloc[j,0]+"\r\n"+str(df2.iloc[j,i]))
            ws_chg.cell(6+i,12+j).alignment = Alignment(wrapText=True)
# 인기 csv 데이터 추출
    df=df_web_dict["인기검색어"]
    for i in range(1,len(df.columns)):
        col=df.columns[i]
        tmp_col=col.split(">")
        ws_chg.cell(11,11+i).value=("\r\n").join(tmp_col[0:len(tmp_col)-1])
        ws_chg.cell(11,11+i).alignment = Alignment(wrapText=True)
        ws_chg.cell(12,11+i).value=tmp_col[len(tmp_col)-1]
        ws_chg.column_dimensions[get_column_letter(11+i)].width = 10
    for x in range(1,len(df.columns)):
        pre=0
        pre_cnt=0
        for i in range(0,len(arr_key_rank)):
            if i>0:
                pre=arr_key_rank[i-1]
                pre_cnt=pre_cnt+arr_key_cnt[i-1]
            ws_chg.column_dimensions[get_column_letter(12+x)].width = 10
            df2=df.iloc[pre:arr_key_rank[i],x]
            df2=df2.sample(arr_key_cnt[i])
            df2=df2.sort_index()
            for y in range(0,df2.value_counts().size):
                mer_t=str(df2.index[y]+1)+")"+str(df2.iloc[y])
                ws_chg.cell(13+y+pre_cnt,11+x).value=mer_t
# 광고대비 매출 csv 추출
    print(df_web_dict["광고대비전환"].columns[1:])
    df=df_web_dict["광고대비전환"]
    df=df[df.columns[1:]].astype(str).replace(",","").astype(int)
    next_y=set_df_to_sht(df,ws_chg,5,2)+2

    df_gsum=df.groupby(df.index//4).sum()
    ws_chg.cell(next_y,2).value="월간"
    print(df_gsum)
    test()
    next_y=set_df_to_sht(df_gsum,ws_chg,next_y,2)+2
    print(next_y)

    # for i in range(1,len(df.columns)):
    #     col=df.columns[i]
    #     if i==2 or i==4:
    #         df[col] = df[col].str.replace(',', '')
    #         df=df.astype({col: float})
    # for x in range(1,len(df.columns)):
    #     for y in range(0,df.value_counts().size):
    #         ws_chg.cell(6+y,1+x).value=df.iloc[y,x]
    # make_chart("주간",df.value_counts().size+2,df.value_counts().size+5,"B6","F6",8)
    # make_chart("전체",6,df.value_counts().size+5,"J28","J39",35)
    #
    # tail_df_a=[96,48,16]
    # detail_df_a=[["반기","B36","F36",8],["분기","B25","F25",8],["월간","B14","F14",8]]
    # idx=0
    # last_y=y+1
    # for tl in tail_df_a:
    #     df=df.tail(tl)
    #     del_tail=tail_df_a[idx]/4
    #     arr_tmp=[]
    #     for y in range(0,df.value_counts().size):
    #         # print(df.iloc[y])
    #         tmp_idx=(int(y//del_tail))
    #         if len(arr_tmp) < tmp_idx+1:
    #             arr_tmp.append([df.iloc[y,1],df.iloc[y,2],df.iloc[y,3],df.iloc[y,4]])
    #         else:
    #             for j in range(1,4):
    #                 arr_tmp[tmp_idx][j]=arr_tmp[tmp_idx][j]+df.iloc[y,j+1]
    #     df_tmp=df
    #     ws_chg.cell(7+last_y,2).value=detail_df_a[idx][0]+" 부분합"
    #     for x in range(0,len(arr_tmp[0])):
    #         for y in range(0,len(arr_tmp)):
    #             ws_chg.cell(8+last_y+y,2+x).value=arr_tmp[y][x]
    #     make_chart(detail_df_a[idx][0],8+last_y,8+last_y+y,detail_df_a[idx][1],detail_df_a[idx][2],detail_df_a[idx][3])
    #     last_y=last_y+y+3
    #     idx=idx+1
    #
    # max_ad=df.tail(4).iloc[:,2].max()
    # next_month=nowDate[4:6]
    # ws_chg.cell(1,2).value=str(int(next_month)+1)+"월"
    # ws_chg.cell(2,3).value=int(max_ad)*4

def set_sell_report():
# 엑셀데이터 가져오기
    in_keyword_per_cut=df_admin_dict["키워드 상위(%)"]
    in_keyword_cnt_cut=df_admin_dict["키워드 최대갯수"]

    # 인기키워드 top 10
    arr_key_rank=[25]
    arr_key_cnt=[10]
    for row in ws['K13:K22']:
        for cell in row:
            tmp=int(cell.value.replace("~",""))
            if not tmp in arr_key_rank:
                arr_key_rank.append(tmp)
                arr_key_cnt.append(1)
            else:
                arr_key_cnt[len(arr_key_cnt)-1]=arr_key_cnt[len(arr_key_cnt)-1]+1
    # 제외키워드
    arr_key_exc=[]
    for i in range(25,27):
        cnt=11
        tmp_v=ws.cell(i,cnt).value
        while tmp_v!=None:
            arr_key_exc.append(tmp_v)
            cnt=cnt+1
            tmp_v=ws.cell(i,cnt).value
    arr_exc=("|").join(arr_key_exc)

# 유입 csv 데이터 추출
    tmp_file=find_file("검색어-보고서",FILE_FOLDER)
    tmp_file=os.path.join(FILE_FOLDER,tmp_file)
    df=pd.read_csv(tmp_file, encoding='utf-8-sig', skiprows=1)
    df=df[1:][["검색어","노출수","클릭수","전환수"]]
    columnNames = df.columns
    for i in range(1,4):
        col=columnNames[i]
        df[col] = df[col].astype(str).str.replace(',', '')
        df=df.astype({col: int})
        df=df.sort_values(by=col, ascending=False)
        df2=df[df[col] > df[col].quantile((100-in_keyword_per_cut)/100)]
        df2=df2.head(in_keyword_cnt_cut)
        ws.cell(6+i,11).value=col
        for j in range(0,df2.value_counts().size):
            ws.cell(6+i,12+j).value=(df2.iloc[j,0]+"\r\n"+str(df2.iloc[j,i]))
            ws.cell(6+i,12+j).alignment = Alignment(wrapText=True)

# 인기 csv 데이터 추출
    tmp_file=find_file("카테고리",FILE_FOLDER)
    tmp_file=os.path.join(FILE_FOLDER,tmp_file)
    df=pd.read_csv(tmp_file, encoding='utf-8-sig')
    for i in range(1,len(df.columns)):
        col=df.columns[i]
        tmp_col=col.split(">")
        ws.cell(11,11+i).value=("\r\n").join(tmp_col[0:len(tmp_col)-1])
        ws.cell(11,11+i).alignment = Alignment(wrapText=True)
        ws.cell(12,11+i).value=tmp_col[len(tmp_col)-1]
        ws.column_dimensions[get_column_letter(11+i)].width = 10
    for x in range(1,len(df.columns)):
        pre=0
        pre_cnt=0
        for i in range(0,len(arr_key_rank)):
            if i>0:
                pre=arr_key_rank[i-1]
                pre_cnt=pre_cnt+arr_key_cnt[i-1]
            ws.column_dimensions[get_column_letter(12+x)].width = 10
            df2=df.iloc[pre:arr_key_rank[i],[0,x]]
            df2=df2.sample(arr_key_cnt[i])
            df2=df2.sort_index()
            for y in range(0,df2.value_counts().size):
                mer_t=str(df2.iloc[y,1])+" > "+str(df2.iloc[y,0])
                ws.cell(13+y+pre_cnt,11+x).value=mer_t

# 광고대비 매출 csv 추출
    tmp_file=find_file("광고대비매출",FILE_FOLDER)
    tmp_file=os.path.join(FILE_FOLDER,tmp_file)
    df=pd.read_csv(tmp_file, encoding='utf-8-sig')

    for i in range(1,len(df.columns)):
        col=df.columns[i]
        if i==2 or i==4:
            df[col] = df[col].str.replace(',', '')
            df=df.astype({col: float})
    for x in range(1,len(df.columns)):
        for y in range(0,df.value_counts().size):
            ws.cell(6+y,1+x).value=df.iloc[y,x]
    make_chart("주간",df.value_counts().size+2,df.value_counts().size+5,"B6","F6",8)
    make_chart("전체",6,df.value_counts().size+5,"J28","J39",35)

    tail_df_a=[96,48,16]
    detail_df_a=[["반기","B36","F36",8],["분기","B25","F25",8],["월간","B14","F14",8]]
    idx=0
    last_y=y+1
    for tl in tail_df_a:
        df=df.tail(tl)
        del_tail=tail_df_a[idx]/4
        arr_tmp=[]
        for y in range(0,df.value_counts().size):
            # print(df.iloc[y])
            tmp_idx=(int(y//del_tail))
            if len(arr_tmp) < tmp_idx+1:
                arr_tmp.append([df.iloc[y,1],df.iloc[y,2],df.iloc[y,3],df.iloc[y,4]])
            else:
                for j in range(1,4):
                    arr_tmp[tmp_idx][j]=arr_tmp[tmp_idx][j]+df.iloc[y,j+1]
        df_tmp=df
        ws.cell(7+last_y,2).value=detail_df_a[idx][0]+" 부분합"
        for x in range(0,len(arr_tmp[0])):
            for y in range(0,len(arr_tmp)):
                ws.cell(8+last_y+y,2+x).value=arr_tmp[y][x]
        make_chart(detail_df_a[idx][0],8+last_y,8+last_y+y,detail_df_a[idx][1],detail_df_a[idx][2],detail_df_a[idx][3])
        last_y=last_y+y+3
        idx=idx+1

    max_ad=df.tail(4).iloc[:,2].max()
    next_month=nowDate[4:6]
    ws.cell(1,2).value=str(int(next_month)+1)+"월"
    ws.cell(2,3).value=int(max_ad)*4

    wb.save(FILE_FOLDER+'/'+startDate+'~'+nowDate+'_☆마케팅보고서.xlsx')

def set_desc_report():
    month_now=int(datetime.datetime.now().strftime('%m'))
    month_prev=(month_now+11)%12
    month_pprev=(month_now+10)%12
    day_now=int(datetime.datetime.now().strftime('%d'))
    df_mas_sum=df_web_dict["소재부분합리스트"].copy()[['대표이미지 URL','기본상품명','상품가격','네이버쇼핑 카테고리','노출수','클릭수','전환수','쇼핑몰 상품 ID']]
    if not isFirstWeek:
        ws_desc["B2"].value="마케팅 주간보고"
        ws_desc["B4"].value=str(month_prev)+"월 방문수 및 전환율"
        ws_desc["F4"].value=str(month_now)+"월(~"+str(day_now)+"일) 방문수 및 전환율"
        ws_desc["J5"].value="직전매출 도달률"
        ws_desc["B9"].value=str(month_prev)+"월 지출광고비"
        ws_desc["B10"].value=str(month_now)+"월 예정광고비"
        ws_desc["B13"].value="ㄴworst 4 외 항목은 주간광고상세를 참고하세요"
        rate=10
        df_mas_sum=df_mas_sum[df_mas_sum["노출수"] > df_mas_sum["노출수"].quantile((100-rate)/100)]
        # df_mas_sum=df_mas_sum[df_mas_sum["클릭수"] < df_mas_sum["클릭수"].quantile((rate*2)/100)]
        df_mas_sum=df_mas_sum.sort_values(by="클릭수", ascending=True).head(4)
    else:
        ws_desc["B2"].value="마케팅 월간보고"
        ws_desc["B4"].value=str(month_pprev)+"월 방문수 및 전환율"
        ws_desc["F4"].value=str(month_prev)+"월 방문수 및 전환율"
        ws_desc["J5"].value="직전대비 전환증액률"
        ws_desc["B9"].value=str(month_prev)+"월 지출광고비"
        ws_desc["B10"].value=str(month_now)+"월 필요광고비"
        ws_desc["D10"].fill=PatternFill("solid", fgColor="FFFFFF00")
        ws_desc["B13"].value="ㄴtop4 외 항목은 주간광고상세를 참고하세요"
        rate=10
        tmp_df1=df_mas_sum.sort_values(by="전환매출액(원)", ascending=False).head(4)
        tmp_df2=df_mas_sum.sort_values(by="전환수", ascending=False).head(4)
        df_mas_sum=pd.merge(tmp_df1,tmp_df2).head(4)
    y=14
    x=4
    df_mas_warn=df_web_dict["점검소재리스트"].copy()[['쇼핑몰 상품 ID','기본상품명','노출상품명','제한 사유']]
    warn_dict={
        "연관성 있는 카테고리":"카테고리 수정 요청/상품과 연관성 있는 카테고리로 수정해 주세요",
        "분할된 비율":"이미지 수정 요청/분할된 이미지는 서로 달라야 하며 분할된 비율이 동일해야 합니다.",
        "이미지 내 텍스트":"이미지 수정 요청/이미지 내 텍스트가 기재된 경우 광고 등록이 불가합니다.",
        "테두리, 공백이 확인":"이미지 수정 요청/테두리, 공백 등 품질이 떨어지는 이미지는 광고 진행이 불가합니다.",
        "무의미하게 반복나열":"상품명 수정 요청/상품과 관련이 없는 수식어로 반복나열되거나 유사 문구를 반복하여 기재할 수 없습니다."
    }
    for idx in range(0,len(df_mas_sum)):
        each_mas=df_mas_sum.iloc[idx]
        ws_ad.column_dimensions[colnum_string(x-2)].width = 6.5
        insert_img(each_mas['대표이미지 URL'],y,x-2,ws_desc)
        ws_desc.cell(y,x).value=each_mas['기본상품명']
        ws_desc.cell(y+1,x).value=each_mas['상품가격']
        ws_desc.cell(y+2,x).value=each_mas['네이버쇼핑 카테고리']
        ws_desc.cell(y,x+2).value=each_mas['쇼핑몰 상품 ID']
        ws_desc.cell(y+1,x+3).value=each_mas['노출수']
        ws_desc.cell(y+1,x+4).value=each_mas['클릭수']
        ws_desc.cell(y+1,x+5).value=each_mas['전환수']
        df_warn_each=df_mas_warn[(df_mas_warn["쇼핑몰 상품 ID"].astype(str)==each_mas['쇼핑몰 상품 ID'].astype(str))]
        if len(df_warn_each)>0:
            df_warn_each=df_warn_each.iloc[0]
            for key in warn_dict.keys:
                if key in df_warn_each["제한 사유"]:
                    fid_title=warn_dict[key].split("/")[0]
                    fid_detail=warn_dict[key].split("/")[1]
        else:
            feed_title="이미지 수정 요청"
            feed_detail="상품성 있는 이미지로 수정이 필요해보입니다."
        ws_desc.cell(y+1,x+2).value=feed_title
        ws_desc.cell(y+2,x+2).value=feed_detail
        y=y+4

def set_ad_report():
    df_all=df_web_dict["소재부분합리스트"].copy()
    df_all_sum=df_all.sum()[["노출수","클릭수","전환수","총비용(VAT포함,원)","전환매출액(원)"]]
    df_all_sum.loc["클릭률"]=(df_all_sum["클릭수"]*10000/df_all_sum["노출수"]//1)/100
    df_all_sum.loc["전환율"]=(df_all_sum["전환수"]*10000/df_all_sum["클릭수"]//1)/100
    y=6
    x=2
    for total_val in df_all.columns:
        if total_val in df_all_sum.index:
            ws_ad.cell(y-1,x).value=df_all_sum[total_val]
        ws_ad.cell(y,x).value=total_val
        if "소재1" == total_val:
            v_idx=0
            tmp_df_val=""
            for each_col in report_col_val:
                tmp_df_val = tmp_df_val + each_col
                tmp_df_val = tmp_df_val + report_col_val_del[v_idx]
                v_idx=v_idx+1
                ws_ad.cell(y-1,x).value=tmp_df_val+"\r\n(노출▶클릭순▶)"
                ws_ad.cell(y-1,x).alignment = Alignment(wrapText=True)
                ws_ad.row_dimensions[y-1].height = 115
            yy=2
            xx=x
            for gg in gg_val:
                ws_ad.cell(yy,xx).value=gg
                ws_ad.cell(yy,xx).fill=PatternFill("solid", fgColor=gg_col[gg_val.index(gg)])
                if xx==x+3:
                    yy=3
                    xx=x
                else:
                    xx=xx+1
        x=x+1
    y=y+1
    for df_y in range(0,len(df_all)):
        x=2
        for df_x in range(0,len(df_all.iloc[df_y])):
            ws_ad.cell(y,x).value=df_all.iloc[df_y,df_x]
            if "기본상품명" in df_all.columns[df_x]:
                ws_ad.cell(y,x).hyperlink = "https://smartstore.naver.com/signcody/products/"+str(df_all["쇼핑몰 상품 ID"].iloc[df_y])
                ws_ad.cell(y,x).style = "Hyperlink"
            elif "대표이미지 URL" in df_all.columns[df_x]:
                ws_ad.column_dimensions[colnum_string(x)].width = 7.5
                url = df_all["대표이미지 URL"].iloc[df_y]
                insert_img(url,y,x,ws_ad)
            elif "소재" in df_all.columns[df_x]:
                ws_ad.column_dimensions[colnum_string(x)].width = 30
                ws_ad.row_dimensions[y].height = 48
                ws_ad.cell(y,x).alignment = Alignment(wrapText=True)
                delim=str(ws_ad.cell(y,x).value).split("\r\n")[0]
                for gg in gg_val:
                    gg_idx=gg_val.index(gg)
                    if gg in delim:
                        ws_ad.cell(y,x).fill=PatternFill("solid", fgColor=gg_col[gg_idx])
            x=x+1
        y=y+1

def insert_img(url,y,x,sht):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    image_file = io.BytesIO(r.data)
    img = Image(image_file)
    size_b=sht.column_dimensions[colnum_string(x)].width*8
    img.width= size_b
    img.height = size_b
    cell_posi=get_column_letter(x)+str(y)
    img.anchor = cell_posi
    sht.add_image(img)

def driver_logout():
    global login_status
    if login_status:
        if store_id_exist:
            time.sleep(1)
            pre_logout("https://sell.smartstore.naver.com/#/logout")
        time.sleep(1)
        pre_ad_logout("https://searchad.naver.com/logout")
        login_status=False

def driver_execute(path):
    global driver_exist
    global login_status
    if not driver_exist:
        driver_init()
        driver_exist=True
    if not login_status:
        login_status=True
        time.sleep(1)
        if store_id_exist:
            pre_login("https://sell.smartstore.naver.com/#/bizadvisor/marketing")
        time.sleep(1)
        pre_ad_login("https://manage.searchad.naver.com/customers/"+ str(df_admin_dict["CUST_ID"])+"/reports/"+ str(df_admin_dict["검색어보고서"]))
    if driver.current_url!=path:
        time.sleep(1)
        driver.get(path)

def driver_init():
    global driver

    g_name=os.path.join(THIS_FOLDER,"chromedriver")
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    # options.add_argument("headless")
    prefs = {
      "download.default_directory": FILE_FOLDER,
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True
    }
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(g_name, options=options)
    driver.implicitly_wait(20)

# ---------------- 서브 모듈
def timer_start():
    global start_t
    start_t = time.time()

def timer_chk():
    print("time :", time.time() - start_t)

def find_file(fname,FOLDER):
    file_flist=os.listdir(FOLDER)
    for file_f in file_flist:
        if file_f.find(fname)>-1:
            return file_f
    return "False"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def make_dummydf(df,fname):
    df.to_csv(FILE_FOLDER+'/_'+fname+'.csv' , encoding='utf-8-sig',index = False)

def test():
    while True:
        clk=input("c or e or any~~")
        try:
            print(clk)
            if clk=="c":
                key=input("key")
                driver.find_element_by_xpath(key).click()
            elif clk=="e":
                break
            elif clk=="m":
                key=input("key")
                posi_m=driver.find_element_by_xpath(key)
                action = ActionChains(driver)
                action.move_to_element(posi_m).perform()
            else:
                key=input("key")
                print(driver.find_element_by_xpath(key).get_attribute("innerHTML"))
        except Exception as e:
            print("Error:" + str(e))

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

def call_RelKwd(_kwds_string):
    global BASE_URL,CUSTOMER_ID,API_KEY,SECRET_KEY
    BASE_URL = 'https://api.naver.com'
    CUSTOMER_ID = '392590'
    API_KEY = '01000000008fa2a584355277148cf5b1792f0a1650becf66b049812186ce69dbfb7cbf4ec3'
    SECRET_KEY = 'AQAAAACPoqWENVJ3FIz1sXkvChZQySFY24NP0GvvyT3R14cXaQ=='

    uri = '/keywordstool'
    method = 'GET'
    prm = {'hintKeywords' : _kwds_string , 'showDetail':1}
    # ManageCustomerLink Usage Sample
    returnData = None
    df = pd.DataFrame()
    # print(_kwds_string)
    repeat_time=0.5
    wait_time=3
    while returnData is None:
        try:
            r = requests.get(BASE_URL + uri, params=prm, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))
            returnData = r.json()
            df = pd.DataFrame(returnData['keywordList'])
        except Exception as e:
            if 'code' in returnData:
                time.sleep(wait_time)
                wait_time=wait_time+1
                print(_kwds_string)
                print(wait_time)
            time.sleep(repeat_time)
            r = requests.get(BASE_URL + uri, params=prm, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))
            returnData = r.json()
            df = pd.DataFrame(returnData['keywordList'])
            pass
        if not 'keywordList' in returnData:
            print(_kwds_string)
            print(returnData)
            return False

    # df.to_csv(FILE_FOLDER+"/sdfasdf.csv", encoding='utf-8-sig')
    df['총검색']=df['monthlyMobileQcCnt'].astype(str).replace("< 10",0).astype(float)+df['monthlyPcQcCnt'].astype(str).replace("< 10",0).astype(float)
    df['총클릭']=df['monthlyAveMobileClkCnt'].astype(float)+df['monthlyAvePcClkCnt'].astype(float)
    df.rename({'compIdx':'경쟁도',       'monthlyAveMobileClkCnt':'평균클릭(폰)',       'monthlyAveMobileCtr':'평균클릭률(폰)',
       'monthlyAvePcClkCnt':'평균클릭(PC)',       'monthlyAvePcCtr':'평클릭률(PC)',       'monthlyMobileQcCnt':'검색(폰)',
       'monthlyPcQcCnt': '검색(PC)',       'plAvgDepth':'노출광고수',       'relKeyword':'연관키워드'},axis=1,inplace=True)
    rate=0.95
    if len(df)>1:
        tmp_df=df[(df['총검색'] > df['총검색'].quantile(rate)) & (df['총클릭'] > df['총클릭'].quantile(rate))]
        while len(tmp_df)==0:
            tmp_df=df[(df['총클릭'] > df['총클릭'].quantile(rate))]
            rate=rate-0.05
        df=tmp_df
        df=df.sort_values(by="총클릭", ascending=False)
    return df

def make_new_name(old_name,df_rel):
    key_arr=old_name.split(" ")
    new_arr=[]
    for tmp_key in key_arr:
        tmp_rel=df_rel[df_rel["노출키워드"]==tmp_key]
        tmp_rel=tmp_rel["연관키워드"].copy().drop_duplicates().values
        if not tmp_key in tmp_rel:
            tmp_rel=np.append(tmp_rel,tmp_key)
        if len(tmp_rel)>0:
            rel_idx=random.randint(0, len(tmp_rel)-1)
            new_arr.append(tmp_rel[rel_idx])
    return " ".join(new_arr)

def get_cate_key(path):
    driver_execute(path)
    cate_df=df_web_dict["광고소재리스트"]["네이버쇼핑 카테고리"].copy().dropna().drop_duplicates().values
    cate_my=df_web_dict["광고소재리스트"]["네이버쇼핑 카테고리"].copy().dropna().drop_duplicates().tolist()
    cate_all_file=find_file("인기검색어.csv",THIS_FOLDER)
    if find_file(cate_all_file,THIS_FOLDER)!="False":
        cate_all_file_name=os.path.join(THIS_FOLDER,cate_all_file)
        df_cate_all=pd.read_csv(cate_all_file_name, encoding='utf-8-sig')
        df_cate_all_col=df_cate_all.columns.tolist()
        cate_my=np.setdiff1d(cate_my,df_cate_all_col)
    else:
        df_cate_all=pd.DataFrame()
    for cate in cate_my:
        cate_arr=cate.split(">")
        driver.find_element_by_xpath('//*[@id="18_device_0"]').click()
        driver.find_element_by_xpath('//*[@id="19_gender_0"]').click()
        driver.find_element_by_xpath('//*[@id="20_age_0"]').click()
        for i in range(0, len(cate_arr)):
            driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])["+str(i+1)+"]").click()
            driver.find_element_by_xpath("(//a[text()='"+cate_arr[i].strip()+"'])").click()
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/a').click()
        time.sleep(1)
        arr_pro=[]
        for p in range(0, 25):
            for i in range(1, 21):
                keyword_path = '//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{}]/a'.format(i)
                key_num=driver.find_element_by_xpath(keyword_path).text.split("\n")[0]
                key_word=driver.find_element_by_xpath(keyword_path).text.split("\n")[1].replace(" ","")
                while(int(key_num)!=p*20+i):
                    time.sleep(0.1)
                    keyword_path = '//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{}]/a'.format(i)
                    key_num=driver.find_element_by_xpath(keyword_path).text.split("\n")[0]
                    key_word=driver.find_element_by_xpath(keyword_path).text.split("\n")[1]
                if len(arr_pro)<int(key_num)+1:
                    arr_pro.append(key_word)
                else:
                    arr_pro[int(key_num)].append(key_word)
            driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
        df_cate_all[cate]=arr_pro
    if nowWeekDay=="월":
        cate_all_file=weekHold+"인기검색어.csv"
    else:
        cate_all_file=weekDel+"인기검색어.csv"
    cate_all_file_name=os.path.join(THIS_FOLDER,cate_all_file)
    df_cate_all.to_csv(cate_all_file_name, encoding='utf-8-sig', index = False)
    return df_cate_all[cate_df]
    # return keyword_list

def pre_logout(path):
    driver_execute(path)

def pre_ad_logout(path):
    driver_execute(path)

def pre_login(path):
    driver_execute(path)
    driver.find_element_by_xpath("//input[@id='loginId']").clear()
    driver.find_element_by_xpath("//input[@id='loginId']").send_keys("signcody4657")
    driver.find_element_by_xpath("//input[@id='loginPassword']").clear()
    driver.find_element_by_xpath("//input[@id='loginPassword']").send_keys("dsp3134233")
    driver.find_element_by_xpath("//input[@id='loginPassword']").send_keys(Keys.RETURN)

def pre_ad_login(path):
    driver_execute(path)
    driver.find_element_by_xpath("//a[@class='btn btn-lg btn-block btn-primary']").click()
    driver.find_element_by_xpath("//input[@id='uid']").clear()
    driver.find_element_by_xpath("//input[@id='uid']").send_keys("signcody")
    driver.find_element_by_xpath("//input[@id='upw']").clear()
    driver.find_element_by_xpath("//input[@id='upw']").send_keys("dsp3134233")
    driver.find_element_by_xpath("//input[@id='upw']").send_keys(Keys.RETURN)

def get_pr_report(path):
    driver_execute(path)
    element = driver.find_element_by_id("__naverpay")
    driver.switch_to.frame(element)
    time.sleep(1)
    driver.find_element_by_xpath("//a[@class='btn select_data']").click()
    driver.find_element_by_xpath('//div[@class="fix_range"]/ul/li[2]').click()
    driver.find_element_by_xpath('//span[@class="select_range"]').click()
    tmp_date1=""
    arr_pro=[]
    while True:
        tmp_dval=driver.find_element_by_xpath("//a[@class='btn select_data']/span/span[2]/em").get_attribute("innerHTML").replace(".","").replace(" ","")[2:]
        if tmp_date1!="" and tmp_date1==tmp_dval:
            break
        tmp_date1=tmp_dval
        tmp_date=tmp_dval[:2] + "/" + tmp_dval[2:4] + "월" + str((int(tmp_dval[4:6])+7)//7) + "주차"
        tmp_add=driver.find_element_by_xpath("//table[@class='tbl_list']/tbody/tr/td[5]").get_attribute("innerHTML")
        tmp_amt=driver.find_element_by_xpath("//table[@class='tbl_list']/tbody/tr/td[11]").get_attribute("innerHTML")
        tmp_buy=driver.find_element_by_xpath("//table[@class='tbl_list']/tbody/tr/td[13]").get_attribute("innerHTML")
        arr_pro.insert(0,[tmp_date,tmp_add*1,tmp_amt*1,tmp_buy*1])

        driver.find_element_by_xpath("//a[@class='btn pre']").click()
    df = pd.DataFrame(arr_pro)
    df.columns = ['주간', '광고비', '매출건수', '매출액']
    return df

def get_adp_report(path):
    driver_execute(path)
    time.sleep(1)
    arr_pro=[]
    from_col=[      '노출수','클릭수', '총비용(VAT포함,원)', '전환수', '전환매출액']
    arr_col=['주간', '노출수','클릭수', '광고비',            '전환수', '전환액']
    while True:
        tmp_dval=driver.find_element_by_xpath("//div[@style='background: rgb(255, 255, 255); color: rgb(51, 51, 51); line-height: 34px; width: 270px; font-size: 13px; font-weight: 600; text-align: center;']").get_attribute("innerHTML").replace(".","").replace(" ","")[2:]
        if driver.find_element_by_xpath("(//button[text()=' < '])").get_property('disabled'):
            break
        tmp_date=tmp_dval.split("~")[1]
        tmp_date=tmp_date[2:4] + "/" + tmp_date[4:6] + "월" + str((int(tmp_date[6:8])+7)//7) + "주차"

        tmp_arr=[tmp_date]
        par = driver.find_elements_by_xpath("//th")
        for eachf in from_col:
            idxd=par.index(driver.find_element_by_xpath("//th/div/div/span[text()='"+eachf+"']/../../.."))
            tmp_arr.append(int(driver.find_element_by_xpath("//tr[@class='summary-row']/td["+str(idxd+1)+"]").get_attribute("innerHTML").replace("원","")))
        arr_pro.insert(0,tmp_arr)
        driver.find_element_by_xpath("(//button[text()=' < '])").click()
    df = pd.DataFrame(arr_pro)
    df.columns = arr_col
    return df

def get_pr_keyword(path):
    driver_execute(path)
    driver.find_element_by_xpath("//a[@data-nclicks-code='stu.selling']").click()
    driver.find_element_by_xpath('//div[@class="selectize-input items ng-valid ng-pristine has-options full has-items"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@data-value="500"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@class="btn btn-sm btn-default progress-button progress-button-dir-horizontal progress-button-style-top-line"]').click()
    time.sleep(1)
    tmp_file=find_file("Product",FILE_FOLDER)
    tmp_file=os.path.join(FILE_FOLDER,tmp_file)
    df=pd.read_csv(tmp_file, encoding='utf-8-sig')[["상품명","상품번호(스마트스토어)","할인가(PC)","대분류","중분류","소분류","세분류","대표이미지 URL"]]
    os.remove(tmp_file)
    df["카테고리명"]=""
    df.loc[(df['세분류'].isnull()),"카테고리명"]=df['대분류']+">"+df['중분류']+">"+df['소분류']
    df.loc[(df['세분류'].notnull()),"카테고리명"]=df['대분류']+">"+df['중분류']+">"+df['소분류']+">"+df['세분류']
    df2=df[["상품명","상품번호(스마트스토어)"]].copy()
    df2["추가홍보문구1"]=""
    df2["추가홍보문구2"]=""
    df2["제외키워드"]=""
    tmp_file2=find_file("※상품별 부가정보",FILE_FOLDER)
    if find_file(tmp_file2,FILE_FOLDER)!="False":
        tmp_file2=os.path.join(FILE_FOLDER,tmp_file2)
        df2=pd.read_csv(tmp_file2, encoding='utf-8-sig')
    df=pd.merge(df,df2,how="left")
    df2.to_csv(FILE_FOLDER + "/※상품별 부가정보.csv", encoding='utf-8-sig' ,index = False)
    return df

def get_ad_report(path):
    driver_execute(path)
    driver.find_element_by_xpath('//button[@class="btn-sm dropdown-toggle btn btn-default"]').click()
    driver.find_element_by_xpath("(//button[text()='필터 만들기'])").click()
    driver.find_element_by_xpath('//button[@style="word-break: keep-all;"]').click()
    driver.find_element_by_xpath('//div[@class="pl-2 filter-checkbox"][2]').click()
    driver.find_element_by_xpath('//button[@class="btn btn-sm btn-default-blue apply-button"]').click()
    driver.find_element_by_xpath("(//span[text()='다운로드'])").click()
    time.sleep(1)
    tmp_file=find_file("보고서(주1회)",FILE_FOLDER)
    tmp_file=os.path.join(FILE_FOLDER,tmp_file)
    df=pd.read_csv(tmp_file, encoding='utf-8-sig', skiprows=1)
    os.remove(tmp_file)
    return df

def get_ad_mass(path):
    mas_file=find_file("mas",FILE_FOLDER)
    if mas_file=="False":
        driver_execute(path)
        driver.find_element_by_xpath('//button[@class="btn btn-default dropdown-toggle"]').click()
        driver.find_element_by_xpath("(//button[text()='쇼핑검색'])").click()
        driver.find_element_by_xpath("(//button[@id='campaigns-dropdown'])").click()
        driver.find_element_by_xpath("(//div[@style='position: absolute; top: 0px; left: 0px; will-change: transform; transform: translate(0px, 32px);']/div[text()=' 스토어팜 ']/input)").click()
        driver.find_element_by_xpath("(//button[text()='다운로드'])").click()
        tmp=driver.find_element_by_xpath("(//tbody[@class='has-data ng-star-inserted']/tr[1]/td[11]/elena-mass-result)").get_attribute("innerHTML")
        while tmp=="<!---->":
            driver.find_element_by_xpath('//button[@class="btn btn-sm btn-default btn-icon"]').click()
            time.sleep(5)
            tmp=driver.find_element_by_xpath("(//tbody[@class='has-data ng-star-inserted']/tr[1]/td[11]/elena-mass-result)").get_attribute("innerHTML")
        driver.find_element_by_xpath("(//tbody[@class='has-data ng-star-inserted']/tr[1]/td[11]/elena-mass-result)").click()
        time.sleep(1)
        zp_fname=find_file("mas",FILE_FOLDER)
        os.chdir(FILE_FOLDER)
        zipfile.ZipFile(zp_fname).extractall()
        os.remove(zp_fname)
        mas_file=find_file("mas",FILE_FOLDER)
        mas_file=os.path.join(FILE_FOLDER,mas_file)
        df=pd.read_csv(mas_file, encoding='utf-8-sig', skiprows=1)
        os.remove(mas_file)
        df.to_csv(FILE_FOLDER+'/'+nowDate+'_mas.csv', encoding='utf-8-sig',index = False)
        mas_file=find_file("mas",FILE_FOLDER)
        mas_file=os.path.join(FILE_FOLDER,mas_file)
    else:
        mas_file=os.path.join(FILE_FOLDER,mas_file)
        df=pd.read_csv(mas_file, encoding='utf-8-sig')

    g_id_arr=df["광고그룹 ID"].copy().drop_duplicates().values
    for g_id in g_id_arr:
        path="https://manage.searchad.naver.com/customers/"+str(df_admin_dict["CUST_ID"])+"/adgroups/"+str(g_id)
        driver_execute(path)
        driver.find_element_by_xpath("//tr[@class='summary-row']")
        driver.find_element_by_xpath("//button[text()='다운로드']").click()
        each_mas=find_file("소재 목록 "+nowDate,FILE_FOLDER)
        while each_mas!="False":
            each_mas=os.path.join(FILE_FOLDER,each_mas)
        btn_listup=driver.find_element_by_xpath('(//button[@class="btn-sm btn-toggle dropdown-toggle btn btn-default"])')
        if not "행 표시: 200" in btn_listup.text:
            action = ActionChains(driver)
            action.move_to_element(driver.find_element_by_xpath('(//div[@class="footer-box"])')).perform()
            btn_listup.click()
            driver.find_element_by_xpath("(//button[text()=200])").click()
        each_mas=find_file("소재 목록 "+nowDate,FILE_FOLDER)
        while each_mas=="False":
            each_mas=find_file("소재 목록 "+nowDate,FILE_FOLDER)
        each_mas=os.path.join(FILE_FOLDER,each_mas)
        df3=pd.read_excel(each_mas, engine='openpyxl', skiprows=[1])
        os.remove(each_mas)
        df3["클릭률(%)"]=df3["클릭률(%)"].astype(str).str.replace(",","").astype(float)
        df3["전환율(%)"]=df3["전환율(%)"].astype(str).str.replace(",","").astype(float)
        df3["광고수익률(%)"]=df3["광고수익률(%)"].astype(str).str.replace(",","").astype(float)
        df3=df3.dropna(subset=['소재 ID'])
        for i in range(0,len(df3)):
            main_id=df3.iloc[i]["소재 ID"]
            status=df3.iloc[i]["상태"]
            if status=="중지 : 소재 연동제한":
                mas_file=find_file("mas",FILE_FOLDER)
                if mas_file!="False":
                    mas_file=os.path.join(FILE_FOLDER,mas_file)
                    os.remove(mas_file)
                remove_s_id(main_id)
            else:
                if status=="중지 : 소재 노출제한":
                    df.loc[df["소재 ID"]==main_id,"제한 사유"]=get_warn_why(main_id)
                tmp_img_url=driver.find_element_by_xpath("//td[@data-value='"+str(main_id)+"']/following-sibling::td/div/div/div/div").get_attribute("style")
                tmp_img_url=tmp_img_url.split('url("')[1].split('");')[0]
                df.loc[df["소재 ID"]==main_id,"대표이미지 URL"]=tmp_img_url
                for x in df3.columns:
                    df.loc[df["소재 ID"]==main_id,x]=df3.iloc[i][x]
    df.loc[df["노출상품명"]=="","노출상품명"]=df["기본상품명"]
    df=df.drop(columns=['쇼핑몰 상품ID', '소재 입찰가', '상품명', '카테고리'])
    df=df.drop(df.loc[df["상태"]=="중지 : 소재 연동제한"].index)
    return df

def get_sum_mass():
    global report_col_val
    global report_col_val_del
    report_col_val=['소재현황',   '노출상품명',  '광고그룹 이름',  '평균노출순위', '노출수',  '클릭수',  '전환수', '전환율(%)',  '총비용(VAT포함,원)', '전환매출액(원)',     '소재 상태',    '입찰가',   '소재 ID',  '광고그룹 ID', '쇼핑몰 상품 ID']
    report_col_val_del=['\r\n',  '(',           ')\r\n',         '/',           '/',      '/',       '/',      '/',      '/',        '\r\n',      '/',            "\r\n",         '/',         '/',           ""]

    df_mas=df_web_dict["소재현황리스트"]
    df_mas_sum=df_mas.copy().groupby(['기본상품명','쇼핑몰 상품 ID','네이버쇼핑 카테고리','대표이미지 URL']).sum().reset_index()
    tmp_file2=find_file("※상품별 부가정보",FILE_FOLDER)
    if find_file(tmp_file2,FILE_FOLDER)!="False":
        tmp_file2=os.path.join(FILE_FOLDER,tmp_file2)
        df2=pd.read_csv(tmp_file2, encoding='utf-8-sig')
        df2.rename(columns = {'상품번호(스마트스토어)' : '쇼핑몰 상품 ID', '상품명':'기본상품명'}, inplace = True)
        df_mas_sum=pd.merge(df_mas_sum,df2)
    df_mas_sum=df_mas_sum.sort_values(by=['노출수','클릭수','총비용(VAT포함,원)'], ascending=[False,False,True])
    df_mas_sum["클릭률"]=(df_mas_sum["클릭수"]*10000/df_mas_sum["노출수"]//1)/100
    df_mas_sum["전환율"]=(df_mas_sum["전환수"]*10000/df_mas_sum["클릭수"]//1)/100
    df_mas_sum=df_mas_sum[['제외키워드','대표이미지 URL','기본상품명','상품가격','네이버쇼핑 카테고리','노출수','클릭수','클릭률','전환수','전환율','총비용(VAT포함,원)','전환매출액(원)','쇼핑몰 상품 ID','추가홍보문구1','추가홍보문구2']]
    df_grp_arr=df_mas['광고그룹 이름'].copy().drop_duplicates().values
    df_pid_arr=df_mas['쇼핑몰 상품 ID'].copy().drop_duplicates().values
    for df_idx in range(0,len(df_mas_sum)):
        this_pro_id=df_mas_sum.iloc[df_idx]['쇼핑몰 상품 ID']
        tmp_df=df_mas[df_mas['쇼핑몰 상품 ID'].astype(str)==str(this_pro_id)].copy()
        this_pro_gid=df_mas[df_mas['쇼핑몰 상품 ID'].astype(str)==str(this_pro_id)].copy()
        for sub_idx in range(0,len(tmp_df)):
            if not "소재"+str(sub_idx+1) in df_mas_sum.columns:
                df_mas_sum["소재"+str(sub_idx+1)]=""
            tmp_df_val=""
            v_idx=0
            for each_col in report_col_val:
                tmp_df_val = tmp_df_val + str(tmp_df.iloc[sub_idx][each_col]).replace(".0","")
                tmp_df_val = tmp_df_val + report_col_val_del[v_idx]
                v_idx=v_idx+1
            df_mas_sum["소재"+str(sub_idx+1)].iat[df_idx]=str(tmp_df_val)
    return df_mas_sum

def get_status_mass():
    global wait_val
    global badgg_val
    global gg_val
    global gg_col

    # 노출 상태 종류
    goodgg_val='양호 소재'
    goodgg_col='FF00B050'
    badgg_val='불량 소재'
    badgg_col='FFFF0000'
    chapri_val='입찰가 변경'
    chapri_col='FF0070C0'
    wait_val='대기 소재'
    wait_col='FFC65911'
    newgg_val='신규 소재'
    newgg_col='FFFFFF00'
    offgg_val='off 소재'
    offgg_col='FFAEAAAA'
    warngg_val='소재 점검 필요'
    warngg_col='FFFFC000'
    emptygg_val='빈 그룹'
    emptygg_col='FFFFFFFF'

    gg_val=[goodgg_val,badgg_val,chapri_val,wait_val,newgg_val,offgg_val,warngg_val,emptygg_val]
    gg_col=[goodgg_col,badgg_col,chapri_col,wait_col,newgg_col,offgg_col,warngg_col,emptygg_col]

    df_status=df_web_dict["광고소재리스트"].copy()
    df_report=df_web_dict["스토어팜-보고서"].copy()

    cut_rank=df_admin_dict['삭제순위(이하)']
    cut_show=df_admin_dict['삭제노출(이하)']
    cut_clk=df_admin_dict['삭제클릭(이하)']
    cut_buy=df_admin_dict['삭제전환(이하)']
    cut_pri_up=df_admin_dict['삭제입찰가(이상)']
    cut_pri_dwn=df_admin_dict['삭제입찰가(이하)']

    price_dwn_cut=df_admin_dict['입찰가상승순위(이상)']
    price_dwn_val=df_admin_dict['입찰가상승값']
    price_up_cut=df_admin_dict['입찰가하강순위(이하)']
    price_up_val=df_admin_dict['입찰가하강값']

    for i in range(0,len(df_report)):
        s_id=df_report.iloc[i]["소재"]
        for x in df_report.columns:
            df_status.loc[df_status["소재 ID"]==s_id,x]=df_report.iloc[i][x]
    df_status=df_status.drop(columns=['캠페인유형','캠페인','소재','광고그룹'])
    df_status.loc[df_status['노출상품명'].isnull(),"노출상품명"]=df_status['기본상품명']
    df_status_col=['평균노출순위','노출수','클릭수','전환수','총비용(VAT포함,원)','입찰가','전환매출액(원)']
    for each_col in df_status_col:
        df_status[each_col]=df_status[each_col].astype(str).str.replace(",","").astype(float)

    df_status["소재현황"]=goodgg_val
    df_status.loc[(df_status['평균노출순위']>=price_dwn_cut),"소재현황"]=chapri_val+"인상 " + df_status["입찰가"].astype(int).astype(str) + ">" + (df_status["입찰가"]+price_dwn_val).astype(int).astype(str)
    df_status.loc[(df_status['평균노출순위']<=price_up_cut),"소재현황"]=chapri_val+"인하 " + df_status["입찰가"].astype(int).astype(str) + ">" + (df_status["입찰가"]+price_up_val).astype(int).astype(str)
    df_status.loc[(df_status['평균노출순위']<=cut_rank) & (df_status['노출수']<=cut_show) & (df_status['클릭수']<=cut_clk) & (df_status['전환수']<=cut_buy)
    & ~((cut_pri_dwn < df_status['입찰가']) & (df_status['입찰가'] < cut_pri_up)),"소재현황"]=badgg_val
    if nextWeekDay==df_admin_dict["정기보고(요일)"]:
        df_status.loc[(df_status['노출수']==0),"소재현황"]=badgg_val
    else:
        df_status.loc[(df_status['노출수']==0),"소재현황"]=wait_val
    df_status.loc[df_status['제한 사유'].notnull(),"소재현황"]=warngg_val

    df_pid_arr=df_status['쇼핑몰 상품 ID'].copy().drop_duplicates().values
    df_grp_arr=df_status['광고그룹 이름'].copy().drop_duplicates().values
    for df_pid in df_pid_arr:
        tmp_df=df_status[df_status['쇼핑몰 상품 ID']==df_pid]
        df_grp_arr_each=tmp_df['광고그룹 이름'].copy().drop_duplicates().values
        grp_minus=np.setdiff1d(df_grp_arr,df_grp_arr_each)
        for x in grp_minus:
            next_each=len(df_status)
            df_status.loc[next_each,"소재현황"]=emptygg_val
            df_status.loc[next_each,"기본상품명"]=tmp_df["기본상품명"].iloc[0]
            df_status.loc[next_each,"노출상품명"]=tmp_df["노출상품명"].iloc[0]
            df_status.loc[next_each,"대표이미지 URL"]=tmp_df["대표이미지 URL"].iloc[0]
            df_status.loc[next_each,"상품가격"]=tmp_df["상품가격"].iloc[0]
            df_status.loc[next_each,"네이버쇼핑 카테고리"]=tmp_df["네이버쇼핑 카테고리"].iloc[0]
            df_status.loc[next_each,"네이버쇼핑 상품 ID"]=tmp_df["네이버쇼핑 상품 ID"].iloc[0]
            df_status.loc[next_each,"광고그룹 이름"]=x
            df_status.loc[next_each,"광고그룹 ID"]=df_status[df_status['광고그룹 이름']==x]['광고그룹 ID'].iloc[0]
            df_status.loc[next_each,"쇼핑몰 상품 ID"]=df_pid
    df_status=df_status.sort_values(by=['쇼핑몰 상품 ID','노출수','클릭수','총비용(VAT포함,원)','소재 상태','광고그룹 이름'], ascending=[False,False,False,True,False,True])
    for df_pid in df_pid_arr:
        tmp_df=df_status[df_status["쇼핑몰 상품 ID"]==df_pid]
        if tmp_df["소재현황"].iloc[0]!=warngg_val:
            st_x=10+len(tmp_df[tmp_df["소재현황"]==badgg_val])
            tmp_df=df_status[df_status["쇼핑몰 상품 ID"]==df_pid].iloc[st_x:]["광고그룹 이름"]
            df_status.loc[(df_status["쇼핑몰 상품 ID"]==df_pid) & (df_status["광고그룹 이름"].isin(tmp_df.values))
            & (df_status["소재 상태"]=="off"),"소재현황"]=offgg_val
            tmp_df=df_status[df_status["쇼핑몰 상품 ID"]==df_pid].iloc[:st_x]["광고그룹 이름"]
            df_status.loc[(df_status["쇼핑몰 상품 ID"]==df_pid) & (df_status["광고그룹 이름"].isin(tmp_df.values))
            & (df_status["소재현황"]==emptygg_val),"소재현황"]=newgg_val
    return df_status

def get_warn_mass():
    df=df_web_dict["광고소재리스트"]
    df_warn=df[df["상태"]=="중지 : 소재 노출제한"]
    for i in range(0,len(df_warn)):
        s_id=df_warn["소재 ID"].iloc[i]
        s_name=df_warn["기본상품명"].iloc[i]
        # s_name=" ".join(df_warn["기본상품명"].iloc[i].split(" ")[:2])
        img_link=df_warn["대표이미지 URL"].iloc[i]
        tmp_img_link=img_link.split(".")
        urllib.request.urlretrieve(img_link, OUTPUT_FOLDER+"\\"+s_name+"_"+s_id+"."+tmp_img_link[len(tmp_img_link)-1])
    return df_warn

def make_import_file():
    df_import_col=["점검소재리스트","소재현황리스트","소재부분합리스트"]
    for key in df_import_col:
        key_file=nowDate+"_"+key+".csv"
        key_file=os.path.join(OUTPUT_FOLDER,key_file)
        if key=="점검소재리스트":
            df_web_dict[key]=get_warn_mass()
        elif key=="소재현황리스트":
            df_web_dict[key]=get_status_mass()
        elif key=="소재부분합리스트":
            df_web_dict[key]=get_sum_mass()
        df_web_dict[key].to_csv(key_file, encoding='utf-8-sig',index = False)

def remove_s_id(s_id):
    action = ActionChains(driver)
    action.move_to_element(driver.find_element_by_xpath('//div[@class="inner-left"]')).perform()
    driver.find_element_by_xpath('//td[@data-value="'+s_id+'"]/preceding-sibling::td[1]/preceding-sibling::td[1]/preceding-sibling::td[1]/input').click()
    action.move_to_element(driver.find_element_by_xpath('//div[@class="inner-left"]')).perform()
    driver.find_element_by_xpath('//button[@class="ml-2 btn btn-default btn-sm"]').click()
    driver.find_element_by_xpath('//button[@class="btn btn-primary Confirm_modal-button__1Kwk6 btn btn-secondary"]').click()

def get_warn_why(s_id):
    if driver.find_element_by_xpath('(//button[@class="btn-sm btn-toggle dropdown-toggle btn btn-default"])').text!="행 표시: 200":
        driver.find_element_by_xpath('//button[@class="btn-sm btn-toggle dropdown-toggle btn btn-default"]').click()
        driver.find_element_by_xpath("(//button[text()=200])").click()
    # 행표시 200개 / 다음페이지 이동 / 노출가능 클릭
    row_posi = driver.find_element_by_xpath('//td[@data-value="'+s_id+'"]/preceding-sibling::td[1]/span/a')
    action = ActionChains(driver)
    try:
        action.move_to_element(row_posi).perform()
        row_posi.click()
    except Exception as e:
        row_posi_parent=driver.find_element_by_xpath('//td[@data-value="'+s_id+'"]/parent::tr/preceding-sibling::tr[1]/td[1]')
        action.move_to_element(row_posi_parent).perform()
        row_posi.click()
    row_detail=[]
    for row_detail_each in driver.find_elements_by_xpath('//div[@class="list-dot"]'):
        row_detail.append(row_detail_each.text.replace("더 알아보기",""))
    driver.find_element_by_xpath('//button[@class="modal-button btn btn-default"]').click()
    return "\r\n".join(row_detail)

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def make_chart(title,minR,maxR,cP1,cP2,wid):
    cats = Reference(ws, min_col=2, max_col=2, min_row=minR, max_row=maxR)
    value_ad = Reference(ws, min_col=3, max_col=3, min_row=minR, max_row=maxR)
    value_cnt = Reference(ws, min_col=4, max_col=4, min_row=minR, max_row=maxR)
    value_price = Reference(ws, min_col=5, max_col=5, min_row=minR, max_row=maxR)

    chart_ad = LineChart()
    chart_ad.add_data(value_ad)
    chart_ad.set_categories(cats)
    chart_ad.y_axis.axId = 200
    chart_ad.y_axis.title = '광고비'
    chart_ad.y_axis.majorGridlines = None
    s = chart_ad.series[0]
    s.graphicalProperties.line.solidFill = "0070C0"

    chart_cnt = LineChart()
    chart_cnt.add_data(value_cnt)
    chart_cnt.y_axis.title = "매출건"

    chart_cnt.title = title+"_매출건"
    chart_cnt.width = wid
    chart_cnt.height = 6
    chart_cnt.y_axis.crosses = "max"
    chart_cnt.legend.tagname="b"
    s = chart_cnt.series[0]
    s.graphicalProperties.line.solidFill = "F4B084"
    chart_cnt += chart_ad
    chart_cnt.legend=None

    chart_price = LineChart()
    chart_price.add_data(value_price)
    chart_price.y_axis.title = "매출액"

    chart_price.title = title+"_매출액"
    chart_price.width = wid+1
    chart_price.height = 6
    chart_price.y_axis.crosses = "max"
    s = chart_price.series[0]
    s.graphicalProperties.line.solidFill = "FFC000"
    chart_price += chart_ad
    chart_price.legend=None

    ws.add_chart(chart_cnt, cP1)
    ws.add_chart(chart_price, cP2)

# -------------------------------------------------------------------------------

def init():
    global THIS_FOLDER
    global nowDate
    global nowWeekDay
    global nextWeekDay
    global isFirstWeek
    global df_admin
    global df_admin_col
    global driver_exist
    global login_status
    global weekDel
    global weekHold

    weekDel="☆"
    weekHold="★"

    df_admin_col=["스토어","CUST_ID","광고","캠페인","CAMP_ID","정기보고(요일)","보고수신메일","최종보고일",
    "스마트스토어 ID","스마트스토어 PW","검색광고 ID","검색광고 PW","검색어보고서","스토어팜보고서",
    "키워드 상위(%)","키워드 최대갯수",
    "삭제순위(이하)","삭제노출(이하)","삭제클릭(이하)","삭제전환(이하)","삭제입찰가(이상)","삭제입찰가(이하)",
    "입찰가상승순위(이상)","입찰가상승값","입찰가하강순위(이하)","입찰가하강값","기본입찰가"]
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    driver_exist=False
    login_status=False
    days=["월","화","수","목","금","토","일"]
    nowDate=datetime.datetime.now().strftime('%Y%m%d')
    if int(datetime.datetime.now().strftime('%d'))<8:
        isFirstWeek=True
    else:
        isFirstWeek=False
    nowWeekDay=days[datetime.datetime.today().weekday()]
    nextWeekDay=days[(datetime.datetime.today().weekday()+8)%7]

def load_df_admin():
    file_admin=find_file("※광고주관리",THIS_FOLDER)
    if file_admin!="False":
        admin_file=os.path.join(THIS_FOLDER,file_admin)
        df_admin=pd.read_csv(file_admin, encoding='utf-8-sig')
    else:
        df_admin=pd.DataFrame(columns=df_admin_col)
        df_admin.to_csv(THIS_FOLDER+"/※광고주관리.csv", encoding='utf-8-sig', index=False)
    return df_admin

def update(admin_df):
    global FILE_FOLDER
    global OUTPUT_FOLDER
    global df_admin_dict

    df_admin_dict={}
    for key in df_admin_col:
        df_admin_dict[key]=admin_df[key]
    for filedel in THIS_FOLDER:
        if not "※" in filedel and weekDel in filedel and nowWeekDay=="월":
            del_fname=os.path.join(THIS_FOLDER,filedel)
            os.remove(del_fname)
        elif not "※" in filedel and weekHold in filedel and nowWeekDay!="월":
            del_fname=os.path.join(THIS_FOLDER,filedel)
            os.rename(del_fname, del_fname.replace(weekHold,weekDel))
    FILE_FOLDER=os.path.join(THIS_FOLDER,df_admin_dict["스토어"])
    createFolder(FILE_FOLDER)
    filedel_list=os.listdir(FILE_FOLDER)
    for filedel in filedel_list:
        if ".csv" in filedel:
            if not "※" in filedel and not nowDate in filedel:
                del_fname=os.path.join(FILE_FOLDER,filedel)
                os.remove(del_fname)
        elif df_admin_dict['광고'] in filedel:
            del_foldname=os.path.join(FILE_FOLDER,filedel)
            shutil.rmtree(del_foldname)
    OUTPUT_FOLDER = FILE_FOLDER+'//'+nowDate+"_"+df_admin_dict['광고']
    createFolder(OUTPUT_FOLDER)

def get_data_file():
    global df_web_dict
    global c_id

    df_web_col=["상품리스트","광고대비매출",
    "광고대비전환","광고소재리스트","인기검색어",
    "검색어-보고서","스토어팜-보고서"]
    df_web_dict={}
    for key in df_web_col:
        key_file=nowDate+"_"+key+".csv"
        key_file=os.path.join(FILE_FOLDER,key_file)
        if find_file(key,FILE_FOLDER)!="False":
            df_web_dict[key]=pd.read_csv(key_file, encoding='utf-8-sig')
        else:
            if store_id_exist:
                if key=="상품리스트":
                    df_web_dict[key]=get_pr_keyword("https://sell.smartstore.naver.com/#/products/origin-list")
                elif key=="광고대비매출":
                    df_web_dict[key]=get_pr_report("https://sell.smartstore.naver.com/#/bizadvisor/marketing")
            if key=="광고대비전환":
                df_web_dict[key]=get_adp_report("https://manage.searchad.naver.com/customers/"+str(df_admin_dict["CUST_ID"])+"/campaigns/"+str(df_admin_dict["CAMP_ID"]))
            elif key=="광고소재리스트":
                df_web_dict[key]=get_ad_mass("https://manage.searchad.naver.com/customers/"+ str(df_admin_dict["CUST_ID"])+"/tool/mass")
            elif key=="인기검색어":
                df_web_dict[key]=get_cate_key("https://datalab.naver.com/shoppingInsight/sCategory.naver")
            elif key=="검색어-보고서":
                df_web_dict[key]=get_ad_report("https://manage.searchad.naver.com/customers/"+ str(df_admin_dict["CUST_ID"])+"/reports/"+ str(df_admin_dict["검색어보고서"]))
            elif key=="스토어팜-보고서":
                df_web_dict[key]=get_ad_report("https://manage.searchad.naver.com/customers/"+ str(df_admin_dict["CUST_ID"])+"/reports/"+ str(df_admin_dict["스토어팜보고서"]))
        df_web_dict[key].to_csv(key_file, encoding='utf-8-sig',index = False)
    driver_logout()

def make_import_file():
    df_import_col=["점검소재리스트","소재현황리스트","소재부분합리스트"]
    for key in df_import_col:
        key_file=nowDate+"_"+key+".csv"
        key_file=os.path.join(OUTPUT_FOLDER,key_file)
        if key=="점검소재리스트":
            df_web_dict[key]=get_warn_mass()
        elif key=="소재현황리스트":
            df_web_dict[key]=get_status_mass()
        elif key=="소재부분합리스트":
            df_web_dict[key]=get_sum_mass()
        df_web_dict[key].to_csv(key_file, encoding='utf-8-sig',index = False)

def make_report_file():
    global wb
    global ws_desc
    global ws_chg
    global ws_sell
    global ws_ad

    wb = load_workbook(THIS_FOLDER+'\※마케팅보고.xlsx')
    ws_desc = wb['간이보고']
    ws_chg = wb['주간전환상세']
    ws_sell = wb['주간매출상세']
    ws_ad = wb['주간광고상세']

    set_desc_report()
    set_ad_report()
    set_chg_report()
    # if store_id_exist:
    #     set_sell_report()
    # else:
    #     set_sell_report()

    wb.save(OUTPUT_FOLDER+'/'+nowDate+'_☆마케팅보고서.xlsx')

timer_start()
init()

global store_id_exist
df_admin=load_df_admin()
for df_idx in range(0,len(df_admin)):
    update(df_admin.iloc[df_idx])
    if df_admin_dict["스마트스토어 ID"]!="":
        store_id_exist=True
    else:
        store_id_exist=False
    if df_admin_dict["광고"]=="검색광고":
        get_data_file()
        make_import_file()
        make_report_file()
        # set_data_to_ad()

if driver_exist:
    driver.close()
timer_chk()
