import requests
from bs4 import BeautifulSoup

#2017년부터 2021년까지만 가져옴
for year in range(2017,2022):
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={2021}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        # 이미지 링크를 받아올 때, 링크가 "https:" 가 아닌, "//" 로 시작할 경우 
        # "https://" 를 붙여서 가져올 수 있도록 설정
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        #movie_2017_1.jpg, movie_2018_2.jpg 등의 형식으로 이미지를 저장
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        # 상위 5개 이미지까지만 다운로드
        if idx >= 4:
            break