import requests

res = requests.get("https://hisnet.handong.edu")
# res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f: 
    f.write(res.text)