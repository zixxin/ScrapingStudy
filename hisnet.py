# -*- coding: utf-8 -*- 

# Hisnet 홈페이지 공지 정보 불러오기 + 파이어베이스 db에 저장하기
# 따로 파일을 만들어서 정보를 저장하지 않아도, 파이어베이스에 바로 올리는 방법 찾음!
# 현재 반복문은 돌아가지만, 데이터가 하나만 올라가는 상태라 수정 필요함!
# firebase_admin 오류 해결 X !!!

import time
import re
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import firestore
 
# # Firebase database 인증 및 앱 초기화
# cred = credentials.Certificate("pleasedothat-f843e-firebase-adminsdk-fut4j-eba096203d.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL' : 'https://pleasedothat-f843e-default-rtdb.firebaseio.com/'
# })
# db = firestore.client()

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

# 일반 공지 메뉴 클릭
browser.find_element_by_xpath('//*[@id="td_box22_img"]').click()

# 더보기 클릭
browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table[1]/tbody/tr/td[2]/div/a/img').click()
time.sleep(1)

# 히즈넷 일반공지 게시판 목록 1페이지 화면까지 들어온 상태

# 공지 번호, 공지 제목 불러오기
for i in range (123, 200):
    # 공지 번호
    notis = soup.find_all("a")[i].string
    notis = re.sub('^[0-9]{0,3}$', '', notis)

    # 공지 제목
    notis_title = soup.find_all("a")[i+1].string
    i = i + 1

    # notis_list.append(notis)

    # 중간에 의미없는 빈칸 없애기
    if notis == '':
        continue
    else:
        print(notis)

    # 파이어베이스 db 'general' 컬렉션 안에 데이터 저장
    # doc_ref = db.collection(u'general').document(notis)
    # doc_ref.set({
    #     u'title': notis_title,
    # })