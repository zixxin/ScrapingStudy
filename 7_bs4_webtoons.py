# -*- coding: utf-8 -*- 

# 네이버 웹툰 페이지 내 요일별 전체 웹툰 목록에 있는 모든 웹툰의 제목 정보를 끌어오는 기능
#   사용자가 원하는 속성에 알맞는 element 를 끌어올 수 있음

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title 인 모든 "a" element 반환
for cartoon in cartoons:
    print(cartoon.get_text())