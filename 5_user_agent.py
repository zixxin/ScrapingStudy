# User Agent
# 	접속하는 브라우저에 따라 user agent가 다르며, 
#   이 값에 따라 정보를 다르게 받아올 수 있음, 
#   웹 스크래핑에 필요한 중요한 기능

import requests

url = "http://nadocoding/tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f: 
    f.write(res.text)