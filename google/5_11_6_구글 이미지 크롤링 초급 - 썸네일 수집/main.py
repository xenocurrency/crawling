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

import sys
import os
import time
import google_image_crawler as ic


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ ������ ������ ���͸��� �Է¹޽��ϴ�.
out_dir = sys.argv[1]

# �˻��� Ű���带 �Է¹޽��ϴ�.
keyword = sys.argv[2]

# ������ �̹��� ������ �Է¹޽��ϴ�.
number = int(sys.argv[3])

# ������� ������ ������ �����մϴ�.
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = ic.ImgCrawler(out_dir)

# ũ�ѷ����� �̹��� ũ�Ѹ��� ��ŵ�ϴ�.
BOT.crawl_images(keyword, number)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
