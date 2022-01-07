# -*- coding: utf-8 -*- 

# selenium 안쓰고 request로 로그인 하는 법 (아직 성공 X)

import requests
from bs4 import BeautifulSoup
      
#세션만들기
session=requests.session()

#로그인 하는 페이지의 general-requestURL에서 url 가져옴
url="https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
      
#가져오고 싶은 데이터 (form data)
data={
    "return_url":"https://hisnet.handong.edu/for_student/main.php",
    "id":"아이디",
    "password":"비밀번호"       
}
response=session.post(url, data=data) #요청을 모방하면됨 (get, post, put 등)
      
#로그인 실행
response.raise_for_status()
      
url="https://hisnet.handong.edu/myboard/list.php?Board=NB0001"
response=session.get(url)
response.raise_for_status()
#print(response.text)
      
# #HTML분석 (이코인 가져오기)
# soup=BeautifulSoup(response.text,"html.parser")
# #body > table:nth-child(12) > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(17) > td:nth-child(2) > a
# text=soup.select_one(".mileage_section2 span").get_text()
# print("공지: ",text)