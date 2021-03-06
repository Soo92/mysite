# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json

client_id = "IEu9KZec1kqGvGkpeZg8"
client_secret = "ynbWZ12hy6"
encText = urllib.parse.quote("간판")
url = "https://openapi.naver.com/v1/search/shop?query="+encText+"&display=10&start=1&sort=sim"
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    j_data = json.loads(response_body)
    # print(response_body.decode('utf-8'))
    print(j_data['total'])
else:
    print("Error Code:" + rescode)
