#-*-coding:euc-kr

# �ڵ� ���� : ����Ű Ȩ�������� '��ǰ' ī�װ� �� 1������ ��ǰ���� ����

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#����Ű ��ǰ ī�װ� url
url = "https://www.nike.com/kr/w/men-accessories-equipment-awwpwznik1"

utility = driver.get(url)
#��� �ð� ����
time.sleep(3)

#��ǰ ���� Ŭ���� ����
product_db = driver.find_elements(By.CLASS_NAME, "product-card__body")

temp_product_text = []
#Ÿ��Ʋ ���� csv ������ "title.csv" ����
outfile = open("titles.csv",'w')

for i in range(len(product_db)):
    product = product_db[i]         #product_db Ŭ���� �� �ϳ� ����
    temp_product_text = product.text            #Ŭ���� �� �ؽ�Ʈ�� ����
    temp_title = temp_product_text.split("\n")          #�ؽ�Ʈ �� ���� ����
    title = temp_title[0]           #���� �ؽ�Ʈ ù��°�� ��ǥ ��ǰ��
    outfile.write("\n" + title)         #��ǥ��ǰ���� csv���Ϸ� ����
    title = temp_title[2]  # ���� �ؽ�Ʈ ����°�� ���� ��ǰ��
    outfile.write(" " + title)  # ���� ��ǰ���� ��ǥ ��ǰ�� ���� csv���Ϸ� ����


#csv ���� �ݱ�
outfile.close