# -*- coding: utf-8 -*- 

# 드디어 ,,, 셀레니엄이 돌아가기 시작했다 ,,,, 감격의 눈물 ,,,,,
# sudo easy_install selenium

import time
from selenium import webdriver
import requests

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화

url = "https://hisnet.handong.edu/login/login.php"
res = requests.get(url)
res.raise_for_status()

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

# 일반 공지 메뉴 클릭
browser.find_element_by_xpath('//*[@id="td_box22_img"]').click()

# 더보기 클릭
browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table[1]/tbody/tr/td[2]/div/a/img').click()
time.sleep(1)

# 히즈넷 일반공지 게시판 목록 화면까지 들어온 상태