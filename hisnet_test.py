# -*- coding: utf-8 -*- 

import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화

url = "https://hisnet.handong.edu/login/login.php"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(browser.page_source, "html.parser")

# 히즈넷 접속
browser.get(url)
time.sleep(1)

# 히즈넷 아이디 입력
browser.find_element_by_xpath('//*[@id="loginBoxBg"]/table[2]/tbody/tr/td[5]/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/span/input').send_keys("id")

# 히즈넷 비밀번호 입력
browser.find_element_by_xpath('//*[@id="loginBoxBg"]/table[2]/tbody/tr/td[5]/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/input').send_keys("password")
time.sleep(1)

# 로그인 버튼 클릭
browser.find_element_by_xpath('//*[@id="loginBoxBg"]/table[2]/tbody/tr/td[5]/form/table/tbody/tr[3]/td/table/tbody/tr/td[2]/input').click()
time.sleep(1)

# 히즈넷 로그인 성공 후 메인화면까지 들어온 상태

# 일반 공지 메뉴 클릭
browser.find_element_by_xpath('//*[@id="td_box22_img"]').click()

# 더보기 클릭
browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table[1]/tbody/tr/td[2]/div/a/img').click()
time.sleep(1)

# 히즈넷 일반공지 게시판 목록 화면까지 들어온 상태

# 1페이지 내에 있는 모든 공지 목록 클릭하여 세부정보 받아오기
for i in range(17,32):
    browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[{0}]/td[2]/a'.format(i)).click()
    time.sleep(1)

    print("\n")
    noti_title = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/span[2]")
    print("[ "+ noti_title.text +" ]\n")
    noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[3]/td/table/tbody/tr/td")

    for i in range(1,6):
        if noti_info.text.encode('UTF-8', 'ignore') == "첨부 #1":
            noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[{0}]/td/table/tbody/tr/td".format(i+3))
        else:
            noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[{0}]/td/table/tbody/tr/td".format(i+2))
            break

    print(noti_info.text)
    print("\n")

    browser.find_element_by_xpath('//*[@id="divReadButton"]/a/img').click()
    time.sleep(1)

# # 첫 번째 공지 클릭
# browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr{i}/td[1]/div/a').click()
# time.sleep(1)

# # 첫 번째 공지 상세 정보 text 불러오기
# print("\n")
# noti_title1 = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/span[2]")
# print("[ "+ noti_title1.text +" ]\n")
# noti_info1 = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[4]/td/table/tbody/tr/td")
# print(noti_info1.text)
# print("\n")

# # 공지 목록 list로 돌아가기
# browser.find_element_by_xpath('//*[@id="divReadButton"]/a/img').click()
# time.sleep(1)

# # 두 번째 공지 클릭
# browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[18]/td[1]/div/a').click()
# time.sleep(1)

# # 두 번째 공지 상세 정보 text 불러오기
# noti_title2 = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/span[2]")
# print("[ "+ noti_title2.text +" ]\n")
# noti_info2 = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[3]/td/table/tbody/tr/td")
# print(noti_info2.text)
# print("\n")