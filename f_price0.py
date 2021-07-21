from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os, time, numpy as np, pandas as pd
import xlsxwriter

def link_login(idx):
    if idx==0:
        actions = ActionChains(driver)
        element = driver.find_element_by_xpath("//div[@id='layout_header']/div/div/ul/li[@class='noline']/div/div")
        actions.move_to_element(element).perform()
        driver.find_element_by_xpath("//div[@id='layout_header']/div/div/ul/li[@class='noline']/div/div/div/div/ul/a").click()
    elif idx==1:
        driver.find_element_by_xpath("//li[@class='loginExistFalse']/a").click()
    driver.implicitly_wait(3)

    if idx==0:
        driver.find_element_by_xpath("//input[@id='userid']").clear()
        driver.find_element_by_xpath("//input[@id='userid']").send_keys("signcody4657")
        driver.find_element_by_xpath("//input[@id='password']").clear()
        driver.find_element_by_xpath("//input[@id='password']").send_keys("dsp3134233")
        driver.find_element_by_xpath("//input[@id='password']").send_keys(Keys.RETURN)
    elif idx==1:
        driver.find_element_by_xpath("//input[@id='loginUserID']").clear()
        driver.find_element_by_xpath("//input[@id='loginUserID']").send_keys("signcody")
        driver.find_element_by_xpath("//input[@id='loginUserPW']").clear()
        driver.find_element_by_xpath("//input[@id='loginUserPW']").send_keys("11111111")
        driver.find_element_by_xpath("//input[@id='loginUserPW']").send_keys(Keys.RETURN)

    time.sleep(2)
    driver.implicitly_wait(3)

def check_exist(xpath):
    if xpath!="":
        try:
            return driver.find_element_by_xpath(xpath).text.strip()
        except:
            return "X"

def get_product(arr,arr2,idx):
    i=1
    while True:
        try:
            driver.implicitly_wait(3)
            driver.find_element_by_xpath(cate_xpath[idx].format(i)).click()
            driver.implicitly_wait(3)
            time.sleep(2)
            get_item(arr,arr2,idx)
            i=i+1
        except Exception as e:
            # print(e)
            break

def get_item(arr,arr2,idx):
    j=1
    while True:
        try:
            # elem = driver.find_element_by_xpath("//div[@id='searchedItemDisplay']/ul/li[{}]".format(j))
            # print(elem.get_attribute("innerHTML"))

            elem_img = driver.find_element_by_xpath(img_xpath[idx].format(j)).get_attribute("src").strip()
            elem_link= driver.find_element_by_xpath(link_xpath[idx].format(j)).get_attribute("href").strip()
            elem_no= check_exist(no_xpath[idx].format(j))
            elem_title= check_exist(title_xpath[idx].format(j))
            elem_detail= check_exist(detail_xpath[idx].format(j))
            elem_price= check_exist(price_xpath[idx].format(j))
            ar_t = np.array(arr2)
            result = np.where(ar_t == elem_no)

            if (len(result[0])!=0 and result[0][0]>-1):
                tmp_arr=arr[result[0][0]]
                if (tmp_arr[5]!=elem_price and len(tmp_arr)<7):
                    arr[result[0][0]].append(elem_price)
            else:
                arr.append([elem_img , elem_link , elem_no , elem_title , elem_detail , elem_price])
                arr2.append(elem_no)
            j=j+1
        except Exception as e:
            # print(e)
            break

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
g_name=os.path.join(THIS_FOLDER,"chromedriver")

path_list=['https://www.howsign.com/shop/main/index.php']

cate_xpath=["(//td[@class='catebar'])[{}]/a"]
img_xpath=["//div[@id='searchedItemDisplay']/ul/li[{}]/div/div/a/img"]
page_xpath=["//div[@id='searchedItemDisplay']/ul/li[{}]/div/div/a/img"]
link_xpath=["//div[@id='searchedItemDisplay']/ul/li[{}]/ul/li[@class='caprlist_name_area']/a"]
no_xpath=["//div[@class='goodsList']/ul/li[{}]/a/div[@class='goodsname']"]
title_xpath=[]
detail_xpath=["//div[@id='searchedItemDisplay']/ul/li[{}]/ul/li[@class='goods_desc_area style_10_summary']"]
price_xpath=["//div[@class='goodsList']/ul/li[{}]/a/div[@class='goodsprice']"]

for path in path_list:
    idx=path_list.index(path)

    arr_pro=[]
    arr_key=[]
    driver = webdriver.Chrome(g_name)
    driver.get(path)

    get_product(arr_pro,arr_key,idx)
    link_login(idx)
    get_product(arr_pro,arr_key,idx)

    driver.close()
    df = pd.DataFrame(arr_pro)
    df.to_excel(THIS_FOLDER+"/도소매가_"+path.split(".")[1]+".xlsx")
