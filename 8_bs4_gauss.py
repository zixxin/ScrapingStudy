# -*- coding: utf-8 -*- 

# 특정 웹툰 하나를 선택
#   그 웹툰 내 원하는 회차의 제목을 끌어올 수 있음
#   회차의 링크를 끌어와서, 그 링크를 클릭하면 해당 회차 페이지로 바로 접속할 수 있도록 하는 기능 학습 및 실습
#   해당 웹툰 내 모든 회차의 제목과 링크를 끌어올 수 있음
#   해당 웹툰 내 모든 회차의 평점을 끌어와서, 그 data를 가지고 해당 웹툰의 평점 평균을 낼 수 있음
# 굳이 vscode 프로그램을 통해 코드를 실행하지 않아도, 터미널을 통하여 해당 코드를 수정해가면서 작성하고, 실행할 수 있음

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=sun"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
cartoons = soup.find_all("td", attrs={"class":"title"})
title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]
print(title)
print("https://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
for cartoon in cartoons:
    title = cartoon[0].a.get_text()
    link = cartoon[0].a["href"]

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates . len(cartoons))