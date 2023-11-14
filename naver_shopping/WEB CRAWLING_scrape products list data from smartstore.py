<<<<<<< HEAD
# 특정 스마트스토어 쇼핑몰의 상위 80개 상품 정보를 크롤링 하는 코드
# 인기도 순, 판매량 순으로 정렬하여 상위
# 사용 프레임 워크 : BeautifulSoup, pandas


import requests
from bs4 import BeautifulSoup
import json
import re

# 스마트스토어 쇼핑몰 url 입력받음
url = input('Enter url:')

# beautifulsoup 이용하여 parsing합니다.
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
all_scripts = soup.find_all('script')

# json 파일 리스트 명을 호출하여 출력하는 방식. (채택)
print('--- Edit method ---')
data = json.loads(all_scripts[0].get_text()[27:])

# storeNo를 string화 시킴
storeNo = data['smartStoreV2']['channelNo']
storeNostr = str(storeNo)

# 인기순 으로 상위 80개 크롤링
# 쇼핑몰 전체상품을 보는 페이지로 url 지정
urlpre = "https://smartstore.naver.com/i/v1/stores/"
urlpost = "/categories/ALL/products"
url = urlpre + storeNostr + urlpost

# 참조 유튜브 : https://www.youtube.com/watch?v=DqtlR0y0suo
# javascript가 웹사이트에 보여주는 모양으로 값을 바꾸기 전 서버 json 데이터를 불러온다고 함. 유튜브 영상 참조.
querystring = {"categoryId": "ALL", "categorySearchType": "DISPCATG", "sortType": "POPULAR", "page": "1",
               "pageSize": "80"}

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://smartstore.naver.com/loupe/category/2cffda4cfe7640df813533657a647ad5?st=POPULAR&dt=BIG_IMAGE&page=1&size=80",
    "Cookie": "NNB=7JHRUJKGXBPGI; ASID=af74dfd200000188194d6e5400000047",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

r = requests.request("GET", url, data=payload, headers=headers, params=querystring)

import pandas as pd

res = []
data = r.json()

for p in data['simpleProducts']:
    res.append(p)
df = pd.json_normalize(res)

# 크롤링 값을 csv로 저장
# 스토어명_popular_연월일시.CSV로 저장
import datetime
today = storeNostr + '_' + 'POPULAR_' + datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
df.to_csv(f'd:/smartstore/{today}.csv', encoding="utf-8-sig")

# 누적판매순 으로 상위 80개 크롤링
# 쇼핑몰 전체상품을 보는 페이지로 url 지정
urlpre = "https://smartstore.naver.com/i/v1/stores/"
urlpost = "/categories/ALL/products"
url = urlpre + storeNostr + urlpost

# 참조 유튜브 : https://www.youtube.com/watch?v=DqtlR0y0suo
# javascript가 웹사이트에 보여주는 모양으로 값을 바꾸기 전 서버 json 데이터를 불러온다고 함. 유튜브 영상 참조.
querystring = {"categoryId": "ALL", "categorySearchType": "DISPCATG", "sortType": "TOTALSALE", "page": "1",
               "pageSize": "80"}
payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://smartstore.naver.com/loupe/category/2cffda4cfe7640df813533657a647ad5?st=TOTALSALE&dt=BIG_IMAGE&page=1&size=80",
    "Cookie": "NNB=7JHRUJKGXBPGI; ASID=af74dfd200000188194d6e5400000047",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

r = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# PANDAS 프레임워크 사용
import pandas as pd
res = []
data = r.json()

for p in data['simpleProducts']:
    res.append(p)

df = pd.json_normalize(res)


# 크롤링 값을 csv로 저장
# 스토어명_TOTALSALE_연월일시.CSV로 저장
import datetime
today = storeNostr+'_'+'TOTALSALE_'+datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
df.to_csv(f'd:/smartstore/{today}.csv', encoding="utf-8-sig")






# 이하 코드는 사용하려다 실패한 코드들. 참조용으로 남겨둠.

#--------------------------------------------------------------
# 글자 순서로 출력하는 방식. 스토어 명이 바뀌면 사용불가한 방법.폐기
# print('--- first method ---')
# print(all_scripts[0].get_text()[8343:8352])
# storeNo = json.loads(all_scripts[0].get_text()[8343:8352])
# storeNostr = str(storeNo)
# print(storeNo)
#--------------------------------------------------------------

#--------------------------------------------------------------
# 또 다른 출력 방법. 폐기
# print('key:', data.keys())
# print('key:', data['smartStoreV2'].keys())
# print('---')

# for item in data['smartStoreV2']:
#    print('channelNo:',item[0:19])
#--------------------------------------------------------------

#--------------------------------------------------------------
# 또 다른 출력 방법. 폐기
# print('--- second method ---')
# for number, script in enumerate(all_scripts):
#    if '{"smartStoreV2"' in script.text:
#        print(number, script.text[:100])
# jsonObj = None

# for s in scripts:
#    if 'window.__PRELOADED_STATE__ = ' in s.text:
#        script = s.text

# script = script.split('window.__PRELOADED_STATE__ = ')[0]
# script = script.split('/script')[0]
#
#        jsonStr = script
#        jsonObj = json.loads(jsonStr)

# for value in jsonObj['smartStoreV2']:
#   print ('ID: '+ (value['channelNo']))
=======
# 특정 스마트스토어 쇼핑몰의 상위 80개 상품 정보를 크롤링 하는 코드
# 인기도 순, 판매량 순으로 정렬하여 상위
# 사용 프레임 워크 : BeautifulSoup, pandas


import requests
from bs4 import BeautifulSoup
import json
import re

# 스마트스토어 쇼핑몰 url 입력받음
url = input('Enter url:')

# beautifulsoup 이용하여 parsing합니다.
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
all_scripts = soup.find_all('script')

# json 파일 리스트 명을 호출하여 출력하는 방식. (채택)
print('--- Edit method ---')
data = json.loads(all_scripts[0].get_text()[27:])

# storeNo를 string화 시킴
storeNo = data['smartStoreV2']['channelNo']
storeNostr = str(storeNo)

# 인기순 으로 상위 80개 크롤링
# 쇼핑몰 전체상품을 보는 페이지로 url 지정
urlpre = "https://smartstore.naver.com/i/v1/stores/"
urlpost = "/categories/ALL/products"
url = urlpre + storeNostr + urlpost

# 참조 유튜브 : https://www.youtube.com/watch?v=DqtlR0y0suo
# javascript가 웹사이트에 보여주는 모양으로 값을 바꾸기 전 서버 json 데이터를 불러온다고 함. 유튜브 영상 참조.
querystring = {"categoryId": "ALL", "categorySearchType": "DISPCATG", "sortType": "POPULAR", "page": "1",
               "pageSize": "80"}

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://smartstore.naver.com/loupe/category/2cffda4cfe7640df813533657a647ad5?st=POPULAR&dt=BIG_IMAGE&page=1&size=80",
    "Cookie": "NNB=7JHRUJKGXBPGI; ASID=af74dfd200000188194d6e5400000047",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

r = requests.request("GET", url, data=payload, headers=headers, params=querystring)

import pandas as pd

res = []
data = r.json()

for p in data['simpleProducts']:
    res.append(p)
df = pd.json_normalize(res)

# 크롤링 값을 csv로 저장
# 스토어명_popular_연월일시.CSV로 저장
import datetime
today = storeNostr + '_' + 'POPULAR_' + datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
df.to_csv(f'd:/smartstore/{today}.csv', encoding="utf-8-sig")

# 누적판매순 으로 상위 80개 크롤링
# 쇼핑몰 전체상품을 보는 페이지로 url 지정
urlpre = "https://smartstore.naver.com/i/v1/stores/"
urlpost = "/categories/ALL/products"
url = urlpre + storeNostr + urlpost

# 참조 유튜브 : https://www.youtube.com/watch?v=DqtlR0y0suo
# javascript가 웹사이트에 보여주는 모양으로 값을 바꾸기 전 서버 json 데이터를 불러온다고 함. 유튜브 영상 참조.
querystring = {"categoryId": "ALL", "categorySearchType": "DISPCATG", "sortType": "TOTALSALE", "page": "1",
               "pageSize": "80"}
payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://smartstore.naver.com/loupe/category/2cffda4cfe7640df813533657a647ad5?st=TOTALSALE&dt=BIG_IMAGE&page=1&size=80",
    "Cookie": "NNB=7JHRUJKGXBPGI; ASID=af74dfd200000188194d6e5400000047",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

r = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# PANDAS 프레임워크 사용
import pandas as pd
res = []
data = r.json()

for p in data['simpleProducts']:
    res.append(p)

df = pd.json_normalize(res)


# 크롤링 값을 csv로 저장
# 스토어명_TOTALSALE_연월일시.CSV로 저장
import datetime
today = storeNostr+'_'+'TOTALSALE_'+datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
df.to_csv(f'd:/smartstore/{today}.csv', encoding="utf-8-sig")






# 이하 코드는 사용하려다 실패한 코드들. 참조용으로 남겨둠.

#--------------------------------------------------------------
# 글자 순서로 출력하는 방식. 스토어 명이 바뀌면 사용불가한 방법.폐기
# print('--- first method ---')
# print(all_scripts[0].get_text()[8343:8352])
# storeNo = json.loads(all_scripts[0].get_text()[8343:8352])
# storeNostr = str(storeNo)
# print(storeNo)
#--------------------------------------------------------------

#--------------------------------------------------------------
# 또 다른 출력 방법. 폐기
# print('key:', data.keys())
# print('key:', data['smartStoreV2'].keys())
# print('---')

# for item in data['smartStoreV2']:
#    print('channelNo:',item[0:19])
#--------------------------------------------------------------

#--------------------------------------------------------------
# 또 다른 출력 방법. 폐기
# print('--- second method ---')
# for number, script in enumerate(all_scripts):
#    if '{"smartStoreV2"' in script.text:
#        print(number, script.text[:100])
# jsonObj = None

# for s in scripts:
#    if 'window.__PRELOADED_STATE__ = ' in s.text:
#        script = s.text

# script = script.split('window.__PRELOADED_STATE__ = ')[0]
# script = script.split('/script')[0]
#
#        jsonStr = script
#        jsonObj = json.loads(jsonStr)

# for value in jsonObj['smartStoreV2']:
#   print ('ID: '+ (value['channelNo']))
>>>>>>> dea8f04f47c7d0f4fea00419f12e57d5b8e1d4c1
#--------------------------------------------------------------