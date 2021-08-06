import csv
import openpyxl
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
    cate_arr=cate.split(chr(10))
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
    test()

global THIS_FOLDER
global FILE_FOLDER

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_FOLDER = THIS_FOLDER+'\자료'
createFolder(FILE_FOLDER)
filedel_list=os.listdir(FILE_FOLDER)
for filedel in filedel_list:
    del_fname=os.path.join(FILE_FOLDER,filedel)
    # os.remove(del_fname)

g_name=os.path.join(THIS_FOLDER,"chromedriver")
options = webdriver.ChromeOptions()
# # 창 숨기는 옵션 추가
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
#
# pre_login("https://sell.smartstore.naver.com/#/bizadvisor/marketing")

# arr_pro=[]
# get_pr_report("https://sell.smartstore.naver.com/#/bizadvisor/marketing",arr_pro)
# df = pd.DataFrame(arr_pro)
# df.columns = ['날짜', '광고비', '매출건수', '매출액']
# df.to_excel(FILE_FOLDER+"\광고대비매출(주단위).xlsx")

# time.sleep(1)
# get_pr_keyword("https://sell.smartstore.naver.com/#/products/origin-list")

arr_pro=[]
arr_cate=[]
tmp_file=find_file("Product_")
if tmp_file!="False":
    tmp_file=os.path.join(FILE_FOLDER,tmp_file)
    f = open(tmp_file, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        arr_pro.append([line[4],line[0],line[12],line[41],line[42],line[43],line[44]])
        tmp_cate=""
        if line[44]!="":
            tmp_cate=line[41]+chr(10)+line[42]+chr(10)+line[43]+chr(10)+line[44]
        else:
            tmp_cate=line[41]+chr(10)+line[42]+chr(10)+line[43]
        if not tmp_cate in arr_cate:
            arr_cate.append(tmp_cate)
    df = pd.DataFrame(arr_pro)
    columnNames = df.iloc[0]
    df = df[1:]
    df.columns = columnNames
    df.to_excel(FILE_FOLDER+"\상품 리스트_판매중.xlsx")

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
    df.to_excel(FILE_FOLDER+"\카테고리 리스트_판매중.xlsx")

# driver.close()
