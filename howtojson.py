# -*- coding: utf-8 -*- 

# json 파일 형식으로 프린트하는 법
# 굳이 파일을 따로 만들어서 저장하지 않아도, 파이어베이스에 바로 데이터를 올릴 수 있는 방법을 찾아 이 방법은 더 이상 시도하지 않을 예정

import requests
from bs4 import BeautifulSoup

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = requests.get(url)
print(res.status_code)
html = res.text
soup = BeautifulSoup(html, 'html.parser')

# dict에 저장
location_dict = {}

location_one = soup.find('a')

data_list = []
for data in location_one:
    data_dict = dict() #{}
    data_dict['number'] = data.find('number').text
    data_dict['title'] = data.find('title').text
    
    data_list.append(data_dict)
    # print(data_dict)
    
# print(data_list)
location_dict['datas'] = data_list
print(location_dict)