#-*-coding:euc-kr
"""
update programmer : Juhyun Kim
GitHub : https://github.com/xenocurrency
update : 2023.11.23
===================================================================
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class ImgCrawler:
    def __init__(self, out_dir):
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.google.co.in/search?tbm=isch&q="
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� ��帮���� ����մϴ�. �ּ��� �����ϸ� ��帮���� �۾��� ����˴ϴ�.
        # self.options.add_argument("--headless=new")
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1024,768")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome()
        # ������� ������ ���͸��� ����մϴ�.
        self.out_dir = out_dir

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # Ű���带 ���� �̹������� �˻��ϴ� �Լ��Դϴ�.
    def search_image(self, keyword):
        self.driver.get(self.querry + keyword)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �̹��� �˻� ȭ���� ��ũ�� �ٿ��ϴ� �Լ��Դϴ�.
    def scroll_down(self):
        # ����Ʈ�� ������ <body> �±׸� ã���ϴ�.
        body = self.driver.find_element(By.TAG_NAME, "body")
        # ���� ���� ��ũ���� �սô�.
        for i in range(50):
            body.send_keys(Keys.END)
            time.sleep(0.5)
        # �ٽ� �� ���� �ö󰩽ô�. ��� ������� �ִ°̴ϴ�. ��� �˴ϴ�.
        body.send_keys(Keys.HOME)

    # �̹��� �˻� ���â�� ��� �̹����� �ܾ���� �Լ��Դϴ�.
    def crawl_pictures(self, num):
        # ���� �˻��� �ʱ⿡ �̹��� �˻� ����� �Ϻθ� ǥ���մϴ�.
        # ��ũ���� �� �Ʒ����� ������ ������ �߰��� �ε��մϴ�.
        # ������ ��ǻ�� �������� �� 400���� ������ ǥ��˴ϴ�.
        self.scroll_down()
        # <img> �±׸� �����ִ� ��� ��Ҹ� �ҷ��ɽô�.
        img_elements = self.driver.find_elements(By.TAG_NAME, "img")
        # for ���� �̿��� �� ��ҵ��� �ϳ��ϳ� �ٿ�޽��ϴ�.
        for i, el in enumerate(img_elements):
            # �ʱ� ������ ������ŭ ������ �ٿ�޾Ҵٸ� ������ ���� �ݴϴ�.
            if i == num:
                break
            # ȭ���� �ų��� ��½�̸鼭 �ٿ�ε�˴ϴ�.
            el.screenshot(self.out_dir + "/" + str(i) + ".png")
            time.sleep(0.1)
        # ��û���� �������� ������ �� ���� �ٿ�޾Ҵٸ�
        if i < num:
            # Ű���带 �ٲ㼭 �ٽ� �˻��� �޶�� �޽����� ����մϴ�.
            print("Not enough search result. Please change the keyword and try again.")

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� ���� �˻��ϰ�, �̹��� ũ�Ѹ��ϴ� �Լ��� ����ϴ�.
    def crawl_images(self, keyword, num):
        # �̹��� �˻��� �����մϴ�.
        self.search_image(keyword)
        # �۾��� �����մϴ�.
        self.crawl_pictures(num)
