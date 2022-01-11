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
f = open("noti.txt", "rt")

cnt = 0
noti = ""
noti_title = ""

while True:
    temp = f.readline()

    if cnt % 2 == 0:
        noti = temp
        print(noti, end='')
        cnt = cnt + 1

    else:
        noti_title = temp
        print(noti_title, end='')
        cnt = cnt + 1

    if temp == '':
        break

    doc_ref = db.collection(u'general').document(noti)
    doc_ref.set({
        u'title': noti_title,
    })

f.close()