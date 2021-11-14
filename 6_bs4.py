# BeautifulSoup4
# 	네이버 웹툰 홈페이지에서 메뉴 정보들을 끌어오거나, 
#   태그 간의 이동을 활용하여 인기 웹툰 순위 정보를 끌어오는 방법을 배우고 실습을 통해 결과를 확인할 수 있음

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs) # a element의 속성 정보 출력
print(soup.a["href"]) # a element의 href 속성 '값' 정보 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 a element를 찾아줘
print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 어떤 element를 찾아줘

print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())
print(rank1.next_sibling)
rank2 = rank1.next_sibling.next_sibling # rank2 기준으로 다음 순위(rank3)를 가져옴
rank3 = rank2.next_sibling.next_sibling # rank3 기준으로 다음 순위(rank4)를 가져옴
print(rank3.a.get_text())
print(rank1.parent)
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

print(rank1.find_next_siblings("li")) # rank1 기준으로 다음 순위들을 모두 가져옴

webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마")
print(webtoon)