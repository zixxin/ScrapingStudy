# 여기서부터 firebase 연결
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

 
# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate("pleasedothat-f843e-firebase-adminsdk-fut4j-e7d1463897.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://pleasedothat-f843e-default-rtdb.firebaseio.com/'
})
# ref = db.reference() # 기본 위치 지정 realtime firebase
db = firestore.client() # firestore firebase settings
# 여기까지 파이어베이스 연결


# 텍스트 파일로 저장되어 있는 공지 정보를 firebase에 업로드
f = open("noti.txt", "rt") # 번호랑 제목만 있는 txt file
con_f = open("noti_final.txt", "rt") # 내용이 있는 txt file

cnt = 0
noti = ""
noti_title = ""
content = ""

while True:
    content = "" # 공지 내용 담는 변수 초기화
    temp = f.readline()

    # 번호랑 제목만 업로드하는 코드
    if cnt % 2 == 0:
        noti = temp
        print(noti, end='')
        cnt = cnt + 1

    else:
        noti_title = temp
        print(noti_title, end='')
        cnt = cnt + 1

    if temp == "":
        break

    con_temp = con_f.readline()
    if con_temp.startswith("???"): # 하나의 내용이 시작함을 알려주는 표지
        # noti_title = con_temp
        continue
    else:
        while True:
            if (con_temp.startswith("???")): # 하나의 내용이 끝났음을 알려주는 표지
                break
            else:
                con_temp = con_f.readline()
                content += con_temp   

    doc_ref = db.collection(u'general').document(noti)
    doc_ref.set({
        u'title': noti_title,
        u'content':content,
    })

f.close()
con_f.close()