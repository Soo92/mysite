import time
import csv
from selenium import webdriver

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
time.sleep(0.5)
driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[2]").click()
driver.find_element_by_xpath("(//a[@data-cid='50000108'])").click()
time.sleep(0.5)
driver.find_element_by_xpath("(//span[contains(@class,'select_btn')])[3]").click()
driver.find_element_by_xpath("(//a[@data-cid='50000964'])").click()
# 조회하기 클릭
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/a').click()
time.sleep(1)
keyword_list = []

for p in range(0, 25):
    # 인기검색어 가져오기
    for i in range(1, 21):
        keyword_path = f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/a'
        keyword_list.append(driver.find_element_by_xpath(keyword_path).text)
    # 다음 페이지 넘기기
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
    time.sleep(0.5)
    # print(keyword_list)

driver.close()

f = open('keyw.csv','r')
rdr = csv.reader(f)
for line in rdr:
    print(line)
f.close()

f = open("keyw.csv", "w")
for i in range(len(keyword_list)):
    f.write(keyword_list[i].split("\n")[0] + ',' + keyword_list[i].split("\n")[1] + '\n')
f.close()
