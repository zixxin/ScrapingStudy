# http method
#   GET 방식
#       어떠한 내용을 누구나 볼 수 있게, url에 적어서 보내는 방식
#       링크 “?” 뒤에 변수와 값이 위치해있음
#       각 변수와 값들은 “&”로 구분
#       한번 전송할 때 보낼 수 있는 data 양이 제한되어 있어서 큰 data는 보낼 수 없음
#   POST 방식
#       url이 아닌, http message body에 적어서 보내는 방식
#       GET 방식에 비해 안전함
#       큰 data 전송 가능
#       페이지는 변하지만, 링크가 변하지 않는 경우에 해당함
# 쿠팡 페이지
#   원하는 상품의 제품명, 가격, 평점, 평점 수 등의 정보를 끌어올 수 있음
#   광고성 제품은 제외하고, 이 외의 상품 정보만 끌어오는 기능
#   평점이 높고, 리뷰 수가 많은 상품의 정보만 끌어오는 기능

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/campaigns/82/components/178155"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:
    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("<광고 상품 제외합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

    # 애플 제품 제외
    if "Apple" in name:
        print("<Apple 상품 제외합니다>")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        print("<평점 없는 상품 제외합니다>")
        continue
    
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 예 : (26)
        rate_cnt = rate_cnt[1:-1]
        print("리뷰 수: ", rate_cnt)
    else:
        print("<평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 50:
        print(name, price, rate, rate_cnt)