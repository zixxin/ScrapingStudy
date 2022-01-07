#-*- coding: utf-8 -*- 

# import requests
# from bs4 import BeautifulSoup
# from bs4 import BeautifulSoup as bs

# url = "https://hisnet.handong.edu/myboard/list.php?Board=NB0001"
# res = requests.get(url)
# res.raise_for_status()

# LOGIN_URL = "https://hisnet.handong.edu/"
# LOGIN_DATA = {
#     'id': 'id',
#     'password': 'password'
# }
# with requests.Session() as s:
#     res = s.post(LOGIN_URL, data=LOGIN_DATA, verify=False, allow_redirects=False)

#     # 쿠키와 헤더에 포함된 302 Location 값을 가져온다.
#     # 이때, 헤더에 설정된 쿠키와 함께 Location으로 Get Request 를 보내면 된다.
#     redirect_cookie = res.headers['Set-Cookie']
#     redirect_url = res.headers['Location']
#     headers = {"Cookie": redirect_cookie}

#     # Location 주소로 Get Request 호출
#     s.get(redirect_url, headers=headers)

# soup = BeautifulSoup(res.text, "html.parser")

# # 전체 목록 가져오기
# notices = soup.find_all("a", attrs={"class":"listBody"})
# # class 속성이 listBody 인 모든 "a" element 반환
# for notice in notices:
#     print(notice.get_text())

#from urllib.parse import urljoin 
import requests 
from bs4 import BeautifulSoup 
#import urllib.request as req 

user = 'id' 
pw = 'password' 

sess = requests.session() 

login = { 
    'email': user, 
    'password': pw 
} 

url = 'https://hisnet.handong.edu/' 
res = sess.post(url, data=login) 
res.raise_for_status() 

# url_p = 'https://hisnet.handong.edu/myboard/list.php?Board=NB0001' 
# res = sess.get(url_p) 
# res.raise_for_status() 

soup = BeautifulSoup(res.text, 'html.parser') 
print(soup.html.body)
