import csv
import datetime
import openpyxl
from openpyxl import load_workbook
from openpyxl.chart import BarChart, LineChart, Reference, Series
from openpyxl.styles import Border, Alignment
from openpyxl.utils import get_column_letter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import zipfile
import os, time, numpy as np, pandas as pd
import xlsxwriter
from bs4 import BeautifulSoup    #BeautifulSoup import

def find_file(fname):
    file_flist=os.listdir(FILE_FOLDER)
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
            else:
                key=input("key")
                print(driver.find_element_by_xpath(key).get_attribute("innerHTML"))
        except Exception as e:
            print("Error:" + str(e))

def get_cate_key(cate,arr_pro):
    path = 'https://datalab.naver.com/shoppingInsight/sCategory.naver'
    driver.get(path)
    cate_arr=cate.split(">>")
    # 기기별 전체 선택
    driver.find_element_by_xpath('//*[@id="18_device_0"]').click()
    # 성별 전체 선택
    driver.find_element_by_xpath('//*[@id="19_gender_0"]').click()
    # 연령별 전체 선택
    driver.find_element_by_xpath('//*[@id="20_age_0"]').click()
    # 분류 & 기간 선택
    for i in range(0, len(cate_arr)):
        driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])["+str(i+1)+"]").click()
        driver.find_element_by_xpath("(//a[text()='"+cate_arr[i]+"'])").click()
    # 조회하기 클릭
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/a').click()
    time.sleep(1)
    for p in range(0, 25):
        # 인기검색어 가져오기
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
                arr_pro.append([key_word])
            else:
                arr_pro[int(key_num)].append(key_word)
            # keyword_list.append(key_word)
        # 다음 페이지 넘기기
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
    # return keyword_list

def pre_login(path):
    driver.get(path)
    driver.find_element_by_xpath("//input[@id='loginId']").clear()
    driver.find_element_by_xpath("//input[@id='loginId']").send_keys("signcody4657")
    driver.find_element_by_xpath("//input[@id='loginPassword']").clear()
    driver.find_element_by_xpath("//input[@id='loginPassword']").send_keys("dsp3134233")
    driver.find_element_by_xpath("//input[@id='loginPassword']").send_keys(Keys.RETURN)

def pre_ad_login(path):
    driver.get(path)
    driver.find_element_by_xpath("//a[@class='btn btn-lg btn-block btn-primary']").click()
    driver.find_element_by_xpath("//input[@id='uid']").clear()
    driver.find_element_by_xpath("//input[@id='uid']").send_keys("signcody")
    driver.find_element_by_xpath("//input[@id='upw']").clear()
    driver.find_element_by_xpath("//input[@id='upw']").send_keys("dsp3134233")
    driver.find_element_by_xpath("//input[@id='upw']").send_keys(Keys.RETURN)

def get_pr_report(path,arr_pro):
    driver.get(path)

    element = driver.find_element_by_id("__naverpay")
    driver.switch_to.frame(element)
    driver.find_element_by_xpath("//a[@class='btn select_data']").click()
    driver.find_element_by_xpath('//div[@class="fix_range"]/ul/li[2]').click()
    driver.find_element_by_xpath('//span[@class="select_range"]').click()

    tmp_date1=""
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

def get_pr_keyword(path):
    driver.get(path)
    driver.find_element_by_xpath("//a[@data-nclicks-code='stu.selling']").click()
    driver.find_element_by_xpath('//div[@class="selectize-input items ng-valid ng-pristine has-options full has-items"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@data-value="500"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@class="btn btn-sm btn-default progress-button progress-button-dir-horizontal progress-button-style-top-line"]').click()
    time.sleep(1)

def get_ad_report(path):
    time.sleep(1)
    driver.get(path)
    driver.find_element_by_xpath('//button[@class="btn-sm dropdown-toggle btn btn-default"]').click()
    driver.find_element_by_xpath("(//button[text()='필터 만들기'])").click()
    driver.find_element_by_xpath('//button[@style="word-break: keep-all;"]').click()
    driver.find_element_by_xpath('//div[@class="pl-2 filter-checkbox"][2]').click()
    driver.find_element_by_xpath('//button[@class="btn btn-sm btn-default-blue apply-button"]').click()
    driver.find_element_by_xpath("(//span[text()='다운로드'])").click()
    time.sleep(1)

def get_ad_mass(path):
    time.sleep(1)
    driver.get(path)
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

def get_data_file():
    global driver

    filedel_list=os.listdir(FILE_FOLDER)
    for filedel in filedel_list:
        if not nowDate in filedel:
            del_fname=os.path.join(FILE_FOLDER,filedel)
            os.remove(del_fname)

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

    pre_login("https://sell.smartstore.naver.com/#/bizadvisor/marketing")

    today_graph = nowDate + "_광고대비매출(주단위).csv"
    if find_file(today_graph)=="False":
        arr_pro=[]
        get_pr_report("https://sell.smartstore.naver.com/#/bizadvisor/marketing",arr_pro)
        df = pd.DataFrame(arr_pro)
        df.columns = ['주간', '광고비', '매출건수', '매출액']
        df.to_csv(FILE_FOLDER+"/"+today_graph, encoding='utf-8-sig')

    tmp_file=find_file("Product_")
    if tmp_file=="False" and not nowDate in tmp_file:
        time.sleep(1)
        get_pr_keyword("https://sell.smartstore.naver.com/#/products/origin-list")
        time.sleep(1)
        tmp_file=find_file("Product_")
        chg_file_arr=tmp_file.split("_")
        os.rename(FILE_FOLDER+"/"+tmp_file, FILE_FOLDER+"/"+chg_file_arr[1]+"_"+chg_file_arr[0]+"_"+chg_file_arr[2])

    tmp_file=find_file("Product_")

    arr_pro=[]
    arr_cate=[]
    today_pro = nowDate + "_상품 리스트_판매중.csv"
    if find_file(today_pro)=="False":
        tmp_file=os.path.join(FILE_FOLDER,tmp_file)
        f = open(tmp_file, 'r', encoding='utf-8-sig')
        rdr = csv.reader(f)
        for line in rdr:
            arr_pro.append([line[4],line[0],line[11],line[41],line[42],line[43],line[44]])
            tmp_cate=""
            if line[44]!="":
                tmp_cate=line[41]+">>"+line[42]+">>"+line[43]+">>"+line[44]
            else:
                tmp_cate=line[41]+">>"+line[42]+">>"+line[43]
            if not tmp_cate in arr_cate:
                arr_cate.append(tmp_cate)
        df = pd.DataFrame(arr_pro)
        columnNames = df.iloc[0]
        df = df[1:]
        df.columns = columnNames
        df.to_csv(FILE_FOLDER + "/" + today_pro, encoding='utf-8-sig')

    today_cate = nowDate + "_카테고리 리스트_판매중.csv"
    if find_file(today_cate)=="False":
        arr_pro=[]
        arr_cate=arr_cate[1:]
        arr_pro.append(arr_cate)
        time.sleep(1)
        for cate_it in arr_cate:
            get_cate_key(cate_it,arr_pro)
        df = pd.DataFrame(arr_pro)
        columnNames = df.iloc[0]
        df = df[1:]
        df.columns = columnNames
        df.to_csv(FILE_FOLDER+"/" + today_cate, encoding='utf-8-sig')

    zp_fname=find_file("mas")
    if zp_fname=="False":
    # 검색광고 로그인
        pre_ad_login("https://manage.searchad.naver.com/customers/392590/reports/rtt-a001-000000000451507")
    # 검색어
        get_ad_report("https://manage.searchad.naver.com/customers/392590/reports/rtt-a001-000000000451507")
    # 스토어팜
        get_ad_report("https://manage.searchad.naver.com/customers/392590/reports/rtt-a001-000000000451508")
    # 광고소재리스트
        get_ad_mass("https://manage.searchad.naver.com/customers/392590/tool/mass")
        zp_fname=find_file("mas")
        os.chdir(FILE_FOLDER)
        zipfile.ZipFile(zp_fname).extractall()
        os.remove(zp_fname)

        na_list=os.listdir(FILE_FOLDER)
        for na in na_list:
            if not nowDate in na:
                os.rename(FILE_FOLDER+"/"+na, FILE_FOLDER+"/"+nowDate+"_광고시스템-"+na.replace("+","-"))
    driver.close()

def set_data_to_xls():
# 엑셀데이터 가져오기
    global wb
    global ws

    wb = load_workbook(THIS_FOLDER+'\key_table.xlsx')
    ws = wb['보고서']
    for row in ws['L7:AC22']:
        for cell in row:
            cell.value = None

    # 유입키워드 컷트라인
    in_keyword_per_cut=ws['L5'].value
    in_keyword_cnt_cut=ws['L6'].value

    # 인기키워드 top 10
    arr_key_rank=[]
    arr_key_cnt=[]
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
    tmp_file=find_file("검색어")
    tmp_file=os.path.join(FILE_FOLDER,tmp_file)
    f = open(tmp_file, 'r', encoding='utf-8-sig')
    rdr = csv.reader(f)
    arr_pro=[]
    for line in rdr:
        if len(line)>3 and line[3]!="-":
            arr_pro.append([line[3],line[4]*1,line[5]*1,line[9]*1])
    df = pd.DataFrame(arr_pro)
    columnNames = df.iloc[0]
    df = df[1:]
    df.columns = columnNames
    for i in range(1,4):
        col=columnNames[i]
        df[col] = df[col].str.replace(',', '')
        df=df.astype({col: int})
        df=df.sort_values(by=col, ascending=False)
        df2=df[df[col] > df[col].quantile((100-in_keyword_per_cut)/100)]
        df2=df2.head(in_keyword_cnt_cut)
        ws.cell(6+i,11).value=col
        for j in range(0,df2.value_counts().size):
            ws.cell(6+i,12+j).value=(df2.iloc[j,0]+"\r\n"+str(df2.iloc[j,i]))
            ws.cell(6+i,12+j).alignment = Alignment(wrapText=True)

# 인기 csv 데이터 추출
    tmp_file=find_file("카테고리")
    tmp_file=os.path.join(FILE_FOLDER,tmp_file)
    df=pd.read_csv(tmp_file, encoding='utf-8-sig')
    for i in range(1,len(df.columns)):
        col=df.columns[i]
        tmp_col=col.split(">>")
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
            while (df2.iloc[:,1].str.contains(arr_exc)).any():
                df2=df.iloc[pre:arr_key_rank[i],[0,x]]
                df2=df2.sample(arr_key_cnt[i])
            df2=df2.sort_index()
            for y in range(0,df2.value_counts().size):
                mer_t=str(df2.iloc[y,1])+" > "+str(df2.iloc[y,0])
                ws.cell(13+y+pre_cnt,11+x).value=mer_t

# 광고대비 매출 csv 추출
    tmp_file=find_file("광고대비매출")
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

    wb.save(FILE_FOLDER+'/'+nowDate+'_☆마케팅보고서+키워드테이블.xlsx')

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

def set_data_to_xls_keyword():
# 엑셀데이터 가져오기
    global wb
    global ws

    wb = load_workbook(THIS_FOLDER+'\key_table.xlsx')
    ws = wb['키워드테이블']

# 상품 csv 데이터 추출
    pro_file=find_file("상품 리스트")
    pro_file=os.path.join(FILE_FOLDER,pro_file)
    df_pro=pd.read_csv(pro_file, encoding='utf-8-sig')
    df_pro.rename(columns = {'상품번호(스마트스토어)' : '상품 ID', '할인가(PC)' : '판매가'}, inplace = True)

    mas_file=find_file("mas")
    mas_file=os.path.join(FILE_FOLDER,mas_file)
    df_mas=pd.read_csv(mas_file, encoding='utf-8-sig', skiprows=1)
    df_mas.rename(columns = {'쇼핑몰 상품ID' : '상품 ID'}, inplace = True)
    df_mas['노출상품명']=df_mas['노출상품명'].fillna(df_mas['기본상품명'])

    report_file=find_file("스토어팜-보고서")
    report_file=os.path.join(FILE_FOLDER,report_file)
    df_report=pd.read_csv(report_file, encoding='utf-8-sig', skiprows=1)
    df_report.rename(columns = {'소재' : '소재 ID', '총비용(VAT포함,원)': '광고비용', '전환매출액(원)': '전환액'}, inplace = True)

    sum_col_val=['노출수','클릭수','광고비용','전환수','전환액']
    report_col_val=['노출상품명',  '광고그룹 이름',  '평균노출순위', '노출수',  '클릭수',  '전환수',  '광고비용', '전환액',     '소재 상태',    '소재 입찰가',   '소재 ID',  '광고그룹 ID', '상품 ID']
    report_col_val_del=['(',      ')\r\n',         '/',           '/',      '/',       '/',      '/',        '\r\n',      '/',            "\r\n",         '/',         '/',           ""]
    total_col_val=['상품명','상품 ID','판매가','대분류','중분류','소분류','세분류','노출수','클릭수','광고비용','전환수','전환액']

    x=10
    for sum_val in sum_col_val:
        df_report[sum_val] = df_report[sum_val].astype(str).str.replace(',', '')
        df_report=df_report.astype({sum_val: float})
        tmp_sum=df_report[sum_val].sum()
        ws.cell(10,x).value=int(tmp_sum)
        x=x+1

    df_mas=pd.merge(df_mas,df_report,on="소재 ID",how="outer")
    df_mas=df_mas.sort_values(by=['소재 상태','상품 ID','클릭수','광고비용','노출수','광고그룹'], ascending=[False,True,False,True,False,False])
    df_mas=df_mas[report_col_val]

    df_mas_sum=df_mas.groupby('상품 ID').sum().reset_index()[['상품 ID','노출수','클릭수','광고비용','전환수','전환액']]
    df_mas_sum=df_mas_sum.sort_values(by=['노출수','클릭수','광고비용'], ascending=[False,False,True])

    for df_idx in range(0,len(df_mas_sum)):
        tmp_df=df_mas[df_mas['상품 ID']==df_mas_sum.iloc[df_idx]['상품 ID']]
        if not "소재"+str(len(tmp_df)) in df_mas_sum.columns:
            for sub_idx in range(0,len(tmp_df)):
                if not "소재"+str(sub_idx+1) in df_mas_sum.columns:
                    total_col_val.append("소재"+str(sub_idx+1))
                    df_mas_sum["소재"+str(sub_idx+1)]=""
        for sub_idx in range(0,len(tmp_df)):
            tmp_df_val=""
            v_idx=0
            for each_col in report_col_val:
                tmp_df_val = tmp_df_val + str(tmp_df.iloc[sub_idx][each_col]).replace(".0","")
                tmp_df_val = tmp_df_val + report_col_val_del[v_idx]
                v_idx=v_idx+1
            df_mas_sum.at[df_idx,"소재"+str(sub_idx+1)]=str(tmp_df_val)

    df_all=pd.merge(df_pro,df_mas_sum,on="상품 ID",how="outer")[total_col_val]
    df_all=df_all.sort_values(by=['노출수','클릭수','광고비용'], ascending=[False,False,True])
    df_all['상품명']=df_all['상품명'].fillna("삭제상품")

    y=12
    for df_y in range(0,len(df_all)):
        x=3
        for df_x in range(0,len(df_all.iloc[df_y])):
            ws.cell(y,x).value=df_all.iloc[df_y,df_x]
            if x>=15:
                ws.column_dimensions[colnum_string(x)].width = 30
                ws.row_dimensions[y].height = 48
                ws.cell(y,x).alignment = Alignment(wrapText=True)
            x=x+1
        y=y+1

    x=3
    for total_val in total_col_val:
        ws.cell(11,x).value=total_val
        x=x+1
    v_idx=0
    tmp_df_val=""
    for each_col in report_col_val:
        tmp_df_val = tmp_df_val + each_col
        tmp_df_val = tmp_df_val + report_col_val_del[v_idx]
        v_idx=v_idx+1
        ws.cell(8,15).value=tmp_df_val+"\r\n(노출▶클릭순▶)"
        ws.cell(8,15).alignment = Alignment(wrapText=True)
        ws.column_dimensions[colnum_string(15)].width = 30
        ws.row_dimensions[8].height = 100

    wb.save(FILE_FOLDER+'/'+nowDate+'_☆마케팅보고서+키워드테이블.xlsx')

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def init():
    global THIS_FOLDER
    global FILE_FOLDER
    global nowDate

    now = datetime.datetime.now()
    nowDate = now.strftime('%Y%m%d')
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FILE_FOLDER = THIS_FOLDER+'\자료'
    createFolder(FILE_FOLDER)

init()
# get_data_file()
# set_data_to_xls()
set_data_to_xls_keyword()
