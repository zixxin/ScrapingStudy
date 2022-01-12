# -*- coding: utf-8 -*- 

# 공지 목록화면에서 각 공지를 클릭한 후, 공지 제목, 내용을 가져오는 코드
# 다음 페이지로 넘어갈 수 있는 코드도 포함되어 있음 (10페이지까지)

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
# 2022년 1월 1일부터 올라온 공지들만 스크래핑하여 파이어베이스 DB에 업로드

# 1페이지 내에 있는 모든 공지 목록 클릭하여 세부정보 받아오기
for i in range(17,32):
    # 공지 제목 클릭
    browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[{0}]/td[2]/a'.format(i)).click()
    # # 공지 번호 클릭
    # browser.find_element('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[17]/td[1]/div/a')
    time.sleep(1)

    # print("\n")
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

# 다음 페이지로 넘어가기
for i in range(1,5):
    # 1페이지에 있을 때, 02는 a[1], (2페이지 이상) a페이지에 있을 때, 다음은 a[i+1]
    if i == 1:
        browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[4]/td/table/tbody/tr/td/div/a[1]/font').click()
        time.sleep(1)

        # # 페이지 내에 있는 모든 공지 목록 클릭하여 세부정보 받아오기
        # for i in range(17,32):
        #     browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[{0}]/td[2]/a'.format(i)).click()
        #     time.sleep(1)

        #     print("\n")
        #     noti_title = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/span[2]")
        #     print("[ "+ noti_title.text +" ]\n")
        #     noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[3]/td/table/tbody/tr/td")

        #     for i in range(1,6):
        #         if noti_info.text.encode('UTF-8', 'ignore') == "첨부 #1":
        #             noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[{0}]/td/table/tbody/tr/td".format(i+3))
        #         else:
        #             noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[{0}]/td/table/tbody/tr/td".format(i+2))
        #             break

        #     print(noti_info.text)
        #     print("\n")

        #     browser.find_element_by_xpath('//*[@id="divReadButton"]/a/img').click()
        #     time.sleep(1)
    else:
        browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[4]/td/table/tbody/tr/td/div/a[{0}]/font'.format(i+1)).click()
        time.sleep(1)

        # # 페이지 내에 있는 모든 공지 목록 클릭하여 세부정보 받아오기
        # for i in range(17,32):
        #     browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[{0}]/td[2]/a'.format(i)).click()
        #     time.sleep(1)

        #     print("\n")
        #     noti_title = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/span[2]")
        #     print("[ "+ noti_title.text +" ]\n")
        #     noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[3]/td/table/tbody/tr/td")

        #     for i in range(1,6):
        #         if noti_info.text.encode('UTF-8', 'ignore') == "첨부 #1":
        #             noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[{0}]/td/table/tbody/tr/td".format(i+3))
        #         else:
        #             noti_info = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td/table/tbody/tr[{0}]/td/table/tbody/tr/td".format(i+2))
        #             break

        #     print(noti_info.text)
        #     print("\n")

        #     browser.find_element_by_xpath('//*[@id="divReadButton"]/a/img').click()
        #     time.sleep(1)