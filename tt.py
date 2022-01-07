# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup
      
#세션만들기
session=requests.session()
#로그인 하는 페이지의 general-requestURL에서 url 가져옴
url="https://www.hanbit.co.kr/member/login.html"
      
#가져오고 싶은 데이터 (form data)
data={
    "return_url":"http://www.hanbit.co.kr/index.html",
    "m_id":"id",
    "m_passwd":"pw" 
}
response=session.post(url, data=data) #요청을 모방하면됨 (get, post, put 등)
      
#로그인 실행
response.raise_for_status()
      
      
# #마이페이지 접근
# url="http://www.hanbit.co.kr/myhanbit/myhanbit.html"
# response=session.get(url)
# response.raise_for_status()
# #print(response.text)
      
# #HTML분석 (이코인 가져오기)
# soup=BeautifulSoup(response.text,"html.parser")
# #container > div > div.sm_mymileage > dl.mileage_section2 > dd
# text=soup.select_one(".mileage_section2 span").get_text()
# print("이코인:",text)