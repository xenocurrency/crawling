#-*-coding:euc-kr

# 코딩 목적 : 나이키 홈페이지의 '용품' 카테고리 내 1페이지 상품명을 추출

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#나이키 용품 카테고리 url
url = "https://www.nike.com/kr/w/men-accessories-equipment-awwpwznik1"

utility = driver.get(url)
#대기 시간 설정
time.sleep(3)

#상품 정보 클래스 선택
product_db = driver.find_elements(By.CLASS_NAME, "product-card__body")

temp_product_text = []
#타이틀 저장 csv 파일인 "title.csv" 생성
outfile = open("titles.csv",'w')

for i in range(len(product_db)):
    product = product_db[i]         #product_db 클래스 중 하나 추출
    temp_product_text = product.text            #클래스 내 텍스트만 추출
    temp_title = temp_product_text.split("\n")          #텍스트 줄 별로 나눔
    title = temp_title[0]           #나눈 텍스트 첫번째가 대표 상품명
    outfile.write("\n" + title)         #대표상품명을 csv파일로 저장
    title = temp_title[2]  # 나눈 텍스트 세번째가 세부 상품명
    outfile.write(" " + title)  # 세부 상품명을 대표 상품명 옆에 csv파일로 저장


#csv 파일 닫기
outfile.close