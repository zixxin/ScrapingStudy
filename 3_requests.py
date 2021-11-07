import requests

res = requests.get("https://hisnet.handong.edu")
print("응답코드 :", res.status_code)