# -*- coding: utf-8 -*- 

# 한동대학교 홈페이지 공지 정보 불러오기

import requests
from bs4 import BeautifulSoup

url = "https://hisnet.handong.edu/myboard/list.php?Board=NB0001"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 공지 목록 가져오기
notice = soup.find_all("a", attrs={"class":"listBody"})
# class 속성이 title al 인 모든 "td" element 반환
for noti in notice:
    print(noti.get_text())